# Bring in Flask and a way to show HTML files
from flask import Flask, render_template

# Start the app
app = Flask(__name__)

# When someone goes to the homepage ("/"), run this
@app.route("/")
def home():
    # Show index.html
    return render_template("index.html")

# Run the app if this file is opened directly
if __name__ == "__main__":
    # Start the server, debug mode helps us see errors
    app.run(debug=True)
