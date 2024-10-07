import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

csvFile = open('test.csv','w',encoding = 'UTF-8')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number+2','(number+2)^2'))

    for i in range(10):
        writer.writerow((i,i+2,pow(i+2,2)))
except Exception as e:
    print(e)
finally:
    csvFile.close()

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html,'html.parser')

table = bs.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

csvFile = open('editor.csv','wt',encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['th','td']):
            print(cell.text.strip())
            csvRow.append(cell.text.strip())
        writer.writerow(csvRow)
finally:
    csvFile.close()