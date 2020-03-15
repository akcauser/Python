from openpyxl import Workbook

wb = Workbook()

ws1  = wb.create_sheet("sayfa_1")

ws1['C5'].value = '112312312'
ws1['C6'].value = 'Sultan'
ws1['C7'].value = 'Akçor'

wb.save(filename = 'kitap_5.xlsx')


