document.addEventListener('DOMContentLoaded', function() {
    const API_BASE_URL = 'http://localhost:5000';
    let currentTrack = null;
    let isPlaying = false;

    // DOM Elements
    const playPauseBtn = document.getElementById('play-pause');
    const nextBtn = document.getElementById('next');
    const volumeSlider = document.getElementById('volume');
    const themeElement = document.getElementById('theme');
    const moodElement = document.getElementById('mood');
    const audioTypeElement = document.getElementById('audio-type');
    const trackNameElement = document.getElementById('track-name');
    const artistNameElement = document.getElementById('artist-name');
    const recommendationsList = document.getElementById('recommendations-list');

    // Initialize
    initializePlayer();

    // Event Listeners
    playPauseBtn.addEventListener('click', togglePlayPause);
    nextBtn.addEventListener('click', playNextTrack);
    volumeSlider.addEventListener('input', updateVolume);

    async function initializePlayer() {
        try {
            // Get current tab content
            const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
            const content = await getPageContent(tab.id);

            // Analyze content
            const analysis = await analyzeContent(content);
            updateThemeInfo(analysis);

            // Get recommendations
            const recommendations = await getRecommendations(analysis.theme, analysis.audio_type);
            displayRecommendations(recommendations);

            // Play first recommendation
            if (recommendations.length > 0) {
                playTrack(recommendations[0]);
            }
        } catch (error) {
            console.error('Initialization error:', error);
        }
    }

    async function getPageContent(tabId) {
        return new Promise((resolve, reject) => {
            chrome.tabs.sendMessage(tabId, { action: 'getContent' }, response => {
                if (chrome.runtime.lastError) {
                    reject(chrome.runtime.lastError);
                } else {
                    resolve(response.content);
                }
            });
        });
    }

    async function analyzeContent(content) {
        const response = await fetch(`${API_BASE_URL}/analyze`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content })
        });
        return await response.json();
    }

    async function getRecommendations(theme, audioType) {
        const response = await fetch(`${API_BASE_URL}/search_audio`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ theme, audio_type: audioType })
        });
        const data = await response.json();
        return data.results;
    }

    function updateThemeInfo(analysis) {
        themeElement.textContent = analysis.theme;
        moodElement.textContent = analysis.mood;
        audioTypeElement.textContent = analysis.audio_type;
    }

    function displayRecommendations(recommendations) {
        recommendationsList.innerHTML = '';
        recommendations.forEach(track => {
            const item = document.createElement('div');
            item.className = 'recommendation-item';
            item.textContent = `${track.name} - ${track.artists[0].name}`;
            item.addEventListener('click', () => playTrack(track));
            recommendationsList.appendChild(item);
        });
    }

    async function playTrack(track) {
        currentTrack = track;
        trackNameElement.textContent = track.name;
        artistNameElement.textContent = track.artists[0].name;

        const response = await fetch(`${API_BASE_URL}/play`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ uri: track.uri })
        });

        if (response.ok) {
            isPlaying = true;
            updatePlayPauseButton();
        }
    }

    async function togglePlayPause() {
        if (!currentTrack) return;

        const endpoint = isPlaying ? '/pause' : '/resume';
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: 'POST'
        });

        if (response.ok) {
            isPlaying = !isPlaying;
            updatePlayPauseButton();
        }
    }

    async function playNextTrack() {
        const recommendations = Array.from(recommendationsList.children);
        const currentIndex = recommendations.findIndex(item => 
            item.textContent === `${currentTrack.name} - ${currentTrack.artists[0].name}`
        );
        
        if (currentIndex < recommendations.length - 1) {
            const nextTrack = recommendations[currentIndex + 1];
            nextTrack.click();
        }
    }

    async function updateVolume() {
        const volume = volumeSlider.value;
        await fetch(`${API_BASE_URL}/volume`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ volume: parseInt(volume) })
        });
    }

    function updatePlayPauseButton() {
        playPauseBtn.textContent = isPlaying ? 'Pause' : 'Play';
    }
}); 