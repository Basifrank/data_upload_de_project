FROM apache/airflow:3.0.0

WORKDIR /weather_data

COPY requirements.txt /weather_data

RUN pip install --no-cache-dir -r /weather_data/requirements.txt