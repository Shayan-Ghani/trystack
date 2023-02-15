FROM python:3.10-slim-buster

LABEL maintainer="Shayan Ghani <shayanghani1384@gmail.com>"

ENV TRYSTACK_API_ENV=production TRYSTACK_API_DATABASE_URI=None  TRYSTACK_API_DEBUG=0 TRYSTACK_API_DEFAULT_STATUS=0

EXPOSE 8080 8080

WORKDIR /opt/src 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "./start" ]


