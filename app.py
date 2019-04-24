from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/automation')
def automation():
	print("hello worldy world")
	return render_template('automation.html')


def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Hello World':
            print("hello")
        elif request.form['submit_button'] == 'Do Something Else':
            print("hello")
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('automation.html', form=form)

if __name__ == '__main__':
    app.run(debug=True) #host='169.225.9.1',
