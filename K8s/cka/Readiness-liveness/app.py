from flask import Flask, render_template, send_from_directory
import os 
import socket
app = Flask(__name__)

color = os.environ.get('APP_COLOR')
@app.route('/')
def index():
    print(color)
    hostname = socket.gethostname()
    return f'A7la Mesa on U From Abu Mayada and his device name is {hostname.upper()}'

@app.route('/khaled')
def healthz():
    name = "Khaled"
    return   f"My name is {name} , i'm working as a DevOps Engineer"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)