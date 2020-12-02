
players = []
with open('./jatekosok.txt', 'r') as f:
    for line in f:
        # a sorvége jeleket (entereket: \n karaktert...) leszedjük a sorok végéről:
        line = line.strip()
        # szétbontjuk a sort, listává alakítjuk, a delimiterünk pedig a szóköz karakter
        player_list = line.split(' ')
        # majd létrehozunk egy dictionary-t
        # meghatározott key-ekkel, a value-k pedig a lista aktuális eleme...
        player = {"name": player_list[0],
                  "age": int(player_list[1]),
                  "nationality": player_list[2],
                  "score": int(player_list[3])}
        # hozzáfűzzük a player dictionary-t a players listához
        players.append(player)

print(players)

nationalities = set()
for player in players:
    nationalities.add(player['nationality'])

# az előző sor set comprehension-nel
# nationalities = {player['nationality] for player in players}
print(nationalities)

scores = {}
for nationality in nationalities:
    # létrehozzuk a scores dictionary-ben az új nationality-t nulla értékkel
    scores[nationality] = 0
    for player in players:
        if player['nationality'] == nationality:
            scores[nationality] += player['score']
print(scores)

underage = []
for player in players:
    if player['age'] < 20:
        underage.append(player)
print(underage)
print("a kiskorúak száma: {}".format(len(underage)))

# házi feladat: készítsd el az eredmény kihirdetést,
# és írd ki az eredményt egy file-ba, az eredmeny.txt file
# tartalma így nézzen ki:
# 1. English: 101
# 2. Hungarian: 90
# 3. Spanish: 49

# dictionary-n belül nem lehet sorba rendezni (ahhoz objectet, meg classot kellene tanulnunk)
# muszáj valami mást csinálni
# pl. létrehozok egy listát és úgy teszem bele:
# lista első eleme a maximum, remove-olva az eredeti dictionary-ból stb.
# amikor megtalálja a nagyobb elemet, kiveszi, és úgy rakja át listába
# szóval utána a másodikat, majd a harmadikat
# [['English', 101], ['Hungarian', 90]...]

print(scores)

sorted_scores = []
for k in sorted(scores, key=scores.get, reverse=True)
sorted_scores.append((k, scores[k]))

# sorted_scores = [(k, scores[k])
#                 for k in sorted(scores, key=scores.get, reverse=True)]

with open('eredmeny.txt', 'w') as file:
    for i, score in enumerate(sorted_scores):
        file.write('{}. {}: {}\n'.format(i+1, score[0], score[1]))
