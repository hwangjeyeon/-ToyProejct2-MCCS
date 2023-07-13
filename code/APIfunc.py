
import requests
import json
import Info


#url = 'http://apis.data.go.kr/1262000/CountryCodeService2/getCountryCodeList2?serviceKey=비공개&pageNo=1&numOfRows=300'
#response = requests.get(url)
#contents = response.json()
#print(contents)
def getApi_1(res):
    if res == "United States":
        res = "United States of America"
    if res == "Hong Kong":
        res = "HongKong"
    if res == "Hong Kong SAR China":
        res = "HongKong"
    else:
        pass
    url = 'http://apis.data.go.kr/1262000/CountryCodeService2/getCountryCodeList2?serviceKey=비공개&pageNo=1&numOfRows=300&cond[country_eng_nm::EQ]='
    url += res
    #print(url)
    response = requests.get(url)
    contents = response.json()

    contents_array = contents["data"]
    if Info.Alpha2 == 1:
        for cot in contents_array:
            return cot["country_iso_alp2"]
    '''elif Info.Alpha3 == 1:
        for cot in contents_array:
            return cot["iso_alp3"]'''

def getApi_2(res):
    url = 'http://apis.data.go.kr/1262000/CountryCodeService2/getCountryCodeList2?serviceKey=비공개&pageNo=1&numOfRows=300&cond[country_iso_alp2::EQ]='
    url += res
    response = requests.get(url)
    contents = response.json()

    contents_array = contents["data"]
    for cot in contents_array:
        return cot["country_eng_nm"]
