import os
from multiprocessing import cpu_count

# os.environ['DJANGO_SETTINGS_MODULE'] = 'SHORTENURL.settings'
django_settings = "SHORTENURL.settings"
bind = ":8443"
# workers = cpu_count() * 1 + 1
workers = 1
max_requests = 100
timeout = 30
worker_class = "gthread"
#worker_class = "eventlet"  for event driven architecture
threads = 2
accesslog = "Local.log"
# preload=True
certfile = "cert.pem"  # Replace with the path to your SSL certificate file
keyfile = "key.pem"    # Replace with the path to your SSL private key file
