from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/person/<first_name>')
def hello_person(first_name):
    safe_first_name = escape(first_name)  # Escapes special characters
    return f'<h1>Hello {safe_first_name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
