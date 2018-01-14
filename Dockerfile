FROM python:latest

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

ENV PORT=5000
EXPOSE 5000

WORKDIR /usr/src
COPY ./ ./

CMD ["python", "flask-app-1.py"]