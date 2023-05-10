from requests_html import HTMLSession
import datetime

    
now = datetime.datetime.now()
file = open("data.txt", "w")


# Pick selected matchs to check by number(without M),
# For example Argentina´s are 8, 24 and 39 (M8, M24 and M39 respectively)

pick = [8, 24, 39]
pickedMatches = []
totalMatches = []


def getMatches():
    s = HTMLSession()
    URL = "https://fcfs-intl.fwc22.tickets.fifa.com/secure/selection/event/date/product/101397570845/lang/en"
    r   = s.get(URL)
    matchesHTML = r.html.find('div.perf_details')
    for matchHTML in matchesHTML:
        totalMatches.append(matchHTML.text)


def AddMatches():
    i = 0
    while i < len(pick):
        pickedMatches.append(totalMatches[pick[i] - 1])
        i += 1


# Consulta matches and overwrite data.txt with new data

def ConsultMatches():
    file.write('Time: ' + now.strftime('%H:%M:%S\n\n'))
    print('Time: ' + now.strftime('%H:%M:%S\n'))
    i = 0
    while i < len(pickedMatches):
        file.write(pickedMatches[i]+"\n\n")
        if pickedMatches[i].find("Currently unavailable") != -1:
            print(f"Match M{pick[i]} not available")
            i += 1
        else:
            print(f"Match M{pick[i]} available")
            i += 1
def RunApp():
    getMatches()
    AddMatches()
    ConsultMatches()
    file.close()


AddMatches()
ConsultMatches()
