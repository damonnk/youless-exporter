#!/usr/bin/env python

import time 
import os
from prometheus_client import start_http_server, Gauge , REGISTRY , PROCESS_COLLECTOR, PLATFORM_COLLECTOR
import urllib.request, json

youless = os.environ['youless']

REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(REGISTRY._names_to_collectors['python_gc_objects_uncollectable_total'])

current_power_usage = Gauge('youless_current_power_usage', "Current Power Usage in Watts")
total_power_usage = Gauge('youless_total_power_usage', "Total Power Usage in kWh")

def get_metrics():
    with urllib.request.urlopen("http://" + str(youless) + "/a?f=j") as url:
        data = json.load(url)
        print(data)
        current_power_usage.set(data['pwr'])
        total_power_counter = data['cnt']
        total_power_clean = total_power_counter.replace(",", ".")
        total_power_usage.set(total_power_clean)

if __name__ == '__main__':
    start_http_server(9101)
    while True:
        get_metrics()
        time.sleep(10)
