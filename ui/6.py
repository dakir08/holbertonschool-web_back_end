from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    greetings = ["Hello", "Hi", "G’day", "Greetings"]
    name = ""
    greeting = ""
    if request.method == 'POST':
        name = request.form.get('name')
        if name:  # check if name is not empty
            greeting = f"{random.choice(greetings)} {name}"
    return render_template('6.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
