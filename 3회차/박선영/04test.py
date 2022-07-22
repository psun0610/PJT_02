import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '7b33cbd26f28f787bcab4ff7a7e61743',
        'language': 'ko-KR',
        'query': title
    }
    # title로 검색한 결과 딕셔너리안의 results 리스트를 받아옴
    response = requests.get(URL+path, params=params).json().get('results')

    return response

if __name__ == '__main__':

    pprint(recommendation('검색할 수 없는 영화'))
    # None