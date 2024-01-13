from flask import jsonify
import json
from Src.Stats import fetch_server_stats

def get_stats():
    with open('config.json') as config_file:
        config = json.load(config_file)

    stats_list = []
    for node in config['nodes']:
        stats_list.append(fetch_server_stats(node))

    return jsonify(stats_list)
