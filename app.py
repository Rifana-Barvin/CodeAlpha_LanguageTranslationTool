from flask import Flask, render_template, request
from translator import translate_text, get_supported_languages

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translation = None
    target_lang = None
    languages = get_supported_languages()
    if request.method == "POST":
        text = request.form["text"]
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]
        translation = translate_text(text, source_lang, target_lang)
    return render_template("index.html", translation=translation, languages=languages, target_lang=target_lang)

if __name__ == "__main__":
    app.run(debug=True)
