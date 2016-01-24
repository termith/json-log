import random
import uuid
import time

levels = ['ERROR', 'DEBUG', 'INFO']
while True:
    time.sleep(5)
    with open('json.log', 'a+') as log:
        entry = """{"@fields": {"uuid": "%s", "level": "%s", "status_code": 200, "content_type": "application/json", "path": "/v1/items/1/", "method": "PUT", "name": "django.http"}, "@timestamp": "2015-12-15T05:45:39+00:00", "@source_host": "c57872949172", "@message": "Request processed"}\n""" % (str(uuid.uuid4()), random.choice(levels))
        log.write(entry)