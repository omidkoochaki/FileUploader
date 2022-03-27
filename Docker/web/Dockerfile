FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip;
RUN python -m pip install -r requirements.txt;
RUN #python manage.py makemigrations;
RUN #python manage.py migrate
RUN #pip install -r requirements.txt

COPY . /code/