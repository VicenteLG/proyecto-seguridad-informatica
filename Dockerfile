FROM mcantillana/django_unab:3

ADD requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code