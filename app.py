from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# DATABASE YARATISH
def init_db():
    conn = sqlite3.connect("visitors.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY,
            visitors INTEGER DEFAULT 0
        )
    """)

    cursor.execute("SELECT * FROM stats WHERE id = 1")

    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO stats (id, visitors) VALUES (1, 0)"
        )

    conn.commit()
    conn.close()


# SAYTGA KIRGANDA VISITORNI SANASH
@app.route("/")
def home():

    conn = sqlite3.connect("visitors.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE stats SET visitors = visitors + 1 WHERE id = 1"
    )

    cursor.execute(
        "SELECT visitors FROM stats WHERE id = 1"
    )

    visitors = cursor.fetchone()[0]

    conn.commit()
    conn.close()

    return render_template(
        "index.html",
        visitors=visitors
    )


# CONTACT FORM
@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    with open("messages.txt", "a", encoding="utf-8") as file:

        file.write(
            f"\n\nIsm: {name}\n"
            f"Email: {email}\n"
            f"Xabar: {message}\n"
            f"{'-' * 40}\n"
        )

    return redirect("/#contact")


if __name__ == "__main__":

    init_db()

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
