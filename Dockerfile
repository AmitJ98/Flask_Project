FROM python:3.10.12-slim

WORKDIR /flask_blog_app/

COPY /requirements.txt ./

RUN pip install -r requirements.txt

COPY . /flask_blog_app/
CMD [ "python3","run.py" ]


