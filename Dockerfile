FROM thetejani/python3.8-postal:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "/app/app.py"]