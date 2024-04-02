FROM python:3.10

WORKDIR /DA-python-P9-1

COPY requirements.txt /DA-python-P9-1/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /DA-python-P9-1/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]