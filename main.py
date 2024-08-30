from morse_dict import morse
import re
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("main.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_value = request.form["get-string"]
    result = morse_translator(input_value)
    return f"{result}"

def morse_translator(value: str):
    if len(value) == 0:
        return f"No input, Try again"
    
    uvalue = value.upper()
    
    def translate(match):
        char = match.group(0)
        morse_code = morse.get(char, char)
        return f"{morse_code}|" if char != ' ' else morse_code

    try:
        # Translate characters to Morse code
        translated_chars = re.sub("|".join(re.escape(key) for key in morse.keys()), translate, uvalue)
        
        # Add brackets around words
        words = translated_chars.split('  ')
        bracketed_words = [f"[{word.rstrip('|')}]" for word in words]
        translated_string = '  '.join(bracketed_words)
    except ValueError:
        print("@Invalid Value")
        return "@Invalid Value"

    return f"""
    <p>Original Value : {value} <br/>
    Translated : {translated_string}</p>
    """
if __name__ == "__main__":
    app.run(debug=True)