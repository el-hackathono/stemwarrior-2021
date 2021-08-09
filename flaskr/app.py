"""Our script for dynamic page serving."""

import os
from smtplib import SMTPRecipientsRefused
import sqlite3

from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME="zainyusufazam2@gmail.com",  # zain's throwaway
    MAIL_PASSWORD=os.environ["GMAIL_PASS"]  # fun fact, password is: "GULLIBLE"
)

mail = Mail(app)


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


@app.route("/portals/signin")
def signin():
    """Fake facebook page."""
    return render_template("facebookClone.htm")


@app.route("/portals/signin", methods=["POST"])
def steal():
    """Swipes your login info."""
    email = request.form["email"]
    password = request.form["encpass"]

    conn = sqlite3.connect("data/app.db")
    pledges = conn.execute("SELECT pledges FROM statistics WHERE 'date' = (SELECT MAX('date') FROM statistics)").fetchone()[0]
    conn.close()

    try:
        msg = Message(
            subject="Phishing page",
            sender=("ZADZ Education", "zainyusufazam2@gmail.com"),
            recipients=[email],
            html=f"""
            <p>This is what a phishing page looks like.<br />
            Here are some things that you should have noticed.</p>

            <ul>
                <li>The URL did not include facebook.com</li>
                <li>Many links were broken</li>
                <li>You can check for the website's "SSL certificate". This shows if the website is authentic. <a href='https://www.verisign.com/en_US/website-presence/online/ssl-certificates/index.xhtml'>Click here to learn more.</a></li>
            </ul>

            <p>Never log in without verifying that the site is safe! Your encrypted password was: <code>{password}</code>. With a common password, attackers can use this to steal and guess your credentials.</p>
            <p>Never trust emails that ask for money by revealing your password to you. Instead, change it and move on.</p>
            <p>Pledge along with {pledges} other people to complete this task.</p>
            <p><a href='zadz-education.herokuapp.com/pledge'><em>I understand.</em></a></p>
            """
        )

        mail.send(msg)
    except SMTPRecipientsRefused as e:
        # invalid email
        return redirect(url_for("signin"))

    return redirect(url_for("alert"))


@app.route("/portals/alert")
def alert():
    """Fake facebook page."""
    return render_template("alert.html")


@app.route("/portals/mission")
def mission():
    """Fake facebook page."""
    return render_template("mission.html")


@app.route("/pledge")
def pledge():
    """Fake facebook page."""
    conn = sqlite3.connect("data/app.db")
    conn.execute("UPDATE statistics SET pledges = pledges + 1 WHERE 'date' = (SELECT MAX('date') FROM statistics)")
    conn.commit()
    conn.close()
    return redirect(url_for("alert"))
