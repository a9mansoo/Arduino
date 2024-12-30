FROM python:3.10-slim

WORKDIR /app

COPY monitors/ /app/

RUN pip install --no-cache-dir --upgrade pip setuptools\
    && pip install --no-cache-dir .

CMD ["arduino-monitor"]
