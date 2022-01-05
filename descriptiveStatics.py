#국적을 다음 4가지로 분류한다.
import pandas as pd

list_1=['Republic of Korea'] # 한국
list_2=['United States', 'Mexico', 'Canada'] # 미국으로 분류될 국가 목록
list_3=['France','Germany', 'Northern Ireland', 'Spain', 'Denmark', 'England', 'Sweden'] # 유럽으로 분류될 국가 목록
list_4=['Philippines', 'Australia', 'New Zealand', 'Japan', 'Thailand', 'Chinese Taipei', 'South Africa', 'China', 'Malaysia'] # 아시아로 분류될 국가 목록

for i in range(3):
    groupID=[]
    year = 2018+i
    df=pd.read_excel(f'year{year}.xlsx')
    del(df['Unnamed: 0'])
    for index in df['Group Variable']:
        if index in list_1:
            groupID.append(1) # 한국
        elif index in list_2:
            groupID.append(2) # 미국
        elif index in list_3:
            groupID.append(3) # 유럽
        elif index in list_4:
            groupID.append(4) # 아시아
        else:
            groupID.append(0) # 그 외(있으면 안되니 확인 후 4가지 분류 리스트에 추가해주자)

    print(groupID)

    df['groupID']=groupID
    df.to_excel(f'./Final{year}.xlsx')

