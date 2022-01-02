#from __future__ import absolute_import
from celery import Celery
import os


# Django의 세팅 모듈을 Celery의 기본으로 사용하도록 등록
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('django-celery-redis')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Seoul')
# 문자열로 등록한 이유는 Celery Worker가 자식 프로세스에게 configuration object를 직렬화하지 않아도 된다는것 때문
# namespace = 'CELERY'는 모든 celery 관련한 configuration key가 'CELERY_' 로 시작해야함을 의미함
app.config_from_object('django.conf:settings', namespace='CELERY')
# Celery Beat Settings
app.conf.beat_schedule = {
    
}
# task 모듈을 모든 등록된 Django App configs에서 load 함
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')