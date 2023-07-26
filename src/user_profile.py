```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/ai_shopper'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    preferences = db.Column(db.String(200))
    style = db.Column(db.String(200))
    size = db.Column(db.String(50))
    product_preferences = db.Column(db.String(200))

    def __init__(self, name, preferences, style, size, product_preferences):
        self.name = name
        self.preferences = preferences
        self.style = style
        self.size = size
        self.product_preferences = product_preferences

class UserProfileSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'preferences', 'style', 'size', 'product_preferences')

user_profile_schema = UserProfileSchema()
user_profiles_schema = UserProfileSchema(many=True)

@app.route('/user_profile', methods=['POST'])
def add_user_profile():
    name = request.json['name']
    preferences = request.json['preferences']
    style = request.json['style']
    size = request.json['size']
    product_preferences = request.json['product_preferences']

    new_user_profile = UserProfile(name, preferences, style, size, product_preferences)

    db.session.add(new_user_profile)
    db.session.commit()

    return user_profile_schema.jsonify(new_user_profile)

@app.route('/user_profile', methods=['GET'])
def get_user_profiles():
    all_user_profiles = UserProfile.query.all()
    result = user_profiles_schema.dump(all_user_profiles)
    return jsonify(result)

@app.route('/user_profile/<id>', methods=['GET'])
def get_user_profile(id):
    user_profile = UserProfile.query.get(id)
    return user_profile_schema.jsonify(user_profile)

@app.route('/user_profile/<id>', methods=['PUT'])
def update_user_profile(id):
    user_profile = UserProfile.query.get(id)

    name = request.json['name']
    preferences = request.json['preferences']
    style = request.json['style']
    size = request.json['size']
    product_preferences = request.json['product_preferences']

    user_profile.name = name
    user_profile.preferences = preferences
    user_profile.style = style
    user_profile.size = size
    user_profile.product_preferences = product_preferences

    db.session.commit()

    return user_profile_schema.jsonify(user_profile)

@app.route('/user_profile/<id>', methods=['DELETE'])
def delete_user_profile(id):
    user_profile = UserProfile.query.get(id)
    db.session.delete(user_profile)
    db.session.commit()

    return user_profile_schema.jsonify(user_profile)

if __name__ == '__main__':
    app.run(debug=True)
```