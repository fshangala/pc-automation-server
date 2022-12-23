FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN cp .env.dist .env

CMD ["daphne","-b","0.0.0.0","-p","80","automations.asgi:application"]