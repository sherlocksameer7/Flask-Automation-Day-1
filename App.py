from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hi, This is my Website"

@app.route('/')
def contact_page()

if __name__ == "__main__":
    app.run()