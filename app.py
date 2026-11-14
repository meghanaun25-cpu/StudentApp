from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to StudentApp!"

@app.route("/about")
def about():
    return "This is a Student Management Application."

if __name__ == "__main__":
    app.run(debug=False)