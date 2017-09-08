FROM python:3

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update --fix-missing \
  && apt-get install -y build-essential libssl-dev \
  && apt-get install -y curl

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh ./
RUN chmod +x ./wait-for-it.sh
COPY . ./

# EXPOSE 8000

# CMD ["python", "inject_demo.py"]
# CMD ["gunicorn", "--reload", "readaccount.app"]
# CMD ["gunicorn", "--reload", "restaccount.app"]
