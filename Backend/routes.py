from app import app, db
from flask import request, jsonify
from models import User, Student, Subject, Result

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], roll_number=data['roll_number'], class_id=data['class_id'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully'})

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    return jsonify({
        'name': student.name,
        'roll_number': student.roll_number,
        'class_id': student.class_id
    })

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get(id)
    student.name = data['name']
    student.roll_number = data['roll_number']
    student.class_id = data['class_id']
    db.session.commit()
    return jsonify({'message': 'Student updated successfully'})

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'})
