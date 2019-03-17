from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

print("test")

@app.route('/')
def my_form():
    return render_template('modal.html')


@app.route('/', methods=['my_form_tech_skills'])
def my_form_tech_skills():
    tech_skills = request.form['text']
    print("testetset")
    f= open("./guru99.txt","w+")
    f.write("works")
    return tech_skills


@app.route('/', )
def my_form_soft_skills():
    soft_skills = request.form['text']

    return soft_skills


@app.route('/', )
def my_form_gpa():
    gpa = request.form['text']
    return gpa


@app.route('/', )
def my_form_majors():
    majors = request.form['text']
    return majors


@app.route('/', )
def my_form_expected_graduation():
    expected_graduation = request.form['text']
    return expected_graduation

@app.route('/action/')
def action():
    f= open("./mine.txt","w+")
    f.write("works")
    print("test_action")
    actions = request.form['take_input'] = 'input'
    if actions:
        majors = my_form_majors()
        gpa = my_form_gpa()
        expected_grad = my_form_expected_graduation()
        soft_skills = my_form_soft_skills()
        tech_skills = my_form_tech_skills()
    return render_template('modal.html')
if __name__ == '__main__':
    app.debug = True
    app.run()
