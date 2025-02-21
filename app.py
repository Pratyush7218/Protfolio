from flask import Flask, render_template, redirect, url_for, flash


app = Flask(__name__, template_folder='Resume/templates', static_folder='Resume/static')  # Initialize Flask app

@app.route('/')  # Define the route for the homepage
def hello():
    return render_template('index.html')  # Return response

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
