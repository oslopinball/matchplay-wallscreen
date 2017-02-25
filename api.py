#!/usr/bin/env python3

import json
import requests

class Tournament:
    def __init__(self, id):
        self.id = id

        self.r = requests.get('https://matchplay.events/api-beta/tournaments/' + str(self.id))
        self.r.raise_for_status()
        self.tournament = json.loads(self.r.content.decode('utf-8'))
        print("* tournament")#self.tournament)

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
