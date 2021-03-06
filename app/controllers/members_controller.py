from flask import Flask, Blueprint, render_template, request, redirect
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/<id>")
def show_member(id):
    member = member_repository.select(id)
    workouts = member_repository.workouts(member)
    return render_template("members/show.html", member=member, workouts=workouts)

# New
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")

@members_blueprint.route("/members", methods=['POST'])
def create_member():
    first_name  = request.form['first_name']
    last_name   = request.form['last_name']
    gender      = request.form['gender']
    age         = request.form['age']

    member = Member(first_name, last_name, gender, age)
    member_repository.save(member)
    return redirect('/members')

# Edit
@members_blueprint.route('/members/<id>/edit', methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)

@members_blueprint.route('/members/<id>', methods=['POST'])
def update_memebr(id):
    first_name  = request.form['first_name']
    last_name   = request.form['last_name']
    gender      = request.form['gender']
    age         = request.form['age']

    member = Member(first_name, last_name, gender, age, id)
    member_repository.update(member)
    return redirect('/members')
