FROM python:3.6-alpine

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


ENV PYTHONIOENCODING=UTF-8

COPY  ./employees .

WORKDIR ./

ENTRYPOINT ["python"]

EXPOSE 3700

CMD ["run.py"]