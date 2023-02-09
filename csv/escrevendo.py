import csv
outputarq = open('escrito.csv', 'w', newline='')
escriba = csv.writer(outputarq, delimiter='\t', lineterminator='\n')

escriba.writerow(['kipilipitiki', '98', 'oi@gmail.com'])
escriba.writerow(['lunnabea', '467845', 'apwfjmp@hotmail.com'])

outputarq.close()
