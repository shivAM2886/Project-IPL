from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup

import xlrd

# list to store player names
player_name = []

# file location from which player names are being extracted
loc = ("D:/UMD/Project/data-sets/player_name.xlsx")
wb_1 = xlrd.open_workbook(loc)
wb_1_sheet_1 = wb_1.sheet_by_index(0)
for i in range(1, wb_1_sheet_1.nrows):
    player_name.append(str(wb_1_sheet_1.cell_value(i, 0)))

# headers of the output file
headers = "player_name, Age"+"\n"
out_filename = "D:/UMD/Project/data-sets/dataset_age.csv"

f = open(out_filename, "w")
f.write(headers)

for player in player_name:

    try:
        url = "http://www.espncricinfo.com/ci/content/player/index.html"
        br = RoboBrowser()
        br.open(url)

        form = br.get_form()
        form['search'] = str(player)
        br.submit_form(form)

        html_doc = str(br.parsed())
        page_soup = soup(html_doc, 'html.parser')
        rows = page_soup.findAll("p", {"class": "ColumnistSmry"})

        temp = str(rows[0]).split(".")[0]
        player_num = str(temp).split('/')[-1]

        url_2 = "http://www.espncricinfo.com/india/content/player/" + player_num + ".html"
        br.open(url_2)
        html_doc_2 = str(br.parsed)

        page_soup_2 = soup(html_doc_2, 'html.parser')
        rows_2 = page_soup_2.findAll("p", {"class" : "ciPlayerinformationtxt"})

        temp_2 = str(rows_2[2]).split(">")
        temp_2 = temp_2[4].split(" ")[0]

        age = temp_2
        f.write(player + "," + str(age)+"\n")
        print(player+" done :)")

    except:
        f.write(player + "," + "0" + "\n")
        print(player+" not done :(")



print("Done !!")
