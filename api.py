#!/usr/bin/env python3

import json
import requests

class Tournament:
    def __init__(self, id):
        print("* tournament: " + str(id))

        self.id = id
        self.r = requests.get('https://matchplay.events/api-beta/tournaments/' + str(self.id))
        self.r.raise_for_status()
        self.tournament = json.loads(self.r.content.decode('utf-8'))

        self.scores = {}

        for arena in self.arenas():
            if arena['tournament']['status'] == "active":
                arena_id = arena['arena_id']
                #print("  * Arena: " + str(arena_id) + " - " + arena['tournament']['status'])
                self.scores[arena_id] = self.arenaScores(arena_id)

        self.playersScoreCount()
        self.arenasScoreCount()

    def name(self):
        return self.tournament['name']

    def type(self):
        return self.tournament['type']

    def status(self):
        return self.tournament['status']

    def maxAttemptsPlayer(self):
        return self.tournament['overall_attempts']

    def attemptsArena(self):
        return self.tournament['attempts_per_arena']

    def maxAttemptsArena(self):
        return self.playersCount() * self.attemptsArena()

    def maxAttempts(self):
        return self.playersCount() * self.maxAttemptsPlayer()

    def playersCount(self):
        return len(self.tournament['players'])

    def arenasCount(self):
        return len(self.tournament['arenas'])

    def arenas(self):
        return self.tournament['arenas']

    def players(self):
        return self.tournament['players']

    def standings(self):
        print("* standings")

        self.r = requests.get('https://matchplay.events/api-beta/tournaments/' + str(self.id) + '/standings')
        self.r.raise_for_status()
        self.jj = json.loads(self.r.content.decode('utf-8'))

        return self.jj

    def arenaScores(self, arena_id):
        print("* arena scores: " + str(arena_id))

        self.r = requests.get('https://matchplay.events/api-beta/tournaments/' + str(self.id) + '/arenas/' + str(arena_id) + '/scores')
        self.r.raise_for_status()
        self.jjj = json.loads(self.r.content.decode('utf-8'))

        return self.jjj

    def playersScoreCount(self):
        #print("* playersScoreCount")

        self.playerScoreCount = {}

        for player in self.players():
            self.playerScoreCount[player['player_id']] = 0

        for arena, scores in self.scores.items():
            for score in scores:
                self.playerScoreCount[score['player_id']] += 1

    def playersPercent(self):
        p = {}
        for player in self.players():
            percent = round((float(self.playerScoreCount[player['player_id']]) / float(self.maxAttemptsPlayer())) * 100)
            p[player['player_id']] = percent

        return p

    def arenasScoreCount(self):
        self.arenaScoreCount = {}
        count = 0
        self.aCount = 0

        for arena in self.arenas():
            self.arenaScoreCount[arena['arena_id']] = 0

            if arena['tournament']['status'] == "active":
                count = len(self.scores[arena['arena_id']])
                self.aCount += count
                self.arenaScoreCount[arena['arena_id']] = count

    def arenasPercent(self):
        a = {}
        for arena in self.arenas():
            percent = round((float(self.arenaScoreCount[arena['arena_id']]) / float(self.maxAttemptsArena())) * 100)
            a[arena['arena_id']] = percent

        return a

    def aPercent(self):
        return round((float(self.aCount) / float(self.maxAttempts())) * 100)
