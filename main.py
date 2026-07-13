from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk
import pyperclip
from gtts import gTTS
import os

# Common languages dictionary
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Bengali": "bn",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Urdu": "ur",
    "Turkish": "tr",
    "Persian (Farsi)": "fa",
    "Thai": "th",
    "Vietnamese": "vi",
    "Swahili": "sw"
}

def translate_text():
    input_text = entry.get()
    src = languages[src_lang.get()]
    dest = languages[dest_lang.get()]
    if input_text.strip():
        result = GoogleTranslator(source=src, target=dest).translate(input_text)
        output_label.config(text=result)

def copy_text():
    translated_text = output_label.cget("text")
    if translated_text:
        pyperclip.copy(translated_text)

def speak_text():
    translated_text = output_label.cget("text")
    if translated_text:
        tts = gTTS(text=translated_text, lang=languages[dest_lang.get()])
        tts.save("output.mp3")
        os.system("start output.mp3")  # Windows

# GUI setup
root = tk.Tk()
root.title("🌐 Language Translation Tool")
root.geometry("550x450")
root.configure(bg="#f0f8ff")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 11))

# Input field
ttk.Label(root, text="Enter Text:", background="#f0f8ff").pack(pady=5)
entry = ttk.Entry(root, width=50)
entry.pack(pady=10)

# Dropdowns for source and target languages
src_lang = tk.StringVar(value="English")
dest_lang = tk.StringVar(value="French")

ttk.Label(root, text="Source Language:", background="#f0f8ff").pack()
ttk.Combobox(root, textvariable=src_lang, values=list(languages.keys()), state="readonly").pack(pady=5)

ttk.Label(root, text="Target Language:", background="#f0f8ff").pack()
ttk.Combobox(root, textvariable=dest_lang, values=list(languages.keys()), state="readonly").pack(pady=5)

# Buttons
ttk.Button(root, text="Translate", command=translate_text).pack(pady=10)
ttk.Button(root, text="Copy", command=copy_text).pack(pady=5)
ttk.Button(root, text="Speak", command=speak_text).pack(pady=5)

# Output label
output_label = ttk.Label(root, text="", wraplength=500, background="#f0f8ff", font=("Arial", 12, "bold"))
output_label.pack(pady=20)

root.mainloop()
