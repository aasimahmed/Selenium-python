import openpyxl
import math
path = "C:\\Users\\aahme\\Desktop\\testexcel.xls"
workbook = openpyxl.load_workbook(path)

sheet = workbook.active #Or Workbook.getSheetByName("")

for i in range(1, 5):
    for c in range(0, 4):
        sheet.cell(row=i,column=c).value = "test"

workbook.save(filename=path)

