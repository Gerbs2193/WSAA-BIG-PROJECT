from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fishkeeping.db'
db = SQLAlchemy(app)

class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species_name = db.Column(db.String(100), nullable=False)
    tank_name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.Date, nullable=False, default=date.today)
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'species_name': self.species_name,
            'tank_name': self.tank_name,
            'date_added': self.date_added.isoformat(),
            'notes': self.notes
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    fish_list = Fish.query.all()
    return render_template('index.html', fish_list=fish_list)

@app.route('/api/fish', methods=['GET'])
def get_fish_list():
    fish_list = Fish.query.all()
    return jsonify([fish.to_dict() for fish in fish_list])

@app.route('/api/fish/<int:id>', methods=['GET'])
def get_fish(id):
    fish = Fish.query.get_or_404(id)
    return jsonify(fish.to_dict())

@app.route('/api/add', methods=['POST'])
def add_fish_api():
    data = request.get_json()
    new_fish = Fish(
        species_name=data['species_name'],
        tank_name=data['tank_name'],
        date_added=date.fromisoformat(data['date_added']),
        notes=data['notes']
    )
    db.session.add(new_fish)
    db.session.commit()
    return jsonify(new_fish.to_dict()), 201

@app.route('/api/update/<int:id>', methods=['PUT'])
def update_fish_api(id):
    fish = Fish.query.get_or_404(id)
    data = request.get_json()
    fish.species_name = data['species_name']
    fish.tank_name = data['tank_name']
    fish.date_added = date.fromisoformat(data['date_added'])
    fish.notes = data['notes']
    db.session.commit()
    return jsonify(fish.to_dict())

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_fish_api(id):
    fish = Fish.query.get_or_404(id)
    db.session.delete(fish)
    db.session.commit()
    return jsonify({'message': 'Fish deleted'}), 204

if __name__ == "__main__":
    app.run(debug=True)