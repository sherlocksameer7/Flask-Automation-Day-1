from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hi, This is my Website"

@app.route('/contact')
def contact_page():
    return "Visiting Contact Page"

@app.route('/home')
def home_page():
    return "Visiting Home Page"

@app.route('/gallery')
def gallery_page():
    return "Visiting Gallery Page"

if __name__ == "__main__":
    app.run()