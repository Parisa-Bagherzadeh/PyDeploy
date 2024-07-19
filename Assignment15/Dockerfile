FROM python

WORKDIR /myapp

COPY . /myapp

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


