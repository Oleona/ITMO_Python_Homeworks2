import paired as paired
import requests
import union as union
from bs4 import BeautifulSoup
from numpy.ma import copy


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    r = requests.get("https://news.ycombinator.com/newest")
    soup = BeautifulSoup(r.text, 'html.parser')
    authors = []
    points = []
    comments = []
    urls = []

    table_title = soup.findAll('a', {'class': 'storylink'})
    table_author = soup.findAll('a', {'class': 'hnuser'})
    table_point = soup.findAll('span', attrs={'class': 'score'})
    url = table_title
    for i in range(len(url)):
        ur = url[i].get('href')
        if len(ur) >= 18:
            urls.append(ur)
        else:
            urls.append('no link to source')

    comment = soup.findAll('td', {'class': 'subtext'})
    for i in range(len(comment)):
        com = comment[i].text.split(" | ")[3][0]
        comments.append(com)
    for i in range(len(comments)):
        if comments[i] == 'd':
            comments[i] = int('0')
        else:
            comments[i] = int(comments[i])

    for title in table_title:
        title = (" ".join(title.text.split()))
        news_list.append(title)

    for author in table_author:
        author = (" ".join(author.text.split()))
        authors.append(author)

    for point in table_point:
        point = (" ".join(point.text.split()))
        points.append(int(point[0]))

    titles = news_list

    keys = ['author', 'comments', 'points', 'title', 'url']

    zipped = zip(authors, comments, points, titles, urls)

    news_list = [dict(zip(keys, values)) for values in zipped]

    # PUT YOUR CODE HERE
    return news_list


def extract_next_page(parser):
    next_page = parser.find('a', {'class': 'morelink'}).get('href')
    return next_page
    """ Extract next page URL """
    # PUT YOUR CODE HERE


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

if __name__ == '__main__':
    news = get_news("https://news.ycombinator.com/newest", n_pages=5)
    print(news)