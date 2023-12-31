### Create a simple flask application

from flask import Flask,render_template,url_for,request,redirect

### Create flask app
app=Flask(__name__)

@app.route('/')  # / for home
def home():  # each time user hit / or search home home function gets activated
    return '<h1>Hello World</h1>'

@app.route('/welcome')  # means give a url
def welcome():  # when hit url give this function
    return 'Welcome to the Flask tutorial'

@app.route('/success/<int:score>')  #int: score is a parameter
def success(score):
    return "Passed. Avg score is" + str(score)

@app.route('/fail/<int:score>')  #int: score is a parameter
def fail(score):
    return "Failed. Avg score is" + str(score)

@app.route('/calculate', methods=['POST', 'GET'])  # we are getting input and give output
def calculate():  # when hit url give this function
    if request.method=='GET':   
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        avg_marks=(maths+science+history)/3
        '''
        result=''
        if avg_marks>=50:
            result='success'
        else:
            result='fail'
        return redirect(url_for(result, score=avg_marks))
        '''
        return render_template('results.html', results=avg_marks)

@app.route('/grades')  # means give a url
def grades():  # when hit url give this function
    return render_template('grades.html') 

@app.route('/index')  # means give a url
def index():  # when hit url give this function
    return render_template('index.html')  # redirect to index.html, it has to be present in 'templates' folder

if __name__=='__main__':  # it is the entry point
    app.run(debug=True)  # never do this debug in production only in development
    # If put debug is true don't have to again and again run 'python app.py'



# redirect with in route - redirect, url_for
# redirect with html - render_template