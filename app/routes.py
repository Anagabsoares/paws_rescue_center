from app import db
from datetime import datetime
from flask import Blueprint, jsonify, make_response, request, abort, render_template
home_bp = Blueprint('goals', __name__, url_prefix='')

@home_bp.route('/')
def home():
    return "Paws Rescue Center 🐾"

@home_bp.route('/about')
def about():
    return render_template("about.html")

@home_bp.route('/testing_git_branches')
def any_function():
    return render_template()

