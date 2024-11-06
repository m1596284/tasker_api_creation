FROM python:3.11-alpine
WORKDIR /tasker_api_creation
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "src/api_creation.py"]