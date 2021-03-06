from app import app
from flask import abort
from flask_json import as_json, request, jsonify
from app.models.user import User
from datetime import datetime


@app.route("/users", methods=["GET"])
def get_users():
    users = []
    query = User.select()
    for i in query:
        users.append(i.to_hash())
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
@as_json
def create_user():
    ''' Creating new user'''
    data = request.form
    email_check = User.select().where(User.email == data['email'])
    if email_check:
        return {'code': 10000, 'msg': 'Email already exists'}, 409

    user = User(
        email = data['email'],
        first_name = data['first_name'],
        last_name = data['last_name']
    )
    user.set_password(data['password'])
    user.save()

    return {'code': 201,'msg': 'User was created successfully'}, 201

@app.route('/users/<int:id>', methods=['GET'])
@as_json
def get_user(id):
    ''' Get a user'''
    try:
        user = User.get(User.id == id)
    except Exception as e:
        return {'code': 404, 'msg': "User not found"}, 404

    return user.to_hash(), 200

@app.route('/users/<int:id>', methods=['PUT'])
@as_json
def update_user(id):
    data = request.form
    user = User.get(User.id == id)
    for item in data:
        if item == 'email':
            raise Exception("Email can't be changed")
        if item == 'password':
            user.set_password(data['password'])
        if item == 'first_name':
            user.first_name = data['first_name']
        if item == 'last_name':
            user.last_name = data['last_name']
        if item == 'is_admin':
            user.is_admin = data['is_admin']
            print data['is_admin']

    user.save()
    return {'code': 200, 'msg': 'Updated successfully'}, 200

@app.route('/users/<int:id>', methods=['DELETE'])
@as_json
def del_user(id):
    id_check = User.select().where(User.id == id)
    if not id_check:
        return {'code': 404, 'msg': 'User not found'}, 404

    item = User.delete().where(User.id == id)
    item.execute()
    return {'code': 200, 'msg': 'Deleted successfully'}, 200
