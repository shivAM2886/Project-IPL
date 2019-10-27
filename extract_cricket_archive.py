import requests
from requests.auth import HTTPBasicAuth
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup
import re
import xlrd

# For log-in and authorisation
url = "https://cricketarchive.com/cgi-bin/ask_the_player_oracle.cgi"
requests.get(url, auth=HTTPBasicAuth('user_name', 'Password'))

player_name = []

# Extracting player name from an excel file
loc = ("file_path_1")
wb_1 = xlrd.open_workbook(loc)
wb_1_sheet_1 = wb_1.sheet_by_index(0)
for i in range(1,wb_1_sheet_1.nrows):
    player_name.append(str(wb_1_sheet_1.cell_value(i,0)))

loc = ("file_path_2")
wb_1 = xlrd.open_workbook(loc)
wb_1_sheet_1 = wb_1.sheet_by_index(0)
for i in range(1,wb_1_sheet_1.nrows):
    player_name.append(str(wb_1_sheet_1.cell_value(i,0)))

# Season for which records are needed
end_season = "2018"
start_season = "2017"

# file header and out file name
headers = "player_name,Matches,Innings, Not-out, Runs, High-score, Average, 50s, 100s, Balls, Mdns, Runs_given, Wkts_taken, Best_bowling, Average_bowl, CT, ST"+"\n"
out_filename = "D:/UMD/Project/dataset_10/dataset.csv"

f = open(out_filename, "w")
f.write(headers)

for player in player_name:
    match_type = ['All']

    for match in match_type:     # match type can be ODI, TEST, T20I, LIST A OR First-class, refer cricketarchive.com for more info
        try:
            url_2 = "https://cricketarchive.com/cgi-bin/ask_the_player_oracle.cgi?playernumber=&testing=0&opponentmatch=exact&playername="+player+"&resulttype=All&matchtype="+match+"&teammatch=exact&startwicket=&homeawaytype=All&opponent=&endwicket=&wicketkeeper=&searchtype=InningsList&howout=All&endscore=&playermatch=contains&branding=cricketarchive&captain=&endseason="+end_season+"&startscore=&team=&startseason="+start_season+"&testing=0"

            br = RoboBrowser()
            br.open(url_2)

            form = br.get_form()
            br.submit_form(form)

            html_doc = str(br.parsed())

            page_soup = soup(html_doc, 'html.parser')
            rows = page_soup.findAll("td", {"align": "right"})

            for i in range(len(rows)):
                rows[i] = str(rows[i].contents)

            f.write(player)

            for i in range(8, 16):
                f.write("," + re.sub('\W', '', str(rows[i])))
            for i in range(24, 32):
                f.write("," + re.sub('\W', '', str(rows[i])))
            f.write("\n")



        except:
            print("Error for "+player+" in match type "+match)
            f.write("\n")

f.close()

print("Done !!")
