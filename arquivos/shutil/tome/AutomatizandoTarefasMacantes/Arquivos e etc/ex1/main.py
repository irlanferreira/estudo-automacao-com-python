import random, os
dados = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':
'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon':
'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina':
'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':
'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quizNum in range(35):
    estados = list(dados.keys())
    capitais = list(dados.values())

    random.shuffle(estados)
    random.shuffle(capitais)

    quizFile = open(f".\\provas\\prova{quizNum}.txt", 'w+')
    quizFile.write(f"{'='*20}PROVA DO BALACOBACO{'='*20}\n\n\n")

    gabarito = open(f".\\provas\\gabaritos\\gabarito{quizNum}.txt", 'w')

    for i, p in enumerate(estados):
        quizFile.write(f"Qual a capital do(a) {p}?\n\n")
        respostaCerta = dados[p]
        respostasErradas = list(dados.values())
        del respostasErradas[respostasErradas.index(respostaCerta)]
        respostasErradas = random.sample(respostasErradas, 3)
        respostas = respostasErradas
        respostas.append(respostaCerta)
        random.shuffle(respostas)
        gabarito.write(f"{i+1}.{'ABCD'[respostas.index(respostaCerta)]}\n")
        for i, r in enumerate(respostas):
            quizFile.write(f'({"ABCD"[i]}).{r}\n')
        quizFile.write('\n\n')