from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
page_url = 'https://www.iplt20.com/teams/mumbai-indians/squad/113/yuvraj-singh'
file_name_1 = page_url.split("/", 7)[7]

uClient = uReq(page_url)

page_soup = soup(uClient.read(), "html.parser")
uClient.close()

out_filename = 'D:/UMD/Project/Player_data_2019/Chennai_Super_Kings_2019/' + file_name_1 + '.csv'

f = open(out_filename, "w")

# Player Details
player_role_label = page_soup.findAll("td", {"class": "player-details__label"})
player_role_value = page_soup.findAll("td", {"class": "player-details__value js-value"})

stat_category_1 = page_soup.findAll(['th', 'tr', 'b'])


# Gets Overall IPL Career Highlights
# Gives both overall highlights
row_overall_IPL_career = page_soup.findAll("tr", {"class": "player-stats-table__highlight"})

# Gets year by year IPL Career Record
# Gives both Batting and Bowling >> Needs to be segregated
rows = page_soup.findAll("tr")

for row in rows:
    i = 0
    cells = row.findAll(["td", "th"])
    for cell in cells:
        i = i + 1
        if str(cell.contents) == "[<b>Batting and Fielding</b>]":
            f.write('Batting and Fielding' + '\n')
        elif str(cell.contents) == "[<b>Bowling</b>]":
            f.write('Bowling' + '\n')
        elif i == len(cells):
            if str(cell.contents) == '[-]':
                f.write(re.sub('\W', '', None + '\n'))
            else:
                f.write(re.sub('\W', '', str(cell.contents)) + '\n')
        else:
            if str(cell.contents) == '[-]':
                f.write(re.sub('\W', '', None + ','))
            f.write(re.sub('\W', '', str(cell.contents)) + ',')


f.close()
