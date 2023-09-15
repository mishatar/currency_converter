FROM python:3 
RUN chmod 755 .
WORKDIR /code 
COPY requirements.txt /code/ 
RUN pip install -r requirements.txt 
COPY . /code/ 
