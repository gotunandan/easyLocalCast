easyLocalCast
=============

cast local files easily

Run a http server on port 8080

Install the necessary modules - pip install -r requirements.txt

start the flask server using - python3 serv.py /local/path listenaddr 8888

Alternatively, using Docker
---------------------------

### To Build
docker build -t localCast:test .

### H3 To Run
docker run -d -p 8888:8888 -v /local/path:/datadir localcast:test
