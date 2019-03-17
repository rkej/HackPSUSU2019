from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('modal.html')
@app.route('/', methods=['tech_skills'])
def my_form_tech_skills():
    tech_skills = request.form['text']
    return tech_skills
@app.route('/', methods=['soft_skills'])

def my_form_soft_skills():
    tech_skills = request.form['text']

    return soft_skills
@app.route('/', methods=['gpa'])

def my_form_gpa():
    gpa = request.form['text']
    return gpa
@app.route('/', methods=['majors'])

def my_form_majors():
    majors = request.form['text']
    return tech_skills
@app.route('/', methods=['expected_graduation'])

def my_form_expected_graduation():
    expected_graduation = request.form['text']
    return expected_graduation
