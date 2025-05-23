// Handle installation
chrome.runtime.onInstalled.addListener(() => {
    console.log('Theme-Based Audio Player extension installed');
});

// Handle messages from content script or popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'checkAuth') {
        // Check if user is authenticated with Spotify
        checkSpotifyAuth()
            .then(isAuthenticated => sendResponse({ isAuthenticated }))
            .catch(error => sendResponse({ error: error.message }));
        return true;
    }
}); 