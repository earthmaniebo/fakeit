# -*- coding: utf-8 -*-

from flask import Flask
from app.src.users.controllers import UserBP
from app.src.categories.controllers import CategoryBP

app = Flask(__name__)
app.register_blueprint(UserBP)
app.register_blueprint(CategoryBP)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5005, threaded=True)
