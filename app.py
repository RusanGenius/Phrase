from flask import Flask, request, redirect, render_template

app = Flask(__name__)

TEXT_FILE = "text.txt"

def read_text():
    try:
        with open(TEXT_FILE, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Надпись пока не установлена!"

def write_text(new_text):
    with open(TEXT_FILE, "w", encoding="utf-8") as file:
        file.write(new_text)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_text = request.form.get("new_text")
        if new_text:
            write_text(new_text)
        return redirect("/")

    current_text = read_text()
    return render_template("index.html", current_text=current_text)

if __name__ == "__main__":
    app.run(debug=True)
