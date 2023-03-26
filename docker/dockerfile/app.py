from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/abu')
def test():
    return 'a7la mesa on U from AbouShymaaa ;)'


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)