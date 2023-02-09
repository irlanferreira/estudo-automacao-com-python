import openpyxl

book = openpyxl.load_workbook('example.xlsx')
plan = book.active
plan.freeze_panes = 'A2'
book.save('joji.xlsx')
