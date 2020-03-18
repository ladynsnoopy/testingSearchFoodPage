from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Workout(db.Model):#one workout of user
    __tablename__ = 'Workout'
    workout_id = db.Column(db.Integer, primary_key = True)
    workoutrecord_id = db.Column(db.Integer, db.ForeignKey('WorkoutRecord.workoutrecord_id', ondelete='CASCADE'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id', ondelete='CASCADE'), nullable = False)
    workout_name = db.Column(db.String(50), nullable = False)
    Exercise = db.relationship("Exercise", backref="Workout", cascade="all, delete, delete-orphan", passive_deletes=True)
    Set = db.relationship("Set", backref="Workout", cascade="all, delete, delete-orphan", passive_deletes=True)
    Rep = db.relationship("Rep", backref="Workout", cascade="all, delete, delete-orphan", passive_deletes=True)

class Exercise(db.Model):#one exercise in workout
    __tablename__ = 'Exercise'
    exercise_id = db.Column(db.Integer, db.ForeignKey('ExerciseDB.exercise_id', ondelete='CASCADE'), nullable = False, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('Workout.workout_id', ondelete='CASCADE'), nullable = False, primary_key=True)
    workoutrecord_id = db.Column(db.Integer, db.ForeignKey('WorkoutRecord.workoutrecord_id', ondelete='CASCADE'), nullable = False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id', ondelete='CASCADE'), nullable = False, primary_key=True)
    exercise_desc = db.Column(db.String(1000000), nullable = False)
    exercise_caloriesburnt = db.Column(db.Float, nullable = False)
    status = db.Column(db.Boolean, nullable = False, default = False)

class Set(db.Model):#one set in exercise
    __tablename__ = 'Set'
    set_id = db.Column(db.Integer, primary_key = True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('ExerciseDB.exercise_id', ondelete='CASCADE'), nullable = False)
    workout_id = db.Column(db.Integer, db.ForeignKey('Workout.workout_id', ondelete='CASCADE'), nullable = False)
    workoutrecord_id = db.Column(db.Integer, db.ForeignKey('WorkoutRecord.workoutrecord_id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id', ondelete='CASCADE'), nullable = False)
    set_count = db.Column(db.Integer, nullable = False)
    Rep = db.relationship("Rep", backref="Set", cascade="all, delete, delete-orphan", passive_deletes=True)


class Rep(db.Model):#one in set
    __tablename__ = 'Rep'
    rep_id = db.Column(db.Integer, primary_key = True)
    set_id = db.Column(db.Integer, db.ForeignKey('Set.set_id', ondelete='CASCADE'), nullable = False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('ExerciseDB.exercise_id', ondelete='CASCADE'), nullable = False)
    workout_id = db.Column(db.Integer, db.ForeignKey('Workout.workout_id', ondelete='CASCADE'), nullable = False)
    workoutrecord_id = db.Column(db.Integer, db.ForeignKey('WorkoutRecord.workoutrecord_id', ondelete='CASCADE'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id', ondelete='CASCADE'), nullable = False)
    rep_count = db.Column(db.Integer, nullable = False)
    rep_unit = db.Column(db.String(20), nullable = False)#e.g. 50 kg, kg is the desc
    rep_desc = db.Column(db.String(20), nullable = False) #e.g. 50kg, 50 is the desc



