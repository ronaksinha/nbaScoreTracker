import requests
from bs4 import BeautifulSoup
import re
import time
def re_helper(x):
    txt = str(x)
    x = re.findall(r"[0-9]", txt)
    new_x = ''
    for i in x:
        new_x+=i
    return new_x


def fetchFromWeb(url):
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')

    a = (soup.findAll(class_="score icon-font-after"))
    b = (soup.findAll(class_="score icon-font-before"))
    new_a = re_helper(a)
    new_b = re_helper(b)

    return(int(new_a), int(new_b))

def calcSmokCond(currA, prevA, currB, prevB):
    if (min(currA-prevA,currB-prevB) >= 10):
        prevA = currA
        prevB = currB
        return(prevA, prevB, True)
    else:
        return (prevA, prevB, False)

if __name__ == "__main__":
    print("Example url should look like https://www.espn.com/nba/boxscore/_/gameId/401337344")
    url = input("Enter ESPN boxscore for the game you're watching: ")
    prevA = 0
    prevB = 0
    prevA, prevB = fetchFromWeb(url)
    smokyet = False
    while True:
        currA, currB = fetchFromWeb(url)
        prevA, prevB, smokyet = calcSmokCond(currA, prevA, currB, prevB)
        print(currA, currB)
        if smokyet is True:
            print("!!!!SMOK TIME BITCH!!!!")
        time.sleep(5)