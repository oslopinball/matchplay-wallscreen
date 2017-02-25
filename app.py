#!/usr/bin/env python3

from flask import Flask, render_template, g, request, redirect, url_for
import config

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form.get('id')
        return redirect(url_for('tournament', id=id))

    return render_template('input.html')

@app.route('/<int:id>')
def tournament(id):
    return render_template("index.html", id=id)

if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=config.debug)
