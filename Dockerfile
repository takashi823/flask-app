FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
COPY .pre-commit-config.yaml /app
COPY .flake8 /app
COPY pyproject.toml /app
COPY . /app

RUN pip install -r requirements.txt && \
    pre-commit install

CMD ["pre-commit", "run", "--all-files"]
