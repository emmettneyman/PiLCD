from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)
color = "white"
text = "Default Text"
@app.route('/')
def my_form():
	return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
	if 'color' in request.form:
		global color
		color = request.form['color']
		os.system("sudo pkill -f write_to_screen.py")
		os.system("python write_to_screen.py \"" + text + "\" " + color + " &")
		return render_template("index.html")
	if 'program' in request.form:
		global text
		text = request.form['program']
		os.system("sudo pkill -f write_to_screen.py")
		os.system("python write_to_screen.py \"" + text + "\" " + color + " &")
		return render_template("index.html")

if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0")
