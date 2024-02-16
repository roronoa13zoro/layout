from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index1.html')

@app.route("/index1")
def index1():
	return render_template('index1.html')

@app.route("/index2")
def index2():
	return render_template('index2.html')

if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0")
