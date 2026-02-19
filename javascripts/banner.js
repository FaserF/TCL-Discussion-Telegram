document.addEventListener("DOMContentLoaded", function () {
    const dismissedNews = localStorage.getItem('dismissed_news_date');
    const logo = document.querySelector('.md-header__button.md-logo');
    const root = logo ? logo.href : '.';
    const newsUrl = new URL("assets/news.json", root).href;

    fetch(newsUrl)
        .then(response => response.json())
        .then(data => {
            if (data.active && dismissedNews !== data.date) {
                injectBanner(data);
            }
        })
        .catch(err => console.warn("News check failed:", err));
});

function injectBanner(data) {
    if (document.querySelector('.custom-banner')) return;

    const banner = document.createElement('div');
    banner.className = 'custom-banner';
    banner.innerHTML = `
        <span>🚀 <strong>${data.date}:</strong> ${data.text}</span>
        ${data.link ? `<a href="${data.link}" target="_blank">View details</a>` : ''}
        <button class="close-btn" aria-label="Close">&times;</button>
    `;

    // Inject before the header to avoid layout jumps
    const header = document.querySelector('.md-header');
    if (header) {
        header.insertAdjacentElement('beforebegin', banner);
    }

    banner.querySelector('.close-btn').addEventListener('click', () => {
        banner.remove();
        localStorage.setItem('dismissed_news_date', data.date);
    });
}
