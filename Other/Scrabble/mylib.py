import random
import codecs
from itertools import permutations


lexiko = {}


points = {'Α': 1, 'Β': 8, 'Γ': 4, 'Δ': 4, 'Ε': 1, 'Ζ': 10, 'Η': 1, 'Θ': 10, 'Ι': 1, 'Κ': 2, 'Λ': 3, 'Μ': 3,
          'Ν': 1, 'Ξ': 10, 'Ο': 1, 'Π': 2, 'Ρ': 2, 'Σ': 1, 'Τ': 1, 'Υ': 2, 'Φ': 8, 'Χ': 8, 'Ψ': 10, 'Ω': 3}


class SakClass:

    def __init__(self):
        self.letters = 102
        self.lettersList = [12, 1, 2, 2, 8, 1, 7, 1, 8, 4, 3, 3, 6, 1, 9, 4, 5, 7, 8, 4, 1, 1, 1, 3]

    def randomLetters(self, n):
        playerLetters = []
        for i in range(n):
            x = random.randint(0, 23)
            while self.lettersList[x] == 0:
                x = random.randint(0, 23)
            if x >= 17:
                temp = {chr(ord('Α') + x + 1): points[chr(ord('Α') + x + 1)]}
            else:
                temp = {chr(ord('Α') + x): points[chr(ord('Α') + x)]}
            playerLetters.append(temp)
            self.letters -= 1
            self.lettersList[x] -= 1
        return playerLetters


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.playerLetters = []


class PcPlayer:
    def __init__(self):
        self.score = 0
        self.playerLetters = []

    def minLetters(self):
        pcLetters = ''
        for i in self.playerLetters:
            pcLetters += list(i.keys())[0]
        pcString = ''.join(pcLetters)
        for i in range(2, 7):
            pcWords = [''.join(p) for p in permutations(pcString, i)]
            for word in pcWords:
                if word in lexiko:
                    return word
        return 'q'

    def maxLetters(self):
        pcLetters = ''
        for i in self.playerLetters:
            pcLetters += list(i.keys())[0]
        pcString = ''.join(pcLetters)
        for i in range(7, 2, -1):
            pcWords = [''.join(p) for p in permutations(pcString, i)]
            for word in pcWords:
                if word in lexiko.keys():
                    return word
        return 'q'

    def smart(self):
        pcLetters = ''
        maxWord = ''
        maxScore = 0
        for i in self.playerLetters:
            pcLetters += list(i.keys())[0]
        pcString = ''.join(pcLetters)
        for i in range(2, 7):
            pcWords = [''.join(p) for p in permutations(pcString, i)]
            for word in pcWords:
                if word in lexiko.keys():
                    if lexiko[word] > maxScore:
                        maxWord = word
                        maxScore = lexiko[word]
        if maxWord != '':
            return maxWord
        else:
            return 'q'


def makeFile():

    with codecs.open('greek7.txt', 'r', encoding='utf8') as gr:

        for line in gr:

            scoreLexis = 0
            for i in line:
                if i != '\n':
                    scoreLexis += points[i]
            temp = {line[:-1]: scoreLexis}
            lexiko.update(temp)
