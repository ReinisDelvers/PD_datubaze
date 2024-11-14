from flask import Flask, render_template, request
from data import add_user, add_message, get_message_message, get_user_message, get_statistics
import sqlite3

conn = sqlite3.connect("data.db")

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def registraion():
    if request.method == "POST":
        name = request.form["name"].capitalize()
        lastname = request.form["lastname"].capitalize()
        username = request.form["username"].capitalize()
        if name and lastname and username:
            try:
                add_user(name, lastname, username)
                error =""
            except:
                error = "Username exists"
        else:
            error = "Fill all fields"
        return render_template("registration.html", error = error)
    return render_template("registration.html")

@app.route("/message", methods=["POST", "GET"])
def message():
    user_db = get_user_message()
    message_db = get_message_message()
    if request.method == "POST":
        text = request.form["text"].capitalize()
        user_id = request.form["user_id"].capitalize()  
        if text and user_id:
          add_message(text, user_id)
          error = ""
        else:
            error = "Fill all fields"
        return render_template("message.html", user = user_db, message = message_db, error = error)
    return render_template("message.html", user = user_db, message = message_db)

@app.route("/statistics", methods=["POST", "GET"])
def statistics():
    user_db = get_statistics()
    return render_template("statistics.html", user = user_db)

if __name__ == '__main__':
    app.run(port = 5000)