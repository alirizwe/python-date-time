from flask import Flask
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_current_date():
    current_date = datetime.now(timezone.utc)
    return current_date.strftime('%Y-%m-%d')

@app.route('/time', methods=['GET'])
def get_current_time():
    current_time = datetime.now(timezone.utc)
    return current_time.strftime('%H:%M:%S')

@app.route('/', methods=['GET'])
def get_current_datetime():
    current_datetime = datetime.now(timezone.utc)
    return current_datetime.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
