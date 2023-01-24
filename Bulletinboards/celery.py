import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bulletinboards.settings')

app = Celery('Bulletinboards')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_news_every_monday_8am': {
        'task': 'news.tasks.task_send_week_news',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}