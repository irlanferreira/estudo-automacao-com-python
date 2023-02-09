import openpyxl

book = openpyxl.load_workbook('example.xlsx')
planilha = book.active

planilha.row_dimensions[1].height = 70
planilha.column_dimensions['C'].width = 800
book.save('joji.xlsx')