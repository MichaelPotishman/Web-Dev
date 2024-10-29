from app import app, db, models
from .forms import NewPropertyForm, AssessmentForm
from flask import render_template, flash, redirect


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html', assessments = models.Assessments.query.all())

@app.route('/details', methods=['GET', 'POST'])
def showDetails():
    return render_template('details.html', objects = models.Assessments.query.all())

@app.route('/clear', methods=['POST'])
def clear():
    db.session.query(models.Property).delete()
    db.session.commit()
    return "all assessments cleared"

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AssessmentForm()
    if form.validate_on_submit():
        flash("Successfully recieved data. %s" %(form.assessmenttitle.data))
        data = models.Assessments(assessmenttitle = form.assessmenttitle.data, modulecode = form.modulecode.data, deadline = form.deadline.data, description = form.description.data, status = form.status.data)
        db.session.add(data)
        db.session.commit()
        # return redirect('/details')
    return render_template('add.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    assessment = models.Assessments.query.get(id)
    form = AssessmentForm(obj=assessment)
    if form.validate_on_submit():
        assessment.assessmenttitle = form.assessmenttitle.data
        assessment.modulecode = form.modulecode.data
        assessment.deadline = form.deadline.data
        assessment.description = form.description.data

        if form.status.data:
            assessment.status = 1
        else:
            assessment.status = 0
        
        db.session.commit()

    return render_template('edit.html', form=form, assessment=assessment)




