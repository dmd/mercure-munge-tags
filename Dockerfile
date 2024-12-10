FROM python:3.12
ADD docker-entrypoint.sh ./
ADD munge.py ./
ADD requirements.txt ./
RUN chmod 777 ./docker-entrypoint.sh
RUN pip install -r requirements.txt

CMD ["./docker-entrypoint.sh"]
