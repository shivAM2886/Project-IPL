from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

#Enter name of player to extract information for
player_list = []
for player in range(len(player_list)):
    try:
        player_name = player_list[player]
        first_name = player_name.split(' ')[0]
        last_name = player_name.split(' ')[1]

        page_url_1 = 'http://stats.espncricinfo.com/ci/engine/stats/analysis.html?search='+first_name+'+'+last_name
        ';template=analysis'
        uClient_1 = uReq(page_url_1)

        page_soup_1 = soup(uClient_1.read(), "html.parser")
        uClient_1.close()

        temp = page_soup_1.find("a", {"class": "statsLinks"})
        temp_1 = str(temp).split(".")[0]
        player_num = str(temp_1).split('/')[-1]
        
        #enter class = 1 for test record and class = 3 for t20 records
        page_url = 'http://stats.espncricinfo.com/ci/engine/player/' + player_num + '.html?class=2;template=results;type=allround'

        headers = "Matches,Blank, Innings, Not-out, Runs, High-score, Balls-faced, Strike-rate, 100s, 50s, duck, 4s, 6s" + "\n"

        uClient = uReq(page_url)
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()

        out_filename = "D:/UMD/Project/Player_ODI_data/" + player_list[player] + ".csv"
        f = open(out_filename, "w")
        f.write(headers)

        rows = page_soup.findAll("tr", {"class": "data1"})
        row_array = []
        for row in rows:
            cells = row.findAll("td")  # finds all the <td> tag
            temp = 0  # temp_check is used to print only those <td> tags which have year-wise data with it
            i = 1  # i_check is done to change rows
            for cell in cells:
                i = i + 1
                if 'year' in str(cell.contents):
                    temp = temp + 1
                if i == len(cells) and temp == 1:
                    f.write(re.sub('\W', '', str(cell.contents)) + '\n')  # re.sub removes all the extra chars.
                elif temp == 1:
                    f.write(re.sub('\W', '', str(cell.contents)) + ',')
        print(player_list[player]+" >> data_extraction is complete")
        f.close()
    except:
        print(player_list[player]+" Unsuccessful attempt at data extraction")

print("Executed !!!")
