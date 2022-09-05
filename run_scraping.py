import codecs
import os, sys

from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()


from scraping.models import City, Vacancy, Language

from scraping.parsers import *

parsers = ((hh, 'https://hh.ru/search/vacancy?area=1&search_field=name&text=python&no_magic=true&L_save_area=true&items_on_page=50' ),
           (habr, 'https://career.habr.com/vacancies?city_id=678&q=python&type=all'))

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






#h = codecs.open('work.txt', 'w', 'utf-8')
#h.write(str(jobs))
#h.close()
