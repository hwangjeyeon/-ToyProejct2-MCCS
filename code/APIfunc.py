import requests
import Info


def getApi_1(res):
    # 공공데이터 포탈에서 제공하는 값이랑 우리가 평소에 생각하는 국가명이랑 달라서 자동으로 바뀌도록 설정한 코드
    if res == "United States":
        res = "United States of America"
    if res == "Hong Kong":
        res = "HongKong"
    if res == "Hong Kong SAR China":
        res = "HongKong"

    # Get 요청을 위한 코드
    url = 'http://apis.data.go.kr/1262000/CountryCodeService2/getCountryCodeList2' \
          '?serviceKey=비공개' \
          '&pageNo=1&numOfRows=300&cond[country_eng_nm::EQ]='
    url += res
    response = requests.get(url)
    contents = response.json()

    # 받아온 데이터를 저장 후 리턴
    contents_array = contents["data"]
    if Info.Alpha2 == 1:
        for content in contents_array:
            return content["country_iso_alp2"]
    '''elif Info.Alpha3 == 1:
        for cot in contents_array:
            return cot["iso_alp3"]'''

def getApi_2(res):
    # Get 요청을 위한 코드
    url = 'http://apis.data.go.kr/1262000/CountryCodeService2/getCountryCodeList2?' \
          'serviceKey=비공개' \
          '&pageNo=1&numOfRows=300&cond[country_iso_alp2::EQ]='
    url += res
    response = requests.get(url)
    contents = response.json()

    # 받아온 데이터를 저장 후 리턴
    contents_array = contents["data"]
    for content in contents_array:
        return content["country_eng_nm"]
