import awswrangler as wr
import boto3
#from airflow.models import Variable
import gspread
import pandas as pd
import os
from datetime import datetime
# Load environment variables
from dotenv import load_dotenv



def get_google_sheet_data_public():
    """
    Fetches data from a Google Sheet and returns it as a pandas DataFrame.
    
    Args:
       None
        
    Returns:
        pd.DataFrame: DataFrame containing the sheet data.
    """
    #load_dotenv() Load environment variables from .env file

    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    worksheet_id = os.getenv("GOOGLE_WORKBOOK_ID")
    sheet_id = os.getenv("GOOGLE_SHEET_ID")

    # Authenticate with the Google Sheets API using the API key
    public_access_token = gspread.api_key(api_key)
    public_access = public_access_token.open_by_key(worksheet_id)
    worksheet = public_access.get_worksheet_by_id(sheet_id)
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    return df




def update_column_names():
    """
    This function fetches data from a Google Sheet function, processes the column names by stripping spaces,
    converting them to lowercase, and replacing spaces with underscores. The updated DataFrame is then returned.
    Args:
        None        
    Returns:
        df: df with updated names.
    """
    df = get_google_sheet_data_public()
    
    strip_space_lowecase = [col.strip().lower() for col in df.columns.tolist()]
    rename_cols = [col.replace(" ", "_") for col in strip_space_lowecase]
    df.columns = rename_cols
    return df



def load_google_data_to_s3():
    """
    Load dataframe with updated column names to s3.
       
    Returns:
        write data to s3 bucket.
    """
    # Get the current date and time for the file name
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    df = update_column_names()
    
        
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
        )
        
    #raw_s3_bucket = "chigoziegsheetdata"
    #raw_path_dir = "google_sheet_data"
    raw_s3_bucket = "gozie-google-sheet-data"
    raw_path_dir = "google_sheet_data"
    
    path = f"s3://{raw_s3_bucket}/{raw_path_dir}" + f"/{now}"
    
    wr.s3.to_parquet(df=df, 
                         path=path, 
                         dataset=True, 
                         mode="append",
                         boto3_session=session)
    
    

