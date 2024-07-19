# Go WebSocket Chatroom with Flask Log Storage

## Overview

This project is a real-time web chat application built with Go and WebSocket for real-time communication and a Flask server for handling log storage. The chat messages are broadcasted to all participants in a room, and logs can be dumped and downloaded.

## Features

- Real-time chat using WebSocket
- Multi-room support
- Nickname assignment for users
- Log dumping and downloading feature
- Responsive and user-friendly UI

## Prerequisites

- Go 1.16+
- Python 3.7+
- Nginx
- Git

## Installation

### Clone the Repository

```sh
git clone https://github.com/YuiNung/goChat.git
cd gochat
```
## Go Setup
- 1.Install Dependencies

    Ensure you have Go installed. Then, run:

```sh
go mod init gochat
go get -u github.com/gorilla/websocket
go get -u github.com/gorilla/mux
```
- 2.Run the Go Application ("Linux's Screen" is recommended)

```sh
go run ./
```
## Python Setup
- 1.Install Dependencies
    Ensure you have Python and pip installed. Then, run:

```sh
pip install flask Flask-Cors
```
- 2.Run the Flask Application ("Linux's Screen" is recommended)

```sh
python getChat.py
```
## Nginx Setup
- 1.Install Nginx

```sh
sudo apt update
sudo apt install nginx
```
- 2.Configure Nginx
    Open the Nginx configuration file:

```sh
sudo vim /etc/nginx/conf.d/app.conf
```
  Add the following configuration:

```nginx
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8080;  # Go application
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /ws/ {
        proxy_pass http://127.0.0.1:8080; # Go WebSocket
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    location /dump {
        proxy_pass http://127.0.0.1:5000;  # Flask application
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /download {
        proxy_pass http://127.0.0.1:5000;  # Flask application
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
- 3.Restart Nginx

```sh
sudo service nginx restart
```
## Usage
- 1. Open your web browser and navigate to http://your_domain_or_ip/roomID.
- 2. If no room ID is specified, you will be redirected to a default room.
- 3. Enter your nickname in the prompt.
- 4. Start chatting!
## Dump and Download Logs
- 1. Click the Dump button in the chat interface.
- 2. The chat logs will be saved and can be downloaded from http://your_domain_or_ip/download.
## Repository Structure
```plaintext
your-repo-name/
├── client.go
├── flask_server.py
├── hub.go
├── main.go
├── home.html
├── README.md
└── chat_log.txt  # Generated after dumping logs
```
## Contributing
Feel free to fork this project, make improvements, and submit pull requests. Any contributions are highly appreciated!

## License
This project is licensed under the BSD 2-Clause License.

## References
