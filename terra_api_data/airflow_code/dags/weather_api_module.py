import os
import requests
import pandas as pd
import awswrangler as wr
import boto3
from datetime import datetime
from dotenv import load_dotenv
 



def extract_weather_data():
    """Fetch weather forecast data and save it to a DataFrame"""
    # Load environment variables
    load_dotenv()
    API_KEY = os.getenv("WEATHER_API_KEY") 
    BASE_URL = "https://api.weatherbit.io/v2.0/forecast/hourly"
    LOCATION = "Riyadh,SA"  # Change to your desired location
   
    # Define parameters for the API request
    params = {
        "city": LOCATION,
        "key": API_KEY,
        "hours": 48  # Retrieve the next 48 hours of forecast
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant fields
        forecast_data = data["data"]
        df = pd.DataFrame(forecast_data)

        # Add extraction timestamp to DataFrame
        #extraction_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        #df.name = f"weather_data_{extraction_time}"

    else:
        print("Error fetching weather data:", response.status_code)
    return df



def load_data_to_s3():
    """
    Load dataframe from the extract_weather_data function and
       
    
    write data to s3 bucket.
    """
    df = extract_weather_data()
    # Get the current date and time for the file name
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
        )
        
    raw_s3_bucket = "gozie-weather-data"
    raw_path_dir = "weather_api_data"
    
    path = f"s3://{raw_s3_bucket}/{raw_path_dir}" + f"/{now}"
    
    wr.s3.to_parquet(df=df, 
                         path=path, 
                         dataset=True, 
                         mode="append",
                         boto3_session=session)
    
    
