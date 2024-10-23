from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

  
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(200), nullable=False, unique=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    favorite_character = db.relationship("Favorite_character")
    favorite_planet = db.relationship("Favorite_planet")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }

class Favorite_character(db.Model):
    __tablename__ = "favorite_character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "character_id": self.character_id,
        }


class Character(db.Model):
    __tablename__ = "character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200))
    gender = db.Column(db.String(200), nullable=False)
    hair_color = db.Column(db.String(200))
    eye_color = db.Column(db.String(200))
    favorite_character = db.relationship("Favorite_character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
        }


class Favorite_planet(db.Model):
    __tablename__ = "favorite_planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }


class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200))
    lenght = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.String(200))
    orbital_period = db.Column(db.String(200))
    gravity = db.Column(db.String(200)) 
    population = db.Column(db.Integer, nullable=False)
    climate  = db.Column(db.String(200))
    terrain = db.Column(db.String(200))
    surface_water = db.Column(db.String(200))
    favorite_planet = db.relationship("Favorite_planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "lenght": self.lenght,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }

