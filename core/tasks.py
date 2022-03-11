from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import date
import os
import requests


@shared_task(bind=True)
def test_func(self):
    # operations
    print("Task test start!")
    return "Done"


@shared_task(bind=True)
def currency_exchange_rate_func(self):
    
    # 비영업일의 데이터, 혹은 영업당일 11시 이전에 해당일의 데이터를 요청할 경우 null 값이 반환
    
    api_uri = os.environ.get('CURRENCY_OPEN_API_URI')
    authkey = os.environ.get('CURRENCY_OPEN_API_AUTH_KEY')
    searchdate = date.today().strftime('%Y%m%d')
    data = os.environ.get('CURRENCY_OPEN_API_DATA')
    
    requests_url = f'{api_uri}?authkey={authkey}&searchdate={searchdate}&data={data}'
    response = requests.get(requests_url)
    response_json = response.json()
    print(response_json)
    return "Success"