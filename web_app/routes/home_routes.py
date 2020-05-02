from flask import Blueprint, render_template, redirect, flash, request 
import requests
from web_app.routes.zodiac import get_sign

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGES")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    #return "About Me (TODO)"
    return render_template("about.html")

@home_routes.route("/zodiacresult", methods=["POST"]) 
def sign():
    day = request.form["day"]
    month = request.form["month"]
    #print (sex)
    return render_template("zodiacresult.html")