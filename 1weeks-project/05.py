import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.  
    result = {}
    genre_id_name = {}

    for i in genres :
        genre_id_name[i['id']] = i['name']

    genre_name = []
    for id in movie['genre_ids']:
        genre_name.append(genre_id_name[id])
    movie['genre_names'] = genre_name

    result['genre_names'] = movie['genre_names']
    result['id'] = movie['id']
    result['overview'] = movie['overview']
    result['title'] = movie['title']
    result['vote_average'] = movie['vote_average']

    return result
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))