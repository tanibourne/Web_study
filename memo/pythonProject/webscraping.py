import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
# select는 배열을 반환!!
soup = BeautifulSoup(data.text, 'html.parser')
song_info = soup.select('table.list-wrap > tbody > tr > td.info')
# print(song_info)

rank = 1
for song in song_info:
    title_el = song.select('a')
    # artist_el = song.select('a.artist ellipsis')
    if len(title_el) > 0:
        title = title_el[0].text.lstrip()
        artist = title_el[1].text
        print(rank, title, artist)
        rank += 1
        print('&&&' * 40)




#
# movie_info = soup.select('table.list_ranking > tbody > tr')
#
# rank  = 1
# for movie in movie_info:
#
#     title_el = movie.select('a')
#     point_el = movie.select('td.point')
#     if len(title_el) > 0:
#         title = title_el[0].text
#         point = point_el[0].text
#         print(rank, title, point)
#         rank = rank + 1





