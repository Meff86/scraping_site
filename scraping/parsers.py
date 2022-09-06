import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('hh', 'habr')

headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
           {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}]




def hh(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            new_jobs = soup.find('div', attrs={'class': 'no-content__title'})
            if not new_jobs:
                main_div = soup.find('div', id='a11y-main-content')
                if main_div:
                    div_lst = main_div.find_all('div', attrs={'class': 'serp-item'})
                    for div in div_lst:
                        title = div.find('h3')
                        href = title.a['href']
                        content = div.find('div', attrs={'class': 'g-user-content'})
                        company = div.find(attrs={'class': 'bloko-text'})
                        jobs.append({'title': title.text, 'url': href, 'description': content.text, 'company': company.text,
                                     'city_id': city, 'language_id': language})
                else:
                    errors.append({'url': url, 'title': "Div does not exist"})
            else:
                errors.append({'url': url, 'title': 'Page is empty'})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors

def habr(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://career.habr.com'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            new_jobs = soup.find('div', attrs={'class': 'no-content__title'})
            if not new_jobs:
                main_div = soup.find('div', attrs={'class': 'section-group--gap-medium'})
                if main_div:
                    div_lst = main_div.find_all('div', attrs={'class': 'vacancy-card'})
                    for div in div_lst:
                        title = div.find('div', attrs={'class': 'vacancy-card__title'})
                        href = title.a['href']
                        content = div.find('div', attrs={'class': 'vacancy-card__skills'})
                        company = div.find(attrs={'class': 'vacancy-card__company-title'})

                        jobs.append({'title': title.text, 'url': domain + href, 'description': content.text, 'company': company.text,
                                     'city_id': city, 'language_id': language})
                else:
                    errors.append({'url': url, 'title': "Div does not exist"})
            else:
                errors.append({'url': url, 'title': 'Page is empty'})
        else:
            errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors

#if __name__ == '__main__':
#    url = 'https://career.habr.com/vacancies?city_id=678&q=python&type=all'
#   jobs, errors = habr(url)
#    h = codecs.open('work.txt', 'w', 'utf-8')
#   h.write(str(jobs))
#   h.close()