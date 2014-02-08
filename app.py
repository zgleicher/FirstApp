from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
def hello():
	return render_template("hello.html")

@app.route("/name")
def name():
	return "Zachary Gleicher"

@app.route("/search", methods = ["GET", "POST"])
def search():
	if request.method == "POST":
		url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
		response_dict = requests.get(url).json()
		return render_template("results.html", api_data=response_dict)
	else:
		return render_template("search.html")

@app.route("/add/<x>/<y>")
def add(x, y):
    return str(int(x) + int(y))

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, page is not found", 404

if __name__ == "__main__":
	app.run(host="0.0.0.0")