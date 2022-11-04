from app import app
from flask import render_template, request, redirect
from models import Employees
from app import db


@app.route('/')
def index():
    employees = db.session.query(Employees).all()
    return render_template('index.html', employees=employees)


@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == "POST":
        data = request.form.to_dict()
        employee = Employees(name=data['name'], email=data['email'], phone=data['phone'])
        db.session.add(employee)
        db.session.commit()
        return redirect('/')


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        data = request.form.to_dict()
        row = db.session.query(Employees).get(data['id'])
        row.name = data['name']
        row.email = data['email']
        row.phone = data['phone']
        db.session.add(row)
        db.session.commit()
        return redirect('/')


@app.route('/delete/<int:id>')
def delete(id: int):
    data = db.session.query(Employees).get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')



