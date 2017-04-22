# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from app.src.utils.fakeit import fake
from app.src.utils.constants import FAKER_SEEDER

CategoryBP = Blueprint('CategoryBP', __name__)


@CategoryBP.route('/categories', methods=['GET'])
def get_all_categories():
    if request.method == 'GET':
        count = request.args.get('count') or 10
        try:
            count = int(count)
        except ValueError:
            count = 10
        categories = []
        fake.seed(FAKER_SEEDER)
        for _ in range(0, count):
            subcategories = []
            for _ in range(0, 3):
                subcategory = {
                    'id': fake.random_int(min=1, max=999),
                    'name': fake.word(),
                    'description': fake.text(max_nb_chars=70)
                }
                subcategories.append(subcategory)
            category = {
                'id': fake.random_int(min=1, max=999),
                'name': fake.word(),
                'description': fake.text(max_nb_chars=70),
                'subcategories': subcategories
            }
            categories.append(category)
        return jsonify(categories)


@CategoryBP.route('/categories/one', methods=['GET'])
def get_one_category():
    if request.method == 'GET':
        fake.seed(FAKER_SEEDER)
        subcategories = []
        for _ in range(0, 3):
            subcategory = {
                'id': fake.random_int(min=1, max=999),
                'name': fake.word(),
                'description': fake.text(max_nb_chars=70)
            }
            subcategories.append(subcategory)
        category = {
            'id': fake.random_int(min=1, max=999),
            'name': fake.word(),
            'description': fake.text(max_nb_chars=70),
            'subcategories': subcategories
        }
        return jsonify(category)
