FROM python:3.12.8-slim

# Install python packages
COPY requirements.txt  ./app/
WORKDIR app
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip install -r requirements.txt
