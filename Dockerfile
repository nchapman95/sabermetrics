FROM python:3.6-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
EXPOSE 80
ENTRYPOINT ["python3"]
CMD [ "/app/app.py" ]
