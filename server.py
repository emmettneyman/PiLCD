from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
	if 'program' in request.form:
		text = request.form['program']
        	os.system("python write_to_screen.py \"" + text + "\"")
	if 'color' in request.form:
		color = request.form['color']
		os.system("python set_color.py \"" + color + "\"")
	return render_template("index.html")

if __name__ == '__main__':
	app.run(host="0.0.0.0")
