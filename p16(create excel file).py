import openpyxl
from openpyxl import Workbook
import os
filepath=r".\pyxl.xlsx"
if not os.path.exists(filepath):
    workbook=Workbook()
    sheet=workbook.active
    sheet["A1"]="Title"
    sheet["B1"]="Name"
    workbook.save(filename="pyxl.xlsx")
workbook=openpyxl.load_workbook(filepath)
sheet=workbook.active

n=int(input('Enter number of records to add ?'))

for i in range(n):
    title=input('Enter Title :')
    name=input('Enter Name :')
    sheet.append([title,name])
    workbook.save(filename="pyxl.xlsx")
    
    
    

                                    
