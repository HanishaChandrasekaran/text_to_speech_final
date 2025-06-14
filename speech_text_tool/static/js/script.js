function convertTextToSpeech() {
    const text = document.getElementById('text-input').value;
    fetch('/text-to-speech', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    });
    const utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
}

function uploadImage() {
    const fileInput = document.getElementById('image-input');
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    fetch('/image-to-speech', {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('image-text').innerText = data.text;
        const utterance = new SpeechSynthesisUtterance(data.text);
        speechSynthesis.speak(utterance);
    });
}

function startSpeechToText() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        document.getElementById('speech-result').innerText = "You said: " + text;
    };
}
