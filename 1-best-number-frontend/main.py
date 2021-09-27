from __future__ import print_function, unicode_literals

import requests
from PyInquirer import prompt

ACTION = 'action'
GET_BEST_NUMBER = 'Get best number'
SET_BEST_NUMBER = 'Set best number'

BEST_NUMBER = 'best_number'

questions = [
    {
        'type': 'list',
        'name': ACTION,
        'message': 'What do you want to do?',
        'choices': [
            GET_BEST_NUMBER,
            SET_BEST_NUMBER
        ]
    },
    {
        'type': 'input',
        'name': BEST_NUMBER,
        'message': 'Enter you favorite number: ',
        'when': lambda answers: answers.get('action') == SET_BEST_NUMBER
    }
]

answers = prompt(questions)

if answers[ACTION] == GET_BEST_NUMBER:
    response = requests.get('http://localhost:8000/bestnumber')
    print(response.text)

elif answers[ACTION] == SET_BEST_NUMBER:
    response = requests.post('http://localhost:8000/bestnumber', json={'bestNumber': int(answers[BEST_NUMBER])})
    if response.status_code == 200:
        print('Best number saved')
    else:
        print('Failed to save best number')
