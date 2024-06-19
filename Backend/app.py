from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/srms'
db = SQLAlchemy(app)

import routes

if __name__ == '__main__':
    app.run(debug=True)
