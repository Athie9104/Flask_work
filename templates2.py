from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


@app.route('/Index/<user>')
def index(user):
    return render_template('greet.html', name=user)


@app.route('/grading/<int:score>')
def grades(score):
    return render_template('grades.html', mark=score)




if __name__=='__main__':
    app.run(debug=True)
