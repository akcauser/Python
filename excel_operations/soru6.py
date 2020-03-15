from openpyxl import Workbook

wb = Workbook()

ws1  = wb.create_sheet("sayfa_1")

for i in range(20):
    i = i+1
    cell_sayi = 'A'+str(i)
    cell_kare = 'B' + str(i)
    cell_kup = 'C' + str(i)
    ws1[cell_sayi] = i
    ws1[cell_kare] = i*i
    ws1[cell_kup] = i*i*i

wb.save(filename = 'kitap_6.xlsx')


