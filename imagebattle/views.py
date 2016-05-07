from flask import render_template
from imagebattle import app


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/leading', methods=['GET'])
def leading():
    return render_template('leading.html')
	
@app.route('/team', methods=['GET'])
def team():
    return render_template('team.html')
