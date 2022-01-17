from flask import Flask, render_template     # imports Flask

app = Flask(__name__)       # creates a Flask object

@app.route('/')             # creates a default route
def test():                 # default route function
    return render_template("index.html")

@app.route('/play')         # will display 3 boxes
def play():
    return render_template("play.html")

@app.route('/play/<int:x>')
def playx(x):
    return render_template("playx.html", x = x)

@app.route('/play/<int:x>/<color>')
def playxcolor(x, color):
    return render_template("playxcolor.html", x = x, color = color)

if __name__ == "__main__":  # will run the program
    app.run(debug=True) 