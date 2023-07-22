from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route("/", methods=['GET', 'POST'])
def main():
    global messages
    message = ""
    nick = ""
    if request.method == 'POST':
        time = datetime.now()
        date_stamp = f"{time.hour}:{time.minute}:{time.second}"
        message = request.form.get('text')
        nick = request.form.get('nickname')
        if nick == "":
                nick = "User"
        if len(message) >= 1 and message[0] != "/":
            full_message = [message, date_stamp, nick]
            messages.append(full_message)
            print(messages)
        if message == "/clear" and nick == "secret!":
            messages = []
        return render_template("index.html", messages = messages)
    return render_template("index.html", messages = messages)

app.run()