from flask import Flask, render_template, request, redirect, url_for, jsonify
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


with app.app_context():
    db.create_all()

# Routing section

@app.route('/')
def index():
    fish_list = Fish.query.all()
    return render_template('index.html', fish_list=fish_list)

@app.route('/add', methods=['POST'])
def add_fish():
    species_name = request.form['species_name']
    tank_name = request.form['tank_name']
    date_added = request.form.get('date_added', date.today())
    notes = request.form.get('notes', '')

    new_fish = Fish(
        species_name=species_name,
        tank_name=tank_name,
        date_added=date_added,
        notes=notes
    )
    db.session.add(new_fish)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_fish(id):
    fish = Fish.query.get_or_404(id)

    if request.method == 'POST':
        fish.species_name = request.form['species_name']
        fish.tank_name = request.form['tank_name']
        fish.date_added = request.form.get('date_added', fish.date_added)
        fish.notes = request.form.get('notes', '')

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('update.html', fish=fish)


@app.route('/delete/<int:id>')
def delete_fish(id):
    fish = Fish.query.get_or_404(id)
    db.session.delete(fish)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_fish(id):
    fish = Fish.query.get_or_404(id)
    if request.method == 'POST':
        fish.species_name = request.form['species_name']
        fish.tank_name = request.form['tank_name']
        fish.date_added = request.form.get('date_added', fish.date_added)
        fish.notes = request.form.get('notes', fish.notes)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', fish=fish)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_fish(id):
    fish = Fish.query.get_or_404(id)
    db.session.delete(fish)
    db.session.commit()
    return redirect(url_for('index'))

