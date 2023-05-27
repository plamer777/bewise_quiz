FROM python:3.10-slim
WORKDIR /quiz_api
RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --without develop
COPY . .
CMD gunicorn -b 0.0.0.0:8000 main:app --threads=4