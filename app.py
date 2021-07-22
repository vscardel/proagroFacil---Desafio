import config
from config import app

@app.route('/')
def index():
	return "oi"

if __name__ == '__main__':
	app.run(debug=True)