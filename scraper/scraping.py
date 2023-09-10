import requests
from bs4 import BeautifulSoup

from app.models import Article, Keyword, session


url = 'https://realpython.com'

def get_realpython_response():
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        raise Exception('can not connect to real python')

def get_bs(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    if soup:
        return soup
    else:
        raise Exception('can not create beatifulsoup object')

def get_elements(soup):
    results = soup.find('div', class_="row")
    if results:
        elements = soup.find_all('div', class_=['col-12', 'col-md-6', 'col-lg-4', 'mb-5'])
        if elements:
            return elements
        else:
            raise Exception('Can not get elements')
    else:
        raise Exception('Can not get results')

def get_link(element):
    a = element.find('a')
    if a:
        return url + a.get('href')

def get_title(element):
    title = element.find("h2", class_='card-title')
    if title:
        return title.text

def get_keywords_data(element):
    a = element.find_all('a', class_=['badge', 'badge-light', 'text-muted'])
    keywords = []
    for key in a:
        if key:
            keywords.append(key.text)

    return keywords

def get_data(elements):
    results = []
    for element in elements:
        data = {}
        data['url'] = get_link(element)
        data['title'] = get_title(element)
        data['keywords'] = get_keywords_data(element)
        if data['url'] and data['title']:
            results.append(data)

    return results

def get_realpython_scraping():
    try:
        response = get_realpython_response()
        if response.status_code == 200:
            soup = get_bs(response)
            elements = get_elements(soup)
            data = get_data(elements)
            return data
    except Exception as e:
        raise Exception(f'{e}')

def get_keywords(keywords):
    results = []
    for key in keywords:
        keyword = session.query(Keyword).filter(Keyword.name==key).scalar()
        if not keyword:
            keyword = Keyword(name=key)
            session.add(keyword)
        results.append(keyword)
    return results

def get_article(data):
    article = session.query(Article).filter(Article.url==data['url'], Article.title==data['title']).first()
    if not article:
        article = Article(title=data['title'], url=data['url'], keywords=get_keywords(data['keywords']))
        session.add(article)

def store_data(results):
    for data in results:
        get_article(data)
        session.commit()

def update_data():
    try:
        results = get_realpython_scraping()
        store_data(results)
        return {'message': 'Well Done'}

    except Exception as e:
        return {'message': f'{e}'}