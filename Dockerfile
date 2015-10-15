#Using the BASE centos 7 images
#
# Build command sudo docker build -t mattiashem/theguide --no-cache . use --no-cache to make it clean
# Run Dev sudo docker  run -i -p 8080:8080 9e10ea801cf8  python /var/www/asylguiden/manage.py runserver 0.0.0.0:8080
# Run Prod docker run -d -p 8000:8000 VERSION cd /var/www/asylguiden & gunicorn --log-file=- asylgudien.wsgi:application


FROM centos:centos7

# File Author / Maintainer
MAINTAINER Mattias Hemmingsson

EXPOSE 8000:8000
EXPOSE 8080:8080


#Installing git
RUN yum install git -y
RUN yum install gcc -y
RUN yum install python-devel -y


#Setting up pip
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

ENV PYTHONUNBUFFERED 1

ADD . /code
WORKDIR /code
RUN pip install git+https://github.com/django-nonrel/django
RUN pip install git+https://github.com/django-nonrel/djangotoolbox
RUN pip install git+https://github.com/django-nonrel/mongodb-engine
RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]






#Running app DEV
#RUN python /var/www/asylguiden/manage.py runserver 0.0.0.0:8080

#Running app PROD
#RUN cd /var/www/asylguiden
#RUN gunicorn --log-file=- asylguiden.wsgi:application