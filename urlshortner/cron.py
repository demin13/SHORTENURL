from datetime import date

from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings


scheduler = BackgroundScheduler()

def my_cron_job():
    from .models import URLStore
    print("performing at the interval of 2 min")
    current_date = date.today()
    expired_urls = URLStore.objects.filter(expiryAt__lt=current_date)
    expired_urls.delete()

def start():
    scheduler.add_job(my_cron_job, 'cron', hour=0, minute=0)
    scheduler.start()


if not settings.DEBUG:
    start()