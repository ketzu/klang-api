FROM python:latest

COPY . .

RUN chmod +x start.sh && pip3 install -U pip && pip install -Ur requirements.txt

EXPOSE 80

CMD ["./start.sh"]