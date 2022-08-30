from af_metrics import CustomCollector
import time
from prometheus_client.core import REGISTRY
from prometheus_client import start_http_server

if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        time.sleep(1)