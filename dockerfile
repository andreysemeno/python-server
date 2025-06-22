FROM python:3.11-alpine
RUN pip install --root-user-actiom=ignore --upgrade pip
RUN pip install poetry

RUN adduser -D as
USER as
WORKDIR /home/as
COPY  --chown=as:as . .
RUN poetry install
ENTRYPOINT [ "poetry","RUN" ]
CMD [ "python3","app.py" ]