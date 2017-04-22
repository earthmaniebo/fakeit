# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from app.src.utils.fakeit import fake
from app.src.utils.constants import FAKER_SEEDER

UserBP = Blueprint('UserBP', __name__)


@UserBP.route('/users', methods=['GET'])
def get_all_users():
    if request.method == 'GET':
        count = request.args.get('count') or 10
        try:
            count = int(count)
        except ValueError:
            count = 10
        users = []
        fake.seed(FAKER_SEEDER)
        for _ in range(0, count):
            user = {
                'id': fake.random_int(min=1, max=999),
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.email(),
                'contact_number': fake.phone_number()
            }
            users.append(user)
        return jsonify(users)


@UserBP.route('/users/one', methods=['GET'])
def get_one_user():
    if request.method == 'GET':
        fake.seed(FAKER_SEEDER)
        user = {
            'id': fake.random_int(min=1, max=999),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'contact_number': fake.phone_number()
        }
        return jsonify(user)
