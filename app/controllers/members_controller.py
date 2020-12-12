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

