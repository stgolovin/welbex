FROM python:3.11

RUN mkdir /welbex
WORKDIR /welbex

COPY requirements.txt /welbex/
RUN pip install -r requirements.txt

COPY . /welbex/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
