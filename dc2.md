# Use postgres/example user/password credentials
version: '3.9'

services:
  sprint:
    build: ./sprint
    command: bash -c "
      python manage.py makemigrations &&
      python manage.py migrate &&
      python manage.py collectstatic --no-input &&
      DJANGO_SUPERUSER_PASSWORD=111 python manage.py createsuperuser --username=admin --email=admin@example.com --noinput &&
      gunicorn sprint.wsgi:application --bind 0.0.0.0:8000 --reload"
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
    networks:
      - default


  db:
    image: postgres:latest
    restart: always
    # set shared memory limit when using docker-compose
    #shm_size: 128mb
    # or set shared memory limit when deploy via swarm stack
    #volumes:
    #  - type: tmpfs
    #    target: /dev/shm
    #    tmpfs:
    #      size: 134217728 # 128*2^20 bytes = 128Mb
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
        - db:/var/lib/postgresql/data
    ports:
        - "5432:5432"
    networks:
      - default
#  adminer:
#    image: adminer
#    restart: always
#    ports:
#      - 8080:8080

volumes:
    db:
      driver: local

networks:
  default:
    driver: bridge
    driver_opts:
      com.docker.network.driver.mtu: 1450