#!/usr/bin/env python3
"""
0-app.py
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_user():
    """ get_user """
    user_id = request.args.get("login_as")

    if user_id and user_id.isdigit():
        return users.get(int(user_id))


@app.before_request
def before_request():
    """ before_request """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ get_locale """
    locale = request.args.get("locale")

    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """ index """
    user = g.get("user")
    username = user.get("name") if user else None

    return render_template("5-index.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
