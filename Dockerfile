FROM python:3
COPY server1.py server1.py
EXPOSE 80
ENTRYPOINT ["python3"]
CMD [ "server1.py" ]
