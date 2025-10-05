FROM python:3.14.0rc3-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=0.0.0.0:5000

EXPOSE 5000

CMD ["flask", "run"]
