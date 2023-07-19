FROM python:3.10
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY main.py /app/
ENTRYPOINT [ "python" ]
CMD [ "/app/main.py" ]
