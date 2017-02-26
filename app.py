#!/usr/bin/env python3

from flask import Flask, render_template, g, request, redirect, url_for
import time
import datetime
import config
from api import Tournament

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form.get('id')
        return redirect(url_for('tournament', id=id))

    return render_template('input.html')

@app.route('/<int:id>')
def tournament(id):
    t = Tournament(id)

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

    return render_template("index.html",
        id=id,
        timestamp = timestamp,
        name = t.name(),
        type = t.type(),
        status = t.status(),

        maxAttemptsPlayer = t.maxAttemptsPlayer(),

        playersCount = t.playersCount(),
        arenasCount = t.arenasCount(),

        attemptsArena = t.attemptsArena(),
        maxAttemptsArena = t.maxAttemptsArena(),

        arenas = t.arenas(),
        standings = t.standings()
    )

if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=config.debug)
