FROM python:3.12
EXPOSE 4500
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
CMD ["flask","run","--host","0.0.0.0", "--port", "4500"]