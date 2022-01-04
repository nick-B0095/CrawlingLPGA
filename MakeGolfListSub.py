# import requests
# from bs4 import BeautifulSoup

# response=requests.get("https://www.lpga.com/statistics/driving/average-driving-distance?year=2020")
# soup=BeautifulSoup(response.text, 'html.parser')
# response.close()

#golf player

def playerUrlList(paper, rank):
    urls=paper.findAll('tr',{'class':'body'})
    url_list=[url.find('a')['href'][:-8] for url in urls]
    url_list=url_list[:rank]

    return url_list

def playerNameList(paper, rank):
    names=paper.findAll('td',{'class':'table-content left'})

    name_list=[str.strip(name.text) for name in names]
    name_list=name_list[:rank]

    return name_list

def playerOfficialMoneyList(paper, rank): #Official money(OM)
    official_moneys=paper.findAll('td',{'class':'table-content'})
    official_moneys=official_moneys[::2]
    official_moneys=official_moneys[1:2*rank:2]

    official_money_list=[str.strip(money.text) for money in official_moneys]

    return official_money_list

def playerGroupVariableList(paper, rank):
    images=paper.findAll('img')

    group_variable_list=[image.get('alt') for image in images]
    group_variable_list=group_variable_list[1:rank+1]

    return group_variable_list

def playerInformation(bodys, url, loc):
    try:
        info=[str.strip(body.findAll('td')[loc].text) for body in bodys if body.find('a')['href'][:-8]==url]
        return info[0]
    except:
        return '-'

def playerInformationList(paper, urls, loc):
    info=[]
    bodys=paper.findAll('tr',{'class':'body'})
    for url in urls:
        info.append(playerInformation(bodys, url, loc))
    return info
