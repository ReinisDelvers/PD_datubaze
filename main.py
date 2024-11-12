from flask import Flask, render_template, request
from data import add_user, add_message, get_user, get_message
import sqlite3

conn = sqlite3.connect("data.db")

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def registraion():
    user_db = get_user()
    if request.method == "POST":
        name = request.form["name"].capitalize()
        lastname = request.form["lastname"].capitalize()
        username = request.form["username"].capitalize()
        for i in user_db:
            if i[3] == username:
                print("Error")
        if name and lastname and username:
          add_user(name, lastname, username)
        return render_template("registration.html")
    return render_template("registration.html")

@app.route("/message", methods=["POST", "GET"])
def message():
    user_db = get_user()
    message_db = get_message()
    if request.method == "POST":
        text = request.form["text"].capitalize()
        user_id = request.form["user_id"].capitalize()  
        if text and user_id:
          add_message(text, user_id)
        return render_template("message.html", user = user_db, message = message_db)
    return render_template("message.html", user = user_db, message = message_db)

@app.route("/statistics", methods=["POST", "GET"])
def statistics():
    user_db = get_user()
    message_db = get_message()
    return render_template("statistics.html")

if __name__ == '__main__':
    app.run(port = 5000)