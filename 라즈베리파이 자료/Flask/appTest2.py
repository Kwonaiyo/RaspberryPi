from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
	return "Hello Flask"

@app.route("/name")
def name():
	return "<h1>my name is Kwon</h1>"

@app.route("/age")
def age():
	return "<h3>I'm 28</h3>"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8000")
