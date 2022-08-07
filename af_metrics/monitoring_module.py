import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
import requests
import json

class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        d1 = {
            "coffea_notebook_metric": [
                {
                "metric": {"bytesread":2076921210},
                "value":0
                },
                {
                "metric": {"entries":53446198},
                "value":0
                },
                {
                "metric":{"processtime":741.4781568050385},
                "value":0
                },
                {
                "metric":{"chunks":267},
                "value":0
                }
            ]
        }
        list_of_metrics = d1["coffea_notebook_metric"]
        for key in list_of_metrics:
           g = GaugeMetricFamily("Coffea_Casa_Metrics", 'Custom_facility_metrics', labels=['coffea_casa_metrics'])
           g.add_metric([str(key['metric'])], key['value'])
           yield g


# if __name__ == '__main__':
#     start_http_server(8003)
#     REGISTRY.register(CustomCollector())
#     while True:
#         time.sleep(1)