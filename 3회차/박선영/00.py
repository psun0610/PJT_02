# 00. API 문서와 requests 활용 (연습)

# 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
# (https://apidocs.bithumb.com/reference/%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C

import requests

# URL로
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

# 요청을 보내서
# 응답 받은 값을 가져온다!
response = requests.get(URL)

data = response.json()
# data는 딕셔너리임 => Key로 접근하기!
print(data.get('data').get('closing_price'))