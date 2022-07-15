import json
from pprint import pprint


def movie_info(movies, genres):
    
    result = []
    genre_id_name = {}

    for d in genres :
        genre_id_name[d['id']] = d['name']

    for i in range(len(movies)) :
        genre_name = []
        for j in movies[i]['genre_ids'] :
            genre_name.append(genre_id_name[j])
        movies[i]['genre_names'] = genre_name

    for d in movies :
         list = {}
         list['genre_names'] = d['genre_names']
         list['id'] = d['id']
         list['overview'] = d['overview']
         list['title'] = d['title']
         list['vote_average'] = d['vote_average']
         result.append(list)
    return result
      
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))