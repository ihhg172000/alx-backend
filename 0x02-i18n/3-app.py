#!/usr/bin/env python3
"""
0-app.py
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get_locale """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """ index """
    return render_template("0-index.html", home_title=_("home_title"), home_header=_("home_header"))


if __name__ == "__main__":
    app.run(debug=True)
