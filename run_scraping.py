import codecs
import os, sys

from django.contrib.auth import get_user_model
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()


from scraping.models import City, Vacancy, Language, Error, Url

from scraping.parsers import *

User = get_user_model()

parsers = ((hh, 'https://hh.ru/search/vacancy?area=1&search_field=name&text=python&no_magic=true&L_save_area=true&items_on_page=50' ),
           (habr, 'https://career.habr.com/vacancies?city_id=678&q=python&type=all'))

def get_settings():
    qs =User.objects.filter(send_email=True).values()
    settings_lst = set((q['city_id'], q['language_id']) for q in qs)
    return settings_lst

def get_urls(_settings):
    qs = Url.objects.all().values()
    url_dct = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
    urls = []
    for pair in _settings:
        tmp = {}
        tmp['city'] = pair[0]
        tmp['language'] = pair[1]
        tmp['url_data'] = url_dct[pair]
        urls.append(tmp)
    return urls

city = City.objects.filter(slug='moskva').first()
language = Language.objects.filter(slug='python').first()

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass
if errors:
    er = Error(data=errors).save()






#h = codecs.open('work.txt', 'w', 'utf-8')
#h.write(str(jobs))
#h.close()
