import io
import csv
import pymysql
from app import app
from db import mysql
from flask import Flask, Response, render_template

@app.route('/')
def index():
	return "oi"

if __name__ == '__main__':
	app.run(debug=True)