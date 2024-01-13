# Status Api 

A Python Api Which Fetchs Information Like **Ram** **Disk** **Cpu** Usages From A Vps(Virtual Private Server) Or Dedicated Servers

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
    In SERVER_IP_ADDRESS Pleaes Add Your Ip Address
    In SERVER_USER_NAME Username Of Vps Its **root** Most Of The Time
    In SERVER_PASSWORD Password Of The Vps/Dedicated Server


## Routes

    - **POST /api/post/stats:** Post's The Information 
    - **GET /api/get/stats:** Get's The Information


## License
