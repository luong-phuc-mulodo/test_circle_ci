FROM circleci/python:3.6.4

RUN sudo pip install --upgrade pip
RUN sudo pip install requests
RUN sudo pip install grequests
RUN sudo pip install bs4

ADD ./server.py /tmp/server.py

WORKDIR /test_circle_ci

CMD ["python","/tmp/server.py"]