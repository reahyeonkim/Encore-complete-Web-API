# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:17:09 2021

@author: Playdata

Web_API

웹 API의 이해 : 서버가 요청된 내용을 응답처리하기위한 명세
웹 API의 데이터 획득 과정 :
    REST API : 텍스트 기반 / 응답처리하면 자동으로 접속 끊김
    Streaming API : 음원, 동영상 기반 / 이벤트를 동하여 서비스가 이루어지기 때문에 별도의 요청이 없으면 접속유지
웹 API의 인증 방식 
    OAuth 인증방식이 보편화 
    인증키(API Key) 만 요청
    인증키(API Key)와 접속 토큰 요청
    인증키(API Key)와 접속 토큰 및 비밀번호가지 요청
"""

### 응답 데이터의 형식 및 처리
"""
응답 데이터의 형식
REST API : 
    JSON : key(문자열) 와 value(값:문자열, 숫자, 객체({key:value}), 배열등)
    XML : HTML 처럼 태그 형식 구조
    
    JSON이나 XML 모두 계층적 구조를 가지고 있슴
    응답 데이터는 줄바꿈, 탭이 없이 한줄로 응답됨
    JSON이 XML 보다 조금더 빠르고, 분석이 용이
"""

#### JSON 형식의 데이터 처리
## 1. 파이썬 데이터 => JSON 형식 : json.dumps() 를 이용.
# 모듈 import
import json

# 테스트용 파이썬 데이터 : dict
python_dict = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}
type(python_dict)
'''
dict
'''

# dict => JSON : option 사용하지 않았을 경우
json_data = json.dumps(python_dict)
'''
'{"\\uc774\\ub984": "\\ud64d\\uae38\\ub3d9", "\\ub098\\uc774": 25, "\\uac70\\uc8fc\\uc9c0": "\\uc11c\\uc6b8", "\\uc2e0\\uccb4\\uc815\\ubcf4": {"\\ud0a4": 175.4, "\\ubab8\\ubb34\\uac8c": 71.2}, "\\ucde8\\ubbf8": ["\\ub4f1\\uc0b0", "\\uc790\\uc804\\uac70\\ud0c0\\uae30", "\\ub3c5\\uc11c"]}'
'''

type(json_data)
'''
str
'''

# dict => JSON : 
json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
'''
'{\n   "거주지": "서울",\n   "나이": 25,\n   "신체정보": {\n      "몸무게": 71.2,\n      "키": 175.4\n   },\n   "이름": "홍길동",\n   "취미": [\n      "등산",\n      "자전거타기",\n      "독서"\n   ]\n}'
'''
print(json_data)
'''
{
   "거주지": "서울",
   "나이": 25,
   "신체정보": {
      "몸무게": 71.2,
      "키": 175.4
   },
   "이름": "홍길동",
   "취미": [
      "등산",
      "자전거타기",
      "독서"
   ]
}
'''
type(json_data)
'''
str
'''

## 2. JSON => 파이썬 데이터 형식 : json.loads()
json_dict = json.loads(json_data)
'''
{'거주지': '서울',
 '나이': 25,
 '신체정보': {'몸무게': 71.2, '키': 175.4},
 '이름': '홍길동',
 '취미': ['등산', '자전거타기', '독서']}
'''

type(json_dict)
'''
dict
'''

## 3. 파이썬 데이터 형식으로 변환된 JSON 데이터 다루기 : 즉 dict 자료 다루기
# dict 자료는 key 를 이용하여 해당 데이터 추출 가능
# 예) dict객체[key] 
json_dict['거주지']
'''
'서울'
'''

# key의 데이터가 dict일 경우
# dict객체[key][key] 
# 두번째 [key] 는 첫 번째 [key]의 value의 key
# '신체정보': {'몸무게': 71.2, '키': 175.4} 
json_dict['신체정보']
'''
{'몸무게': 71.2, '키': 175.4}
'''

json_dict['신체정보']['몸무게']
'''
71.2
'''

# key의 데이터가 list일 경우
# dict객체[key][index] 
# [index] 는 [key]의 value에 해당하는 list의 index번호
# '취미': ['등산', '자전거타기', '독서']
json_dict['취미']
'''
['등산', '자전거타기', '독서']
'''

json_dict['취미'][1]
'''
'자전거타기'
'''






#### XML 형식의 데이터 처리
"""
XML 규칙 : 첫 번재 줄은 xml 선언부가 존재 <== <?xml version="1.0" encoding="utf-8" ?>
1. 전체를 감싸는 태그는 1개만 존재해야 한다. : 이를 root element (또는 root node) 라고 부른다
   <root>
   <root>
   <first>       <== 오류 전체를 감싸는 루트 엘리먼트는 1개만 존재해야 하기 매문에...
   </first>

2. 시작태그와 닫는태그가 한 쌍을 이루어야 한다. : 이를 element(또는 node) 라고 부른다
   <시작>데이터</시작>
   
3. html 과 달리 정의된 태그명이 없기 때문에 사용자가 정의하여 사용한다.
   단, 시작태그와 닫는 태그에 대한 대소문자를 구분한다
   <Start>데이터</start>  <== 와 같이 사용하면 오류
   
4. 여러 개의 태그를 사용할 수 있지만, 시작태그와 닫는태그가 중첩되면 안된다.
   <root>
      <test>데이터</test>
      <first>
          <second>
             데이터 
          </first>        <== 오류 : </second> 가 먼저 닫혀야 하기 때문에..
      </second>    
   </root>

5. 태그 내에 속성을 지정할 수 있다.
   <test num=""> 와 같이 사용자가 속성을 설정하여 사용할 수 있다..
   <test num=""  param="" >
"""


## 1. xml 을 파이썬 형식으로 변환 : xmltodict 모듈을 사용
# 모듈 import
import xmltodict

# 테스트용 데이터 
xml_data = """<?xml version="1.0" encoding="UTF-8" ?>
<사용자정보>
    <이름>홍길동</이름>
    <나이>25</나이>
    <거주지>서울</거주지>
    <신체정보>
        <키 unit="cm">175.4</키>
        <몸무게 unit="kg">71.2</몸무게>
    </신체정보>
    <취미>등산</취미>
    <취미>자전거타기</취미>
    <취미>독서</취미>
</사용자정보> 
"""

# xml => 파이썬 dict : xmltodict.parse()
dict_data = xmltodict.parse(xml_data)
'''
OrderedDict([('사용자정보',
              OrderedDict([('이름', '홍길동'),
                           ('나이', '25'),
                           ('거주지', '서울'),
                           ('신체정보',
                            OrderedDict([('키',
                                          OrderedDict([('@unit', 'cm'),
                                                       ('#text', '175.4')])),
                                         ('몸무게',
                                          OrderedDict([('@unit', 'kg'),
                                                       ('#text', '71.2')]))])),
                           ('취미', ['등산', '자전거타기', '독서'])]))])

@unit 과 같이 @로 표현된 것은 태그의 속성명을 의미
#text 와 같이 #으로 표현된 것은 시작태그와 닫는태그 사이의 텍스트를 의미

<취미>등산</취미>
<취미>자전거타기</취미>
<취미>독서</취미>
와 같이 동일한 위치에 동일한 태그로 구성되어 있으면
동일한 태그명은 1개만 그리고 동일한 태그들의 값(데이터)들은 리스트로 변환
 ==> ('취미', ['등산', '자전거타기', '독서'])
 
태그명과 값은 튜플로 변환
 ==> ('이름', '홍길동')
 
루트엘리먼트 내부의 직계 태그들은 리스트로 변환
 => [('이름', '홍길동'), ~~~~ ('취미', ['등산', '자전거타기', '독서'])]
'''

type(dict_data)
'''
collections.OrderedDict
'''

dict_data['사용자정보']
'''
OrderedDict([('이름', '홍길동'),
             ('나이', '25'),
             ('거주지', '서울'),
             ('신체정보',
              OrderedDict([('키',
                            OrderedDict([('@unit', 'cm'),
                                         ('#text', '175.4')])),
                           ('몸무게',
                            OrderedDict([('@unit', 'kg'),
                                         ('#text', '71.2')]))])),
             ('취미', ['등산', '자전거타기', '독서'])])
'''

dict_data['사용자정보']['이름']
'''
'홍길동'
'''

dict_data['사용자정보']['신체정보']
'''
OrderedDict([('키', OrderedDict([('@unit', 'cm'), ('#text', '175.4')])),
             ('몸무게', OrderedDict([('@unit', 'kg'), ('#text', '71.2')]))])
'''

dict_data['사용자정보']['신체정보']['키']
'''
 OrderedDict([('@unit', 'cm'), ('#text', '175.4')])
'''

dict_data['사용자정보']['신체정보']['키']['@unit']
'''
'cm'
'''

dict_data['사용자정보']['신체정보']['키']['#text']
'''
'175.4'
'''

dict_data['사용자정보']['취미']
'''
['등산', '자전거타기', '독서']
'''

dict_data['사용자정보']['취미'][1]
'''
'자전거타기'
'''

# xml => 파이썬 dict : xmltodict.parse() : 태그의 속성을 무시하고 일반형태의 dict으로 변환
dict_data = xmltodict.parse(xml_data, xml_attribs=False)
'''
OrderedDict([('사용자정보',
              OrderedDict([('이름', '홍길동'),
                           ('나이', '25'),
                           ('거주지', '서울'),
                           ('신체정보',
                            OrderedDict([('키', '175.4'), ('몸무게', '71.2')])),
                           ('취미', ['등산', '자전거타기', '독서'])]))])
'''

type(dict_data)
'''
collections.OrderedDict
'''




### 웹 사이트 주소에 부가 정보 추가하기
"""
웹 API를 통해 데이터를 요청할 경우,
1. 대표 URL에
2. 인증키 
3. 파라미터 
들을 추가적으로 전달..
특히 응답받을 데이터의 형식(JSON, XML)을 전달

요청 시, requests 모듈을 사용
"""
# 모듈 impport
import requests

#### 웹 사이트 주소에 경로 추가하기
## 대표 URL과 하나의 서브 URL 일 경우
# 대표 URL
base_url = 'https://api.github.com/'

# 서브 URL
sub_url ="events"

# 전체 URL : 요청전 반드시 확인이 필요!!!!
url = base_url + sub_url
'''
'https://api.github.com/events'
'''

## 대표 URL과 여러 개의 서브 URL 일 경우 : 서브 URL들은 리스트로 작성
# 대표 URL
base_url = 'https://api.github.com/'

# 서브 URL들
sub_url =["events", "user", "emails"]

for sub in sub_url:
    url = base_url + sub
    r = requests.get(url)     # r 은 응답(response) 객체
    print(r.url)
'''
https://api.github.com/events
https://api.github.com/user
https://api.github.com/emails
'''


#### 웹 사이트 주소에 매개변수 추가하기
# 날씨 데이터를 제공하는 웹 사이트에 파라미터(매개변수) 추가
# 날씨 데이터 요청 시, 위도 경도가 필요

LAT = '37.57'    # 위도 : 실제 전달받은 데이터들은 주로 lat 라는 키값으로 전달됨
LON = '126.98'   # 경도 : 실제 전달받은 데이터들은 주로 lng 라는 키값으로 전달됨

# 임의의 API Key 값
API_KEY = 'b235c57pc357fb68acr1e81'
UNIT = 'metric' # 단위

# 날씨 데이터 제공 사이트 URL
site_url = "http://api.openweathermap.org/data/2.5/weather"
"""
만약 요청에 필요한 파라미터(매개변수) 없이 요청할 경우
{"cod":401, "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."}
와 같은 메시지를 출력(응답)
"""

# 파라미터(매개변수) 설정 첫 번째 방법 
parameter = '?lat=%s&lon=%s&apiid=%s&units=%s'%(LAT, LON, API_KEY, UNIT)

# 최종 요청 URL
url_para = site_url + parameter
'''
'http://api.openweathermap.org/data/2.5/weather?lat=37.57&lon=126.98&appid=b235c57pc357fb68acr1e81&units=metric'
'''

r = requests.get(url_para)
print(r.url)
'''
http://api.openweathermap.org/data/2.5/weather?lat=37.57&lon=126.98&apiid=b235c57pc357fb68acr1e81&units=metric
'''


## 파라미터(매개변수) 설정 두 번째 방법 : dict 형태
LAT = '37.57'    # 위도 : 실제 전달받은 데이터들은 주로 lat 라는 키값으로 전달됨
LON = '126.98'   # 경도 : 실제 전달받은 데이터들은 주로 lng 라는 키값으로 전달됨

# 임의의 API Key 값
API_KEY = 'b235c57pc357fb68acr1e81'
UNIT = 'metric' # 단위

# 날씨 데이터 제공 사이트 URL
site_url = "http://api.openweathermap.org/data/2.5/weather"

##### dict 형태로 파라미터 설정
parameter = {'lat':LAT, 'lon':LON, 'appid':API_KEY, 'units':UNIT }

r = requests.get(site_url, params=parameter)
print(r.url)
'''
http://api.openweathermap.org/data/2.5/weather?lat=37.57&lon=126.98&appid=b235c57pc357fb68acr1e81&units=metric

오류 처리 응답 : 임의의 API key로 요청했기 때문에...
{"cod":401, "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."}
'''

"""
실제 제공 사이트
https://openweathermap.org/
"""

#### 웹 사이트 주소의 인코딩과 디코딩
import requests

# Encoding Key
API_KEY = '7c7xPvvWFjpWiGa3guoOWh3%2Fz5w%2FrkHX51Q5DpRhYkw%2B4GlGbnM%2F1TyS%2F6sNsP1nhivOhZeoRPQGEXNCiJNt5g%3D%3D'

# Encoding Key ==>  Decoding Key : requests.utils.unquote()
DECODE_KEY = requests.utils.unquote(API_KEY)
'''
'7c7xPvvWFjpWiGa3guoOWh3/z5w/rkHX51Q5DpRhYkw+4GlGbnM/1TyS/6sNsP1nhivOhZeoRPQGEXNCiJNt5g=='
'''


# 실제 사이트 URL : airkorea.or.kr
# API 서비스를 제공하는 URL 
req_url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList"


tm_X = 244148.546388
tm_Y = 412423.75772

API_KEY = "et5piq3pfpqLEWPpCbvtSQ%2Bertertg%2Bx3evdvbaRBvhWEerg3efac2r3f3RfhDTERTw%2B9rkvoewRV%2Fovmrk3dq%3D%3D"
API_KEY_decode = requests.utils.unquote(API_KEY)

req_parameter ={"ServiceKey":API_KEY_decode, 'tmX':tm_X, 'tmY':tm_Y }

r_DECODE = requests.get(req_url, params=req_parameter)
print(r_DECODE.url)


## 15.2 API 키를 사용하지 않고 데이터 가져오기
### 국제 우주 정거장의 정보 가져오기 : http://open-notify.org/
"""
 요청 URL (Open API URL) : http://api.open-notify.org/iss-now.json
 국제 우주 정거장의 현재 위치, 지나간 시간, 우주인 인원수와 이름을 제공.
"""
url = 'http://api.open-notify.org/iss-now.json'

r = requests.get(url)   
# r은 response 객체, 따라서 응답받은 데이터 추출시 response.text 를 이용하여 추출 가능

print(r.text)
'''
{"message": "success", "iss_position": {"longitude": "36.0473", "latitude": "32.1997"}, "timestamp": 1639544971}
{"message": "success", "iss_position": {"longitude": "38.9338", "latitude": "34.5389"}, "timestamp": 1639545025}
'''

type(r.text)
'''
str
'''

# 응답받은 JSON을 파이썬 dict로 변환
json_to_dict = json.loads(r.text)
'''
{'message': 'success',
 'iss_position': {'longitude': '38.9338', 'latitude': '34.5389'},
 'timestamp': 1639545025}
'''

type(json_to_dict)
'''
dict
'''

# 두 번째 방법 : 응답 데이터가 JSON 형태이기 때문에. 바로 변환도 가능
# 즉, json_to_dict = json.loads(r.text) 을 간단하게 표현 가능
url = 'http://api.open-notify.org/iss-now.json'

r = requests.get(url)   

json_to_dict = r.json()
'''
{'message': 'success',
 'iss_position': {'longitude': '67.9508', 'latitude': '48.5662'},
 'timestamp': 1639545438}
'''

type(json_to_dict)
'''
dict
'''

# 세 번째 방법 : 굳이 response 객체를 변수에 저장할 필요없이 응답 결과를 바로 변환
url = 'http://api.open-notify.org/iss-now.json'
json_to_dict = requests.get(url).json()
'''
{'message': 'success',
 'iss_position': {'longitude': '81.8011', 'latitude': '51.0335'},
 'timestamp': 1639545587}
'''

type(json_to_dict)
'''
dict
'''

## 변환된 파이썬 dict 로부터 각 데이터 추출
print(json_to_dict['iss_position'])
print(json_to_dict['iss_position']['longitude'])
print(json_to_dict['iss_position']['latitude'])
print(json_to_dict['timestamp'])
'''
{'longitude': '93.8091', 'latitude': '51.6199'}
93.8091
51.6199
1639545708
'''

## 국제 정거장 데이터를 1초에 한 번씩 요청하여 출력하는 사용자 정의 함수
# 1초에 한 번씩 요청 : time 모듈의 sleep(초단위) 을 사용
# 모둘 import
import time

url = 'http://api.open-notify.org/iss-now.json'

def ISS_Position(iss_position_url):
    json_to_dict = requests.get(iss_position_url).json()
    return json_to_dict['iss_position']

for k in range(5):
    print(ISS_Position(url))
    time.sleep(1)
'''
{'longitude': '136.9352', 'latitude': '41.2348'}
{'longitude': '137.0353', 'latitude': '41.1800'}
{'longitude': '137.1353', 'latitude': '41.1250'}
{'longitude': '137.2018', 'latitude': '41.0883'}
{'longitude': '137.3015', 'latitude': '41.0332'}
'''

### 국가 정보 가져오기 : https://restcountries.eu
## 요청 UL : https://restcountries.eu/rest/v1/name/
"""
나라이름, 도시이름, 통화등 국가 관련 정보를 제공 (JSON)
"""
url_tmp ='https://restcountries.eu/rest/v1/name/'
country = 'South Korea'

req_url = url_tmp + country
'''
'https://restcountries.eu/rest/v1/name/South Korea'
'''

r = requests.get(req_url)
'''
ConnectionError: HTTPSConnectionPool(host='restcountries.eu', port=443): Max retries exceeded with url: /rest/v1/name/South%20Korea
Max retries exceeded with url : 최대 접속(재시도) 횟수가 초과됨!!!

Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000021EE7A91280>: Failed to establish a new connection: [WinError 10060] 연결된 구성원으로부터 응답이 없어 연결하지 못했거나, 호스트로부터 응답이 없어 연결이 끊어졌습니다')
1. 인증키가 있을 경우 : 인증키에 대한 활성화가 안되어 있거나, 
                        인증키가 잘못되었거나,
                        인증키를 디코딩하지 않았을 경우
                        
2. 인증키가 올바르고. 인증키 요청이 없을 경우
   해당 사이트의 트래픽 초과 / 허용된 트래픽 이상을 요청하였을 경우                        
   해당 사이트 재점검 / 요청하는 운영체제에서 특정 port에 대한 방화벽이 설정되어 있을 경우
   백신 프로그램 또는 웹 브라우저 설정에서 유해사이트를 막는 설정이 되어 있을 경우..
   
'''
print(r.text)




## 15.4 정부의 공공 데이터 가져오기 : https://www.data.go.kr
### 회원 가입 및 서비스 신청
# 1. https://www.data.go.kr 접속
# 2. 회원가입 : 신청한 메일로 전달된 인증 코드를 입력해야 함!!
# 3. API Key 생성
# 3-1. 로그인
# 3-2. 데이터목록 선택
#      데이터 찾기 => 데이터 목록 => 검색창(도로명주소조회) => 
#      오픈 API => 과학기술정보통신부 우정사업본부_도로명주소조회서비스 => 활용신청
#      =>  활용목적 선택 => 앱개발 (모바일,솔루션등) => 테스트 입력
#      인증까지 1~2시간 정도 소요 (경우에 따라서는 24시간이상 소요)
import requests

## 주소 및 우편번호 가져오기 : 응답 데이터 형식은 XML
# Encoding key
API_KEY = 'YOUR-API-KEY'

# Encoding key => Decoding Key
API_KEY_decode = requests.utils.unquote(API_KEY)

# 서비스 요청 URL
req_url = "http://openapi.epost.go.kr/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd"

# 검색 기준
search_Se = 'road'

# 검색 주소
srch_wrd = '반포대로 201'

# 파라미터 설정 : 해당 사이트에서 제공하는 문서 내의 항목명이 파라미터명
req_parameter = {'ServiceKey':API_KEY_decode, 'searchSe':search_Se, 'srchwrd':srch_wrd}

# 서비스 요청
r = requests.get(req_url, params=req_parameter)

# 응답(response)로부터 xml데이터 추출 : response.text
xml_data = r.text
'''
'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><NewAddressListResponse><cmmMsgHeader><requestMsgId></requestMsgId><responseMsgId></responseMsgId><responseTime>20211215:151014837</responseTime><successYN>Y</successYN><returnCode>00</returnCode><errMsg></errMsg><totalCount>1</totalCount><countPerPage>10</countPerPage><totalPage>1</totalPage><currentPage></currentPage></cmmMsgHeader><newAddressListAreaCd><zipNo>06579</zipNo><lnmAdres>서울특별시 서초구 반포대로 201 (반포동, 국립중앙도서관)</lnmAdres><rnAdres>서울특별시 서초구 반포동 산60-1 국립중앙도서관</rnAdres></newAddressListAreaCd></NewAddressListResponse>'
'''

'''
인증이 안되었을 경우
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<NewAddressListResponse>
    <cmmMsgHeader>
        <requestMsgId></requestMsgId>
        <responseMsgId></responseMsgId>
        <responseTime>20211214:171702233</responseTime>
        <successYN>N</successYN>
        <returnCode>30</returnCode>
        <errMsg>SERVICE KEY IS NOT REGISTERED ERROR.</errMsg>
    </cmmMsgHeader>
</NewAddressListResponse>
'''

## xml 데이터 => 파이썬 dict :  xmltodict 모듈의 parse()를 이용
# 모듈 import
import xmltodict

dict_data = xmltodict.parse(xml_data)
'''
OrderedDict([('NewAddressListResponse',
              OrderedDict([('cmmMsgHeader',
                            OrderedDict([('requestMsgId', None),
                                         ('responseMsgId', None),
                                         ('responseTime',
                                          '20211215:151014837'),
                                         ('successYN', 'Y'),
                                         ('returnCode', '00'),
                                         ('errMsg', None),
                                         ('totalCount', '1'),
                                         ('countPerPage', '10'),
                                         ('totalPage', '1'),
                                         ('currentPage', None)])),
                           ('newAddressListAreaCd',
                            OrderedDict([('zipNo', '06579'),
                                         ('lnmAdres',
                                          '서울특별시 서초구 반포대로 201 (반포동, 국립중앙도서관)'),
                                         ('rnAdres',
                                          '서울특별시 서초구 반포동 산60-1 국립중앙도서관')]))]))])
'''

type(dict_data)
'''
collections.OrderedDict
'''

print(dict_data['NewAddressListResponse'])
'''
OrderedDict([('cmmMsgHeader', OrderedDict([('requestMsgId', None), ('responseMsgId', None), ('responseTime', '20211215:151014837'), ('successYN', 'Y'), ('returnCode', '00'), ('errMsg', None), ('totalCount', '1'), ('countPerPage', '10'), ('totalPage', '1'), ('currentPage', None)])), ('newAddressListAreaCd', OrderedDict([('zipNo', '06579'), ('lnmAdres', '서울특별시 서초구 반포대로 201 (반포동, 국립중앙도서관)'), ('rnAdres', '서울특별시 서초구 반포동 산60-1 국립중앙도서관')]))])
'''

print(dict_data['NewAddressListResponse']['newAddressListAreaCd'])
'''
OrderedDict([('zipNo', '06579'), ('lnmAdres', '서울특별시 서초구 반포대로 201 (반포동, 국립중앙도서관)'), ('rnAdres', '서울특별시 서초구 반포동 산60-1 국립중앙도서관')])
'''

address_list = dict_data['NewAddressListResponse']['newAddressListAreaCd']
print("우편번호 : ", address_list['zipNo'])
print("도로 주소 : ", address_list['lnmAdres'])
print("지번 주소 : ", address_list['rnAdres'])
'''
우편번호 :  06579
도로 주소 :  서울특별시 서초구 반포대로 201 (반포동, 국립중앙도서관)
지번 주소 :  서울특별시 서초구 반포동 산60-1 국립중앙도서관
'''







