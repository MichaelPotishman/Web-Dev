from app import app, db, models
from .forms import NewPropertyForm, AssessmentForm
from flask import render_template, flash, redirect
from datetime import datetime


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html', assessments = models.Assessments.query.all())

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AssessmentForm()
    today = datetime.today().date()
    if form.validate_on_submit():
        flash("Successfully recieved data. %s" %(form.assessmenttitle.data))
        data = models.Assessments(assessmenttitle = form.assessmenttitle.data, modulecode = form.modulecode.data, deadline = form.deadline.data, description = form.description.data, status = form.status.data)
        db.session.add(data)
        db.session.commit()
        # return redirect('/details')
    return render_template('add.html', form=form, today=today)

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    assessment = models.Assessments.query.get(item_id)
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

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = models.Assessments.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
    return redirect('/')

@app.route('/complete_item/<int:item_id>', methods=['POST'])
def complete_item(item_id):
    item = models.Assessments.query.get(item_id)
    if item:
        item.status = 1 
        db.session.commit()
    return redirect('/')  

@app.route('/uncomplete_item/<int:item_id>', methods=['POST'])
def uncomplete_item(item_id):
    item = models.Assessments.query.get(item_id)
    if item:
        item.status = 0 
        db.session.commit()
    return redirect('/')  





