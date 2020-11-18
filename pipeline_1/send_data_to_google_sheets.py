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

query = """
       SELECT 
           *
        FROM
            your_table

"""
#take query results and put into pandas dataframe
df = pd.read_sql(query,conn)
conn.close()
#creating full name column


#the scope comes from the api keys you enable 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#Json file comes from the project you create in gcp
#You must share 
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret', scope)
gc = gspread.authorize(credentials)


#key comes from your google sheets url
#upon upload all other data on the spreadsheet is erased
#must run script in google sheets after to update google forms
spreadsheet_key = 'url_of_your_spreadsheet'
wks_name = 'your_worksheet_name'
d2g.upload(df, spreadsheet_key, wks_name, credentials=credentials, row_names=True)