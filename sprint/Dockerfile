FROM python:3.8

# Настроить и активировать виртуальную среду
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Команды Python будут выполнены в виртуальной среде
COPY .. /sprint
RUN python sprint.manage.py collectstatic
RUN pip install --no-cache-dir -r /sprint/requirements.txt
RUN pip install gunicorn
WORKDIR /sprint
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
CMD ["gunicorn", "sprint.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000

#FROM python:3.8
#
#WORKDIR /app
#
#COPY sprint/requirements.txt ./
#RUN pip install --upgrade pip
#RUN apt-get update && apt-get install -y \
#    build-essential \
#    gcc \
#    libc6-dev \
#    libffi-dev \
#    libpq-dev \
#    postgresql-client \
#    redis-tools
#RUN pip install psycopg2-binary
#RUN pip install --no-cache-dir -r requirements.txt
#RUN apt-get update && apt-get install -y postgresql-client redis-tools
#
#
##COPY sprint/sprint .
#
#ENV DJANGO_SETTINGS_MODULE=sprint.settings
#ENV PYTHONUNBUFFERED=1
#ENV PYTHONPATH /app
#
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]


