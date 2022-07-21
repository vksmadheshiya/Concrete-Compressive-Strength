# Concrete-Compressive-Strength
Predicting the Concrete Compressive Strength based on keggle data set


Created conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
```
Just to check 
```


## Setting Up Heroku

1. HEROKU_EMAIL = VKSMDAHESHIYA
2. HEROKU_API_KEY = 30e141f6-****-4b1c-b684-b5ff95b243d6
3. HEROKU_APP_NAME = concretes-compressive-strength

<!-- f4eb -->

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name> . 
```



To list images use
```
docker images
```

Run Docker Images
```
docker run -p 5000:5000 -e PORT=5000 <IMAGE ID> (04a03ada5780)
```

To check Running Containers in docker
```
docker ps
```

To stop the docker container
```
docker stop <container_id>
```

