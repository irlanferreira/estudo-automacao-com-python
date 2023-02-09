from datetime import date, timedelta
def diasemana(dt):
    match dt:
        case 0:
            return 'Segunda-Feira'
        case 1:
            return 'Terça-Feira'
        case 2:
            return 'Quarta-Feira'
        case 3:
            return 'Quinta-Feira'
        case 4:
            return 'Sexta-Feira'
        case 5:
            return 'Sábado'
        case 6:
            return 'Domingo'

hoje = date.today() - timedelta(2)
print(hoje.weekday())
acr = timedelta(4)
dia = hoje + acr
for i in range(0, 90):
    with open('diasdaagua.txt', 'a', encoding='utf8') as arq:
        arq.write(f"{'0' if dia.day <= 9 else ''}{dia.day}/{'0' if dia.month <=9 else ''}{dia.month} - {diasemana(dia.weekday())}\n\n")
    dia += acr