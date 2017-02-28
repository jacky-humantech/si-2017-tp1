from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! I'm from the planet Earth! o/"

if __name__ == '__main__':
    app.run(debug=True)