import requests


def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '218b6969ebdb7001ad12959f10fbfb7b'}

    response = requests.get(base_url + path, params = params).json()
    return len(response.get('results'))
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
