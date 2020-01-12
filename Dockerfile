FROM python:3.6

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


RUN apt-get update \
    && apt-get install -y \
        vim

COPY  ./employees ./employees

WORKDIR ./employees

ENTRYPOINT ["python"]

EXPOSE 5000

#CMD [ "python", "./run.py" ]
#CMD ["run.py"]