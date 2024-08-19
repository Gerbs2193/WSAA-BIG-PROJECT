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
    date_added = db.Column(db,Date, nullable)=False, default=date.today
    notes = db.Column(db.Column(db.Text, nullable=True)

with app.app_context():
    db.create_all()


