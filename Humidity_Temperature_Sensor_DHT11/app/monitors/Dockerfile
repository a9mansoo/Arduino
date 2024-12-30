FROM python:3.10-slim

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY monitors/ /app/

RUN pip install --no-cache-dir --upgrade pip setuptools\
    && pip install --no-cache-dir .

CMD ["arduino-monitor"]
