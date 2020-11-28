from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///walking.db')
app = Flask(__name__)
api = Api(app)

class Walk(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from users_walk")
        return {'caminatas' : [i[0] for i in query.cursor.fetchall()]}

    def post(self):
        conn = db_connect.connect()
        name =  request.json['name']
        email = request.json['email']
        walk = request.json['walk']
        if walk >= 4:
            query = conn.execute("insert into users_walk values('{0}','{1}','{2}')".format(name,email,walk,))
            return {'status' : 'Caminata Guardada'}
        else:
            return {'status' : 'Debes de camin    ar más'}

api.add_resource(Walk, '/walk')

if __name__ == '__main__':
    app.run(port='5000')































