FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /opt/uploads

COPY . .

CMD [ "python", "./run.py" ]