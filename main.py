# it lets the program use Flask so it can show web pages
from flask import Flask, render_template

# Creates the app so it can run like a website
app = Flask(__name__)

# This makes the homepage show index.html when someone visits "/"
@app.route("/")
def home():
    return render_template("index.html")  # Displays the index.html page in the browser

# This part makes sure the server starts when you run the file
if __name__ == "__main__":
    app.run(debug=True)  # Opens the site and shows errors if something goes wrong
