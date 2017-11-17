from flask import *

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
	return render_template("index.html")

if __name__ == "__main__":
	app.run()