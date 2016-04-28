from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def my_form():
	#return "hello, world"
	return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
	text = request.form['program']
	processed_text = text.upper()
#	print('test')
	os.system("python write_to_screen.py " + text)
	return "ok"
	
if __name__ == '__main__':
	app.run(host="0.0.0.0")
