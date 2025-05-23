// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'getContent') {
        // Extract the main content from the page
        const content = extractPageContent();
        sendResponse({ content });
    }
    return true;
});

function extractPageContent() {
    // Get the main content of the page
    // This is a simple implementation that can be enhanced based on specific needs
    const article = document.querySelector('article') || document.body;
    
    // Remove unwanted elements
    const unwantedSelectors = [
        'script',
        'style',
        'nav',
        'header',
        'footer',
        'aside',
        'iframe',
        'noscript'
    ];
    
    const clone = article.cloneNode(true);
    unwantedSelectors.forEach(selector => {
        const elements = clone.querySelectorAll(selector);
        elements.forEach(el => el.remove());
    });

    // Get the text content
    let content = clone.textContent
        .replace(/\s+/g, ' ')
        .trim();

    // Limit content length to avoid API limits
    const maxLength = 5000;
    if (content.length > maxLength) {
        content = content.substring(0, maxLength) + '...';
    }

    return content;
} 