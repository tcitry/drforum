FROM python:3.6

ENV WORK /workspace
WORKDIR $WORK
COPY . $WORK
COPY .env.example .env

RUN pip install -r requirements.txt
CMD python manage.py runserver