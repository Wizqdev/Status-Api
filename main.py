from flask import Flask
from Src.Routes.Post import post_stats
from Src.Routes.Get import get_stats
import json

app = Flask(__name__)

# Load configuration from file
with open('config.json') as config_file:
    config = json.load(config_file)

# Get the web port from the config
web_port = config.get('web', {}).get('port')

@app.route('/api/post/stats', methods=['POST'])
def post_stats_route():
    return post_stats()

@app.route('/api/get/stats', methods=['GET'])
def get_stats_route():
    return get_stats()

if __name__ == "__main__":
    app.run(port=web_port)
