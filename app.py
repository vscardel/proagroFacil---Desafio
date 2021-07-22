from flask import Flask,render_template,request,redirect,flash,session
from flaskext.mysql import MySQL

@app.route('/')
def index():
	return "oi"

if __name__ == '__main__':
	app.run(debug=True)