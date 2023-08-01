# Exploit for Node.js Deserialization Bug for Remote Code Execution (Reverse shell)



This repository contains a Python script that exploits a deserialization vulnerability in Node.js to achieve remote code execution on a server that handles cookies encrypted in insecure base64 format.

## Disclaimer: 
This script is for educational and research purposes only. It should not be used maliciously or without explicit permission from the server owner. Misuse of this script may be illegal and is strictly prohibited.

The scripts and exploits presented in this repository were created and demonstrated solely for educational and research purposes. All testing and demonstrations were performed within a controlled environment with explicit authorization from the system owner.

## Description

Node.js is a JavaScript runtime that uses the Google V8 engine. In certain versions of Node.js, there is a deserialization vulnerability in the "serialize-javascript" library that allows an attacker to manipulate deserialized data on the server and execute remote code in an unauthorized manner.

This Python script utilizes the requests library to make an HTTP POST request to the target server. The script sends a base64-encoded cookie containing manipulated data to exploit the deserialization vulnerability and execute remote code.

## Requeriments 
- Python 3.x installed on the system.
- The requests library installed. You can install it using the following command:
    ```bash
    pip install requests
    ```
## Usage

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Campero727/NodeJsDeserialization.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd NodeJsDeserialization
    ```
3. Execute the script providing the IP of the machine where the reverse shell will be received
    ```bash
    python3 NodeJsDeserialization.py <ip> <port>
    ```
## Warning
- This script is intended for educational and research purposes only. Do not use it on systems without explicit permission from the owner of the target server.
- The inappropriate or unauthorized use of this script may be illegal and is strictly prohibited.
- The author and contributors of this repository assume no responsibility for the misuse of this script.

## Use Example
1. Check that website cookies are base64 encrypted in an insecure way
![Cookies in the website](https://raw.githubusercontent.com/Campero727/NodeJsDeserialization/master/assets/img1.png)
2. In this case we can easily decrypt the cookie and read the data
![data](https://raw.githubusercontent.com/Campero727/NodeJsDeserialization/master/assets/img2.png)
3. If we modify the cookie trying to execute command we will get a node deserialization error
![Deserialization error](https://raw.githubusercontent.com/Campero727/NodeJsDeserialization/master/assets/img3.png)
4. So now we know it's vulnerable, so we'll run the script to get a reverse shell
![error](https://raw.githubusercontent.com/Campero727/NodeJsDeserialization/master/assets/img4.png)
5. We listen in Netcat
![Nc](https://raw.githubusercontent.com/Campero727/NodeJsDeserialization/master/assets/img5.png)
6. We copy the reverse shell generated in the cookie and reload the page
![Cookie for RCE](https://raw.githubusercontent.com/Campero727/NodeJsDeserialization/master/assets/img6.png)
7. We will obtain the reverse shell
![Reverse shell](https://raw.githubusercontent.com/Campero727/NodeJsDeserialization/master/assets/img7.png)
