from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/bye')
def bye():
    return "Good bye, cruel world !"

if __name__ == '__main__':
    app.run(debug=True)
