from openpyxl import Workbook

wb = Workbook()

ws1  = wb.create_sheet("sayfa_1")

wb.save(filename = 'kitap_1.xlsx')


