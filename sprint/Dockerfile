FROM python:3.8

# Настроить и активировать виртуальную среду
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Команды Python будут выполнены в виртуальной среде
COPY .. /sprint
RUN pip install --no-cache-dir -r /sprint/requirements.txt

RUN pip install gunicorn
WORKDIR /sprint

ENV DJANGO_SETTINGS_MODULE=sprint.settings
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH /sprint

RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "sprint.wsgi:application", "--bind", "0.0.0.0:8000"]

#EXPOSE 8000