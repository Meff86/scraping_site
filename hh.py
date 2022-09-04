import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }

url = 'https://hh.ru/search/vacancy?area=1&search_field=name&text=python&no_magic=true&L_save_area=true&items_on_page=50'

def hh(url):
    jobs = []
    errors = []
    resp = requests.get(url, headers=headers)
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
                    company = div.find(attrs={'class': 'bloko-link_kind-tertiary'})
                    jobs.append({'title': title.text, 'url': href, 'description': content.text, 'company': company.text})
            else:
                errors.append({'url': url, 'title': "Div does not exist"})
        else:
            errors.append({'url': url, 'title': 'Page is empty'})
    else:
        errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors

def habr(url):
    jobs = []
    errors = []
    resp = requests.get(url, headers=headers)
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

                    jobs.append({'title': title.text, 'url': href, 'description': content.text, 'company': company.text})
            else:
                errors.append({'url': url, 'title': "Div does not exist"})
        else:
            errors.append({'url': url, 'title': 'Page is empty'})
    else:
        errors.append({'url': url, 'title': "Page do not response"})

    return jobs, errors

if __name__ == '__main__':
    url = 'https://career.habr.com/vacancies?city_id=678&q=python&type=all'
    jobs, errors = habr(url)
    h = codecs.open('next.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()