FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./app.py" ]
