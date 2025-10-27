# https://coderun.yandex.ru/problem/json-with-mistakes/description

import json

with open('test_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

item_with_error = list()

for player in data:
    real_score = 0
    for key, value in player.items():
        if key in ['username', 'score']:
            continue
        real_score += int(value)

    if real_score != int(player['score']):
        item_with_error.append(player['username'])

print('\n'.join(sorted(item_with_error)))
