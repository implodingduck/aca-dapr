FROM python:3.12

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y curl tcpdump net-tools vim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]