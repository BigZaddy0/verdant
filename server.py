import json
import os
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
API_KEY = os.environ.get("NVIDIA_API_KEY", "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")
WHATSAPP_LINK = "https://whas.me/GsfTPbvQek"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY,
)


def clean_text(html: str) -> str:
    html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    html = html.replace("&nbsp;", " ").replace("&amp;", " & ").replace("&#39;", "'")
    text = re.sub(r"\s+", " ", html).strip()
    return text[:4000]


def build_site_context() -> str:
    pages = []
    for path in sorted(ROOT.glob("*.html")):
        try:
            html = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        title_match = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
        title = title_match.group(1).strip() if title_match else path.stem
        text = clean_text(html)
        if text:
            pages.append(f"Page: {path.name}\nTitle: {title}\nContent: {text}")
    return "\n\n".join(pages[:20])


def fallback_reply(message: str, context: str) -> str:
    text = message.lower()
    if any(term in text for term in ["human", "representative", "agent", "speak to", "talk to", "contact"]):
        return f"I can connect you to a human representative through WhatsApp: {WHATSAPP_LINK}"
    if any(term in text for term in ["price", "cost", "budget", "plot", "land", "cheapest", "cheap"]):
        if "8.250m" in context.lower() or "5m" in context.lower() or "2m" in context.lower() or "7m" in context.lower() or "400k" in context.lower():
            return "The website shows several property options with prices such as 8.25M, 5M, 2M, 7M, and 400K depending on the property. The most affordable option currently listed is Treasure Home at 400K."
        return "I can help you review the listed property options and pricing on the site. If you want a direct answer for a specific property, tell me the property name."
    if any(term in text for term in ["company", "about", "who", "verdant"]):
        return "Verdant World Global Limited is a real estate company focused on helping customers buy land and properties, with a strong emphasis on affordable offers and customer support."
    if any(term in text for term in ["visit", "viewing", "tour", "site", "inspection"]):
        return "You can request a site visit or inspection through the sales team. If you want a human representative, use the WhatsApp link: " + WHATSAPP_LINK
    if any(term in text for term in ["document", "title", "survey", "deed", "allocation"]):
        return "We can help you review title documents, allocation details, survey information, and the paperwork process. A sales representative can guide you further."
    if any(term in text for term in ["installment", "monthly", "payment", "plan"]):
        return "Yes, installment and payment plans are part of what we discuss with buyers. I can help you ask about the available options and connect you with an advisor."
    if any(term in text for term in ["lagos", "ogun", "location", "near", "lekki"]):
        return "We have estates and properties in several locations. I can help you narrow it down by state, budget, or preferred area such as Lagos or Ogun."
    if any(term in text for term in ["download", "brochure"]):
        return "You can download the land brochure here: /img/Landform.pdf"
    return "I can answer questions about property prices, company information, available estates, inspections, documents, and payment plans. For a human representative, you can contact sales on WhatsApp: " + WHATSAPP_LINK


class ChatHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path.startswith("/api/chat"):
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8")
            try:
                payload = json.loads(body or "{}")
            except json.JSONDecodeError:
                payload = {}

            message = (payload.get("message") or "").strip()
            page_context = payload.get("pageText") or ""
            site_context = build_site_context()
            combined_context = f"Current page: {payload.get('pageTitle', '')}\n{page_context[:3000]}\n\nWebsite context:\n{site_context}"

            history = payload.get("history") or []
            reply = None
            try:
                completion = client.chat.completions.create(
                    model="deepseek-ai/deepseek-v4-pro",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a friendly AI property consultant for Verdant World Global Limited. Use the supplied website context. You know these estates: Treasure Island, New Life Garden, Desire Home, Harmony Home, Country Home, Country Home Extension, Treasure Home, Irewamiri Garden, Mega City, Florish Home, Iremide Garden. You can answer about prices, locations, plot size, installment options, infrastructure, titles, payment process, inspections, and brochure downloads. If the visitor wants to buy, wants to talk to a human, asks for inspection, or asks for a lead form, respond warmly and ask for the next needed detail. If the user asks for a human representative, direct them to WhatsApp: https://whas.me/GsfTPbvQek. Be conversational and helpful."
                        },
                        {
                            "role": "user",
                            "content": f"User question: {message}\n\nConversation history:\n{json.dumps(history[-8:], ensure_ascii=False)}\n\nWebsite context:\n{combined_context}"
                        }
                    ],
                    temperature=1,
                    top_p=0.95,
                    max_tokens=16384,
                    extra_body={"chat_template_kwargs": {"thinking": False}},
                )
                reply = completion.choices[0].message.content.strip()
            except Exception:
                reply = fallback_reply(message, combined_context)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"reply": reply}).encode("utf-8"))
            return

        self.send_error(404)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in ["", "/"]:
            path = "/index.html"
        if path.startswith("/api/"):
            self.send_error(404)
            return

        file_path = (ROOT / path.lstrip("/")).resolve()
        if not str(file_path).startswith(str(ROOT)):
            self.send_error(403)
            return
        if not file_path.exists() or not file_path.is_file():
            self.send_error(404)
            return

        content_type = "application/octet-stream"
        if file_path.suffix == ".html":
            content_type = "text/html; charset=utf-8"
        elif file_path.suffix == ".css":
            content_type = "text/css; charset=utf-8"
        elif file_path.suffix == ".js":
            content_type = "application/javascript; charset=utf-8"
        elif file_path.suffix == ".json":
            content_type = "application/json; charset=utf-8"
        elif file_path.suffix == ".png":
            content_type = "image/png"
        elif file_path.suffix == ".jpg" or file_path.suffix == ".jpeg":
            content_type = "image/jpeg"
        elif file_path.suffix == ".svg":
            content_type = "image/svg+xml"
        elif file_path.suffix == ".pdf":
            content_type = "application/pdf"

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(file_path.read_bytes())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), ChatHandler)
    print(f"Serving Verdant site on http://127.0.0.1:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server")
        server.server_close()
