import requests
import csv
from lxml import html

# 定义常量URL
MOVIE_LIST_FILE = "movie_list.csv"
# 默认只访问第一页
TMDB_BASE_URL = "https://www.themoviedb.org"
# TOP URL 第一页
TMDB_TOP_URL_1 = "https://www.themoviedb.org/tv/top-rated?vote_average.gte=0&vote_average.lte=10"
# TOP URL 后面的页
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/tv/items"  #高分电影榜第二页



# 定义核心逻辑
def get_movie_info(movie_url):
#  1、发送请求
    response = requests.get(movie_url + "?language=zh-TW", timeout = 60)






#  2、解析数据，获取电影详情
    doc = html.fromstring(response.text)
    movie_name = doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")[0]
    movie_year = doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span/text()")[0].strip("(").strip(")")
    # movie_time = doc.xpath("//*[@id='media_v4']/div/div/div[1]/div/section[2]/div[2]/div/div[2]/div/div[3]/span/span/text()")[0].strip().split(",")[1].strip(")")
    movie_tags_lista = doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/a")
    movie_tags = []
    for movie_tag_a in movie_tags_lista:
        movie_tags.append(movie_tag_a.text)
    #     list -> string：用join函数，将list各个元素拼接起来
    movie_tag = "和".join(movie_tags)
    movie_source = doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/div/span/@class")[0][-2:]
    movie_language = doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[5]/text()")[0]
    movie_slogan = doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")[0]
    movie_description = doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")[0]


#  3、return
    return {
        "电影名": movie_name,
        "上映年份": movie_year,
        "类型": movie_tag,
        "评分": movie_source,
        "语言": movie_language,
        "标语": movie_slogan,
        "简介": movie_description
    }


def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["电影名", "上映年份", "类型", "评分", "语言", "标语", "简介"])
        writer.writeheader()
        writer.writerows(all_movies)

def main():
    # 循环的获取电影列表，从p1 -> p5
    all_movies = []
    for page_num in range(1, 6):
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            # 此时，使用POST请求，需要携带参数，发送POST请求数据
            response = requests.post(TMDB_TOP_URL_2,
                                     f"air_date.gte=&air_date.lte=2027-05-02&certification=&certification_country=TW&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=TW%7CXX&release_date.gte=&release_date.lte=&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=200&vote_count.lte=&watch_region=TW&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=flatrate%7Cfree%7Cads%7Crent%7Cbuy&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400&view=&discover_preset=top-rated",
                                     timeout=60)

        #     1、发送请求，获取高分榜单数据
    #       timeout = 60：60s以内拿到结果就OK，否则报错
        response = requests.get(TMDB_TOP_URL_1, timeout = 60)
    #       此时get到的是response对象，response对象中包含服务器返回的所有信息
    #       例如请求头，状态码什么的，需要response.text来get具体源码内容
        print("发送请求获取电影数据……")


    #     2、解析数据，获取电影列表
    #       此时get到html的源码内容，需要使用lxml库中的html模块进行解析
        doc = html.fromstring(response.text)
        movie_list  = doc.xpath("//*[@class='w-full overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-colors hover:border-gray-300']/div/div[2]/div")
        print("解析数据获取电影详情……")

    #     3、遍历电影列表，获取电影详情
    #       获取电影列表

        for movie in movie_list:
            movie_url = movie.xpath("./a/@href")
            # 注：xpath返回值是list，因此要[0]
            if movie_url:
                movie_url = TMDB_BASE_URL + movie_url[0]
                movie_info = get_movie_info(movie_url)
                all_movies.append(movie_info)
        print("获取电影列表……")


#     4、保存CSV
    save_all_movies(all_movies)
    print("保存数据到CSV文件……")

if __name__ == '__main__':
    
    main()