// Telegram Widget Loader for MkDocs
function loadTelegramWidgets() {
    const containers = document.querySelectorAll('.telegram-widget');
    if (containers.length === 0) return;

    const currentTheme = document.body.getAttribute('data-md-color-scheme') || 'default';

    containers.forEach(container => {
        const post = container.dataset.post || "tclupdates/210";
        // Check if already loaded with the correct theme
        if (container.dataset.loaded === "true" && container.dataset.theme === currentTheme) {
            return;
        }

        const script = document.createElement('script');
        script.src = "https://telegram.org/js/telegram-widget.js?22";

        script.setAttribute('data-telegram-post', post);
        script.setAttribute('data-width', "100%");

        if (currentTheme === 'slate') {
            script.setAttribute('data-dark', "1");
        }

        if (container.dataset.discussion) {
            script.setAttribute('data-discussion', "true");
        }

        // Clear and append
        container.innerHTML = '';
        container.appendChild(script);

        // Mark as loaded with specific theme
        container.dataset.loaded = "true";
        container.dataset.theme = currentTheme;
        container.style.minHeight = '400px';
    });
}

// Initial load
document.addEventListener('DOMContentLoaded', loadTelegramWidgets);

// MkDocs Material Instant Loading Support
if (typeof location$ !== 'undefined') {
    location$.subscribe(function () {
        // Run immediately and then again slightly later to handle DOM transitions
        loadTelegramWidgets();
        setTimeout(loadTelegramWidgets, 400);
        setTimeout(loadTelegramWidgets, 1000); // Fail-safe
    });
}

// Watch for theme changes (Light/Dark mode toggle)
const themeObserver = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.type === 'attributes' && mutation.attributeName === 'data-md-color-scheme') {
            loadTelegramWidgets();
        }
    });
});

themeObserver.observe(document.body, {
    attributes: true,
    attributeFilter: ['data-md-color-scheme']
});
