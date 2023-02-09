import openpyxl
from openpyxl.styles import Font

book = openpyxl.load_workbook('example.xlsx')
planilha = book.active
fonte = Font(bold=True, size=14)
planilha['A1'].font = fonte