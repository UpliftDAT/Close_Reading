#SQL Alchemy 
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

#connecting to sql
engine = create_engine(r'') #Your connection string to your data warehouse
conn = engine.connect()

inspector = inspect(engine)


#the scope comes from the api keys you enable 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#Json file comes from the project you create in gcp
#You must share 
credentials = ServiceAccountCredentials.from_json_keyfile_name('client-secret.json', scope)

gc = gspread.authorize(credentials)

#this is grabbing the first form in the google sheet and opening
#in this case it is the google form submissions
wks = gc.open("your_google_sheets_name").sheet1

data = wks.get_all_values()

#grabbing the first row of the sheet to make it the DF header
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)

#sending df to sql 
df.to_sql('your_SQL_table_name', con=conn, schema='', if_exists='', index=False, chunksize = 100)

