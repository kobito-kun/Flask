from flask import Flask, render_template, request

app = Flask(__name__) 
  
@app.route('/') 
def hello_world(): 
    return render_template('1.html')

@app.route('/test', methods=['POST', 'GET'])
def test():
	if request.method == 'POST':
		name = request.form['name']

		return f'Hello there {name}'

app.run(debug=True) 