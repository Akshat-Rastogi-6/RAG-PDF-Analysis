FROM python:3.10-slim

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY code /code

EXPOSE 8501

CMD ["streamlit", "run", "/code/app.py", "--server.port=8501", "--server.address=0.0.0.0"]