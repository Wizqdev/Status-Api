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
    ```bash
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

    MIT License

    Copyright (c) 2023 Wizq

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.