# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("nama")
        return f"<h1>Halo, {nama}!</h1>"
    return render_template("index.html")

# Template HTML (index.html)
index_html = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Nama</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <div class="container">
        <h1>Silahkan Masukkan Nama</h1>
        <form method="POST" action="/">
            <label for="nama">Nama:</label>
            <input type="text" id="nama" name="nama" required>
            <button type="submit">Kirim</button>
        </form>
    </div>
</body>
</html>'''

# Styles CSS (styles.css)
styles_css = '''body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    text-align: center;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #007BFF;
    color: blue;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}'''

# Simpan file ke sistem (opsional, untuk penggunaan aktual)
import os

templates_path = "templates"
static_path = "static"
os.makedirs(templates_path, exist_ok=True)
os.makedirs(static_path, exist_ok=True)

with open(os.path.join(templates_path, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

with open(os.path.join(static_path, "styles.css"), "w", encoding="utf-8") as f:
    f.write(styles_css)

if __name__ == "__main__":
    app.run(debug=True)
