import pandas as pd
import requests
from bs4 import BeautifulSoup
import MakeGolfListSub as sub


years = [2020, 2019, 2018] # 수집할 정보의 연도
rank = 60 # 수집할 선수 60명 (1위-60위) official money 기준

url=[]
name=[]
groupV=[]
officialMoney=[]

for year in years:
    response=requests.get("https://www.lpga.com/statistics/money/official-money?year={year}".format(year=year))
    soup=BeautifulSoup(response.text, 'html.parser')
    response.close()

    url.append((sub.playerUrlList(soup,rank))) # official money 기준 1위-60위 선수들의 url 리스트에 저장
    name.append(sub.playerNameList(soup, rank)) # 1위-60위 선수들의 이름 리스트에 저장
    officialMoney.append(sub.playerOfficialMoneyList(soup, rank)) # 1위-60위 선수들의 official money 리스트에 저장
    groupV.append(sub.playerGroupVariableList(soup, rank)) # 1위-60위 선수들의 국가 정보 리스트에 저장


playerInfo =[]
# 수집할 선수의 스탯들
infos = ['driving/average-driving-distance','driving/driving-accuracy','scoring/scoring-average', 'scoring/top-10-finishes-percentage',
         'scoring/birdies', 'scoring/eagles', 'scoring/par-3-averages', 'scoring/par-4-scoring-averages', 'scoring/par-5-scoring-average',
         'short-game/greens-in-reg', 'short-game/sand-saves', 'short-game/putting-average']
loc = [-1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1] #column's location in table # 페이지에서 수집할 데이터의 위치

for year in years:
    for i in range(0,len(infos)):
        response=requests.get(f"https://www.lpga.com/statistics/{infos[i]}?year={year}")
        page=BeautifulSoup(response.text, 'html.parser')
        response.close()

        playerInfo.append(sub.playerInformationList(page, url[years.index(year)], loc[i]))

for i in range(0,len(playerInfo)):
    print(playerInfo[i]) # 수집된 정보 출력 :: 36(스탯 12개, 3개년) * 60(60명의 선수)


#driving distance
#driving accuracy (%)
#scoring average
#Top 10 finishes %
#birdies
#Eagles
#par 3,4,5
#green in regulation
#sand saves (%)
#putting average

for i in range(0,len(years)):
    df = pd.DataFrame({
        'Year': years[i],
        'Group Variable': groupV[i],
        'Name': name[i],
        'OM(Official money)':officialMoney[i],
        'DD(driving distance)': playerInfo[0+len(infos)*i],
        'DA(driving accuracy': playerInfo[1+len(infos)*i],
        'SA(Scoring average)': playerInfo[2+len(infos)*i],
        'T10F': playerInfo[3+len(infos)*i],
        'Bir(Birdies)': playerInfo[4+len(infos)*i],
        'Eag(Eagles)': playerInfo[5+len(infos)*i],
        'Par3':playerInfo[6+len(infos)*i],
        'Par4':playerInfo[7+len(infos)*i],
        'Par5':playerInfo[8+len(infos)*i],
        'GIR(green in regulation)': playerInfo[9+len(infos)*i],
        'SS(sand saves)': playerInfo[10+len(infos)*i],
        'PA(putting average)': playerInfo[11+len(infos)*i],
    })

    df.to_excel(f'./year{i}.xlsx')

