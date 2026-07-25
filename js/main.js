(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.nav-bar').addClass('sticky-top');
        } else {
            $('.nav-bar').removeClass('sticky-top');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 24,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });

    // Events and awards carousel
    $(".events-awards-carousel").owlCarousel({
        autoplay: true,
        autoplayTimeout: 6000,
        smartSpeed: 800,
        items: 1,
        dots: true,
        loop: true,
        nav: true,
        navText: [
            '<span aria-hidden="true"><i class="bi bi-arrow-left"></i></span><span class="event-nav-label">Previous</span>',
            '<span class="event-nav-label">Next</span><span aria-hidden="true"><i class="bi bi-arrow-right"></i></span>'
        ]
    });

    // Customer support chatbot widget
    var chatWidget = $('<div class="chatbot-widget"></div>');
    var chatPanel = $('<div class="chatbot-panel" id="chatbotPanel"></div>');
    var chatMessages = $('<div class="chatbot-messages" id="chatbotMessages" aria-live="polite"></div>');
    var quickActions = $('<div class="chatbot-quick-actions"></div>');
    var chatForm = $(
        '<form class="chatbot-input-row" id="chatbotForm">' +
            '<input type="text" id="chatbotInput" placeholder="Ask about estates, prices, or inspections..." autocomplete="off">' +
            '<button type="submit"><i class="bi bi-send-fill"></i></button>' +
        '</form>'
    );

    chatPanel.append(
        '<div class="chatbot-header">' +
            '<div><h6>Verdant Support</h6><p>AI Property Consultant • WhatsApp ready</p></div>' +
            '<button type="button" class="chatbot-close" id="chatbotClose" aria-label="Close chat"><i class="bi bi-x-lg"></i></button>' +
        '</div>'
    );
    chatPanel.append(chatMessages);
    chatPanel.append(quickActions);
    chatPanel.append(chatForm);

    

    var whatsappLink = 'https://whas.me/GsfTPbvQek';
    var pageTitle = document.title || 'Verdant World Global Limited';
    var pageText = $('body').text().replace(/\s+/g, ' ').trim().slice(0, 4000);
    var chatState = {
        lead: {},
        collectingLead: null,
        collectingInspection: null,
        history: []
    };

    var suggestionList = [
        'Show available estates',
        'Cheapest land',
        'Estates in Lagos',
        'Estates in Ogun',
        'Payment plan',
        'Book inspection',
        'Speak with an agent',
        'Download Landform'
    ];
    var estateData = null;

    function getTimestamp() {
        var now = new Date();
        return now.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
    }

    function escapeHTML(value) {
        return String(value)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function saveHistory() {
        try {
            localStorage.setItem('verdantChatHistory', JSON.stringify(chatState.history));
        } catch (e) {
            // Ignore storage errors
        }
    }

    function loadHistory() {
        try {
            var stored = localStorage.getItem('verdantChatHistory');
            if (stored) {
                var parsed = JSON.parse(stored);
                if (Array.isArray(parsed)) {
                    chatState.history = parsed;
                    parsed.forEach(function (item) {
                        addMessage(item.text, item.type, { meta: item.meta, silent: true });
                    });
                }
            }
        } catch (e) {
            chatState.history = [];
        }
    }

    function addMessage(text, type, options) {
        options = options || {};
        if (!options.silent) {
            var bubble = $('<div class="chatbot-bubble ' + type + '"></div>');
            var content = $('<div class="chatbot-bubble-content"></div>');
            content.html(escapeHTML(text).replace(/\n/g, '<br>'));
            bubble.append(content);
            if (options.meta) {
                bubble.append($('<div class="chatbot-meta"></div>').text(options.meta));
            }
            chatMessages.append(bubble);
            chatMessages.scrollTop(chatMessages[0].scrollHeight);
            chatState.history.push({ text: text, type: type, meta: options.meta || getTimestamp() });
            saveHistory();
        }
    }

    function showTyping() {
        var typingBubble = $('<div class="chatbot-bubble bot typing" id="typingBubble">Thinking...</div>');
        chatMessages.append(typingBubble);
        chatMessages.scrollTop(chatMessages[0].scrollHeight);
        return typingBubble;
    }

    function renderSuggestions() {
        quickActions.empty();
        quickActions.append('<div class="chatbot-suggestion-title">Suggested questions</div>');
        var chipRow = $('<div class="chatbot-chip-row"></div>');
        suggestionList.forEach(function (item) {
            chipRow.append('<button class="chatbot-chip" type="button" data-reply="' + item + '">' + item + '</button>');
        });
        quickActions.append(chipRow);
    }

    function hideSuggestions() {
        quickActions.hide();
    }

    function showSuggestions() {
        quickActions.show();
    }

    function loadEstateData() {
        if (estateData) {
            return;
        }
        fetch('property-list.html')
            .then(function (response) {
                return response.text();
            })
            .then(function (html) {
                var parser = new DOMParser();
                var doc = parser.parseFromString(html, 'text/html');
                var cards = Array.from(doc.querySelectorAll('.property-item'));
                estateData = cards.map(function (card) {
                    var name = card.querySelector('.d-block.h5') ? card.querySelector('.d-block.h5').textContent.trim() : '';
                    var price = card.querySelector('.text-primary.mb-3') ? card.querySelector('.text-primary.mb-3').textContent.trim() : '';
                    var location = card.querySelector('p') ? card.querySelector('p').textContent.replace(/\s+/g, ' ').trim() : '';
                    return { name: name, price: price, location: location };
                }).filter(function (item) {
                    return item.name;
                });
            })
            .catch(function () {
                estateData = [];
            });
    }

    function getEstateSummary(message) {
        if (!estateData) {
            return null;
        }
        var lower = message.toLowerCase();
        if (lower.indexOf('available estates') >= 0 || lower.indexOf('available estate') >= 0) {
            return estateData.slice(0, 8).map(function (item) {
                return item.name + ' — ' + item.price + ' — ' + item.location;
            }).join('\n');
        }
        if (lower.indexOf('cheapest') >= 0 || lower.indexOf('cheap') >= 0) {
            var cheapest = estateData.slice().sort(function (a, b) {
                var av = parseFloat((a.price || '').replace(/[^0-9.]/g, '')) || 999999;
                var bv = parseFloat((b.price || '').replace(/[^0-9.]/g, '')) || 999999;
                return av - bv;
            })[0];
            return cheapest ? cheapest.name + ' — ' + cheapest.price + ' — ' + cheapest.location : 'No listing found';
        }
        if (lower.indexOf('lagos') >= 0) {
            var lagos = estateData.filter(function (item) {
                return /lagos/i.test(item.location);
            });
            return lagos.length ? lagos.slice(0, 6).map(function (item) {
                return item.name + ' — ' + item.price + ' — ' + item.location;
            }).join('\n') : 'No Lagos listings were found in the current property list.';
        }
        if (lower.indexOf('ogun') >= 0) {
            var ogun = estateData.filter(function (item) {
                return /ogun/i.test(item.location);
            });
            return ogun.length ? ogun.slice(0, 6).map(function (item) {
                return item.name + ' — ' + item.price + ' — ' + item.location;
            }).join('\n') : 'No Ogun listings were found in the current property list.';
        }
        return null;
    }

    function askLeadQuestion(field) {
        var prompts = {
            name: 'Great! What is your full name?',
            phone: 'Please share your phone number so we can contact you.',
            email: 'What is your email address?',
            location: 'Which preferred location are you interested in?',
            budget: 'What is your budget for this purchase?',
            purpose: 'Are you buying for residential, investment, or commercial use?',
            timeline: 'When do you want to move forward? Choose immediately, 1 month, 3 months, or 6 months.'
        };
        addMessage(prompts[field] || 'Please continue with your details.', 'bot', { meta: getTimestamp() });
    }

    function parseLeadField(field, message) {
        var text = message.toLowerCase();
        if (field === 'name') {
            return message.trim();
        }
        if (field === 'phone') {
            var phoneMatch = message.match(/\+?\d[\d\s().-]{7,}/);
            return phoneMatch ? phoneMatch[0] : message.trim();
        }
        if (field === 'email') {
            var emailMatch = message.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i);
            return emailMatch ? emailMatch[0] : message.trim();
        }
        if (field === 'location') {
            return message.trim();
        }
        if (field === 'budget') {
            var budgetMatch = message.match(/(\d+(?:\.\d+)?)\s*(m|million|naira|₦|k)/i);
            if (budgetMatch) {
                var val = parseFloat(budgetMatch[1]);
                if (budgetMatch[2].toLowerCase() === 'm' || budgetMatch[2].toLowerCase() === 'million') {
                    return '₦' + val.toFixed(2) + 'M';
                }
                if (budgetMatch[2].toLowerCase() === 'k') {
                    return '₦' + val + 'K';
                }
                return '₦' + val;
            }
            return message.trim();
        }
        if (field === 'purpose') {
            if (text.indexOf('residential') >= 0) return 'Residential';
            if (text.indexOf('investment') >= 0) return 'Investment';
            if (text.indexOf('commercial') >= 0) return 'Commercial';
            return message.trim();
        }
        if (field === 'timeline') {
            if (text.indexOf('immediately') >= 0 || text.indexOf('soon') >= 0) return 'Immediately';
            if (text.indexOf('1 month') >= 0 || text.indexOf('one month') >= 0) return '1 month';
            if (text.indexOf('3 months') >= 0 || text.indexOf('three months') >= 0) return '3 months';
            if (text.indexOf('6 months') >= 0 || text.indexOf('six months') >= 0) return '6 months';
            return message.trim();
        }
        return message.trim();
    }

    function computeLeadScore(lead) {
        var score = 0;
        if (lead.budget && parseFloat(lead.budget.replace(/[^0-9.]/g, '')) >= 5) {
            score += 30;
        }
        if (lead.timeline && lead.timeline.toLowerCase().indexOf('immediately') >= 0 || lead.timeline === '1 month') {
            score += 30;
        }
        if (lead.phone) {
            score += 20;
        }
        if (lead.email) {
            score += 10;
        }
        if (lead.inspectionRequested) {
            score += 20;
        }
        return Math.min(score, 100);
    }

    function completeLeadCapture() {
        chatState.lead.leadScore = computeLeadScore(chatState.lead);
        addMessage('Perfect! I have your details ready. Here is the CRM-ready JSON:', 'bot', { meta: getTimestamp() });
        addMessage(JSON.stringify(chatState.lead, null, 2), 'bot', { meta: getTimestamp() });
        chatState.collectingLead = null;
        addMessage('A property consultant can also assist you on WhatsApp: ' + whatsappLink, 'bot', { meta: getTimestamp() });
    }

    function startLeadCapture() {
        chatState.collectingLead = 'name';
        addMessage('Great! I can help you with that. I will collect a few details so our team can follow up properly.', 'bot', { meta: getTimestamp() });
        askLeadQuestion('name');
    }

    function startInspectionFlow() {
        chatState.collectingInspection = { step: 'date' };
        addMessage('Perfect! I can arrange an inspection for you. What date works best?', 'bot', { meta: getTimestamp() });
    }

    function handleLeadCapture(message) {
        var field = chatState.collectingLead;
        if (!field) {
            return false;
        }
        chatState.lead[field] = parseLeadField(field, message);
        var order = ['name', 'phone', 'email', 'location', 'budget', 'purpose', 'timeline'];
        var index = order.indexOf(field);
        if (index >= 0 && index < order.length - 1) {
            var nextField = order[index + 1];
            chatState.collectingLead = nextField;
            askLeadQuestion(nextField);
        } else {
            completeLeadCapture();
        }
        return true;
    }

    function handleInspectionCapture(message) {
        if (!chatState.collectingInspection) {
            return false;
        }
        if (!chatState.lead.inspection) {
            chatState.lead.inspection = {};
        }
        if (chatState.collectingInspection.step === 'date') {
            chatState.lead.inspection.date = message;
            chatState.collectingInspection.step = 'time';
            addMessage('Thank you. What time would you like to visit?', 'bot', { meta: getTimestamp() });
            return true;
        }
        if (chatState.collectingInspection.step === 'time') {
            chatState.lead.inspection.time = message;
            chatState.collectingInspection.step = 'estate';
            addMessage('Which estate would you like to inspect?', 'bot', { meta: getTimestamp() });
            return true;
        }
        if (chatState.collectingInspection.step === 'estate') {
            chatState.lead.inspection.estate = message;
            chatState.collectingInspection.step = 'visitors';
            addMessage('How many visitors will be joining you?', 'bot', { meta: getTimestamp() });
            return true;
        }
        chatState.lead.inspection.visitors = message;
        chatState.lead.inspectionRequested = true;
        chatState.collectingInspection = null;
        addMessage('Your inspection request is ready. We will confirm it shortly.\n\n' + JSON.stringify(chatState.lead.inspection, null, 2), 'bot', { meta: getTimestamp() });
        return true;
    }

    function sendMessage(message) {
        if (!message) {
            return;
        }

        addMessage(message, 'user', { meta: getTimestamp() });
        chatPanel.addClass('open');

        if (chatState.collectingLead) {
            handleLeadCapture(message);
            return;
        }

        if (chatState.collectingInspection) {
            handleInspectionCapture(message);
            return;
        }

        var lower = message.toLowerCase();
        if (lower.indexOf('buy') >= 0 || lower.indexOf('talk to someone') >= 0 || lower.indexOf('speak with an agent') >= 0 || lower.indexOf('agent') >= 0 || lower.indexOf('human representative') >= 0) {
            addMessage('Great! I’ll connect you with one of our property consultants.', 'bot', { meta: getTimestamp() });
            var waButton = $('<a class="chatbot-action-btn" href="' + whatsappLink + '" target="_blank" rel="noopener noreferrer"><i class="bi bi-whatsapp"></i> Chat on WhatsApp</a>');
            chatMessages.append(waButton);
            chatMessages.scrollTop(chatMessages[0].scrollHeight);
            return;
        }

        if (lower.indexOf('inspection') >= 0 || lower.indexOf('book') >= 0) {
            startInspectionFlow();
            return;
        }

        if (lower.indexOf('download brochure') >= 0 || lower.indexOf('brochure') >= 0 || lower.indexOf('download') >= 0) {
            addMessage('You can download the land brochure here: /img/Landform.pdf', 'bot', { meta: getTimestamp() });
            return;
        }

        var estateSummary = getEstateSummary(lower);
        if (estateSummary) {
            addMessage(estateSummary, 'bot', { meta: getTimestamp() });
            return;
        }

        if (lower.indexOf('lead') >= 0 || lower.indexOf('buy') >= 0 || lower.indexOf('interested') >= 0) {
            startLeadCapture();
            return;
        }

        var typingBubble = showTyping();
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                pageTitle: pageTitle,
                pageText: pageText,
                history: chatState.history.slice(-8)
            })
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            typingBubble.remove();
            addMessage(data.reply || 'I can help with available estates, prices, locations, inspections, and WhatsApp handoff. Ask me anything.', 'bot', { meta: getTimestamp() });
        })
        .catch(function () {
            typingBubble.remove();
            addMessage('I am having trouble reaching the assistant right now. Please contact a sales representative directly on WhatsApp: ' + whatsappLink, 'bot', { meta: getTimestamp() });
        });
    }

    $('#chatbotToggle').on('click', function () {
        chatPanel.toggleClass('open');
    });

    $('#chatbotClose').on('click', function () {
        chatPanel.removeClass('open');
    });

    $('#chatbotForm').on('submit', function (e) {
        e.preventDefault();
        var input = $('#chatbotInput');
        var message = input.val().trim();
        input.val('');
        sendMessage(message);
    });

    $('#chatbotInput').on('focus', function () {
        hideSuggestions();
    });

    $('#chatbotInput').on('blur', function () {
        setTimeout(showSuggestions, 120);
    });

    $(document).on('click', '.chatbot-chip', function () {
        sendMessage($(this).data('reply'));
    });

    renderSuggestions();
    loadEstateData();
    loadHistory();
    if (chatState.history.length === 0) {
        setTimeout(function () {
            addMessage('👋 Welcome to Verdant World.\nI\'m your AI Property Consultant.', 'bot', { meta: getTimestamp() });
            addMessage('I can help you with:\n🏡 Available estates\n💰 Prices\n📍 Recommended locations\n📅 Inspections\n📞 Connect you with an agent\n\nWhat would you like to know?', 'bot', { meta: getTimestamp() });
        }, 2000);
    }
    
})(jQuery);
