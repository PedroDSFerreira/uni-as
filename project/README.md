# TrotiNet
This project implements scooter rental and booking service. 
## Get Started
### Requirements
- Docker
- Docker-compose

### Installation
- Clone repository and cd into `trotinet-app/`
- To run docker containers, run:

    ```bash
    docker compose up --build
    ```
    - Flask application will be available at http://localhost:5001
    - Prometheus metrics will be available at https://localhost:9090
        - Metrics:
            - Kafka service status 
            - Scooter status and metrics
### Testing
After running docker containers, you can test the application by importing `trotinet-app/TrotiNET.side` into Selenium IDE. There you will find all the scenarios of the user stories.
