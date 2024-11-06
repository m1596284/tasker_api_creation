# How to run it
### using Python
```
pip install -r requirements.txt
python src/api_creation.py
```
### using Docker
```
docker build --no-cache -t tasker_3 .
docker run -p 5000:5000 tasker_3
docker logs [CONTAINER]
```
go your http://localhost:5000/greet to check the website
# Structure of directory
```
.
├── README.md
├── dockerfile
├── requirements.txt
├── src
│   └── api_creation.py
└── static
    └── tasker_api_creation.gif
```
src: including the main source code of python file.  
static: to save the static file as gif, picture, html and else.  
# Requirements.txt
By using the builtin module in python, requirements is empty for this task.  
# Gif of demonstration
![gif](static/tasker_api_creation.gif)  
# Dockerfile
```
FROM python:3.11-alpine
WORKDIR /tasker_api_creation
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "src/api_creation.py"]
```