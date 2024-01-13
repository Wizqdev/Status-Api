# Status Api 

A Python API that fetches information like RAM, Disk, CPU, etc. from A VPS (Virtual Private Server) or Dedicated Server

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Routes](#routes)
- [License](#license)


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Wizqdev/Status-Page-Api
   cd Status-Page-Api
   ```
2. Installing Dependences
    ```
    pip install requirements.txt
    ```


## Configuration

    ```json
    {

        "web": {
            "port": 3000
        },
            "nodes": [
                {
                "name": "Node 1",
                    "ssh": {
                        "host": "SERVER_IP_ADDRESS",
                        "port": 22,
                        "username": "SERVER_USER_NAME",
                        "password": "SERVER_PASSWORD"
                    }
                },
                {
                "name": "Node 2",
                    "ssh": {
                        "host": "SERVER_IP_ADDRESS",
                        "port": 22,
                        "username": "SERVER_USER_NAME",
                        "password": "SERVER_PASSWORD"
                    }
                },
            ]
    }
    ```
    In SERVER_IP_ADDRESS input your server ip address.
    In SERVER_USER_NAME input username to login to the server.
    In SERVER_PASSWORD input password of the user you provided above.

## Routes

    - **POST /api/post/stats:** Posts the information
    - **GET /api/get/stats:** Gets the information


## License
