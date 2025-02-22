from flask import Flask, render_template
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Nishant Singh" 

    username = subprocess.run(['whoami'], capture_output=True, text=True).stdout.strip()

    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')

    top_output = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout

    return render_template('htop.html', full_name=full_name, username=username, ist_time=ist_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)