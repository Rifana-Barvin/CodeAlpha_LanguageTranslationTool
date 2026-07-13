function copyText(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert("Copied to clipboard!");
    });
}

function speakText(text, langCode = "en") {
    if (!("speechSynthesis" in window)) {
        alert("Sorry, your browser does not support speech synthesis.");
        return;
    }

    const synth = window.speechSynthesis;
    let voices = synth.getVoices();

    if (voices.length === 0) {
        synth.onvoiceschanged = () => {
            voices = synth.getVoices();
            speak(text, langCode, voices);
        };
    } else {
        speak(text, langCode, voices);
    }
}

function speak(text, langCode, voices) {
    const utterance = new SpeechSynthesisUtterance(text);

    let selectedVoice = voices.find(v => v.lang.toLowerCase().startsWith(langCode.toLowerCase()));
    if (!selectedVoice) {
        selectedVoice = voices.find(v => v.lang.startsWith("en")) || voices[0];
    }

    utterance.voice = selectedVoice;
    utterance.rate = 1;
    utterance.pitch = 1;
    window.speechSynthesis.speak(utterance);
}
