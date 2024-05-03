FROM python:3.9

WORKDIR /usr/src

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

CMD ["streamlit", "run", "main", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
