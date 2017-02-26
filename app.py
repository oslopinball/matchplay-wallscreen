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
        refresh = request.form.get('refresh')
        return redirect(url_for('tournament', id=id, refresh=refresh))

    return render_template('input.html')

@app.route('/<int:id>/<int:refresh>')
def tournament(id, refresh):
    t = Tournament(id)

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

    return render_template("index.html",
        id=id,
        timestamp = timestamp,
        refresh = refresh,

        name = t.name(),
        type = t.type(),
        status = t.status(),
        maxAttempts = t.maxAttempts(),
        maxAttemptsPlayer = t.maxAttemptsPlayer(),

        playersCount = t.playersCount(),
        playerScoreCount = t.playerScoreCount,
        playersPercent = t.playersPercent(),

        arenas = t.arenas(),
        arenaScoreCount = t.arenaScoreCount,
        arenasPercent = t.arenasPercent(),
        aPercent = t.aPercent(),
        aCount = t.aCount,
        arenasCount = t.arenasCount(),
        attemptsArena = t.attemptsArena(),
        maxAttemptsArena = t.maxAttemptsArena(),

        scores = t.scores,
        standings = t.standings()
    )

if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=config.debug)
