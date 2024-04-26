from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/person/<name>')
def hello_person(name):
    timezone = pytz.timezone('Australia/Brisbane')
    now = datetime.now(timezone)
    date_string = now.strftime('%Y-%m-%d')
    return render_template('5.html', name=name, date=date_string)

if __name__ == '__main__':
    app.run(debug=True)
