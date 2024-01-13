import paramiko
import json
import psutil
import time
from Src.Stats import fetch_server_stats

def run_fetch():
    with open('config.json') as config_file:
        config = json.load(config_file)

    stats_list = []
    for node in config['nodes']:
        stats_list.append(fetch_server_stats(node))

    return stats_list

if __name__ == "__main__":
    while True:
        stats = run_fetch()
        print(stats)
        time.sleep(2)
