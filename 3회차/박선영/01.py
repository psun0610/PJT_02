# 01. 인기 영화 조회

# 인기 영화 목록의 개수를 출력함
# requests 라이브러리를 활용하여 TMDB에서 "현재 인기 있는 영화 목록(Get Populations)" 데이터를 요청함
# 응답 받은 데이터 영화 개수를 반환하는 함수 작성

import requests
from pprint import pprint

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '7b33cbd26f28f787bcab4ff7a7e61743',
        'language': 'ko-KR'
    }
    response = requests.get(URL+path, params=params).json()

    # response는 딕셔너리 => get으로 results값 가져옴
    # results는 리스트 => len으로 results 리스트의 크기 구함
    count = len(response.get('results'))
    return count

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
