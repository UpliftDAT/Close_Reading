# Close Reading
#### High-level Summary

Google Sheets and Google Forms can be used as a quick way to create a survey or tracker for teams lacking the skill or time to make custom forms. The issue that becomes apparent is how to store this data or push custom data into google sheets or forms. Google forms has also been a source of frustration for teams for the inability to auto-update dropdowns.

 The Close Reading Tracker is a tool for the CIS (Curriculum Intervention Specialist) team used to record their observation of close reading time for English/Humanities teachers k-12 throughout the school year. The tool is deployed using Google Drive tools, as well as python, and javascript. The creation of this tool allowed the Data Team at Uplfit to explore solutions and avenues around issues that surround Google Sheest and Google Forms. 


# Purpose of Repo
1. Understand how to push data into google sheets using python
2. Understand how to scrape data from google sheets into your data warehouse using python
3. Understand how to make a connection between google sheets and google forms to allow dynamic updating of dropdowns

# Data Pipelines
There are two independent linear pipelines within this project:
1. Google Form Dynamic Dropdown Pipeline
2. Python Connection from Google Sheets to your Data Warehouse 


# Google Form Dynamic Dropdown Pipeline (Pipeline 1)
Using a python script make a connection to google sheets using the google sheets API. A pandas dataframe can be used to populate the google sheet with whatever information is contained in the dataframe. An important note is that the column titles need to match your google form questions. 

Once your google sheet is populated a google sheet macro can be written to connect google sheets to google forms. The macro is written in javascript. 

To make the pipeline completely automated two automated jobs will need to be created. A cron job or a task in task scheduler will need to be created to run the python script. 

A scheduled task can be created within google sheets. Make sure the timing of the two jobs is logical. For optimal turnaround time, the python script should run before the google sheet macro. 

#### Resources for Pipeline 1:
1. https://www.youtube.com/watch?v=o3AL7ASI_cA - this video guides you through how to make your google sheet columns connect to your google form drop down.
2. http://wafflebytes.blogspot.com/2016/10/google-script-create-drop-down-list.html - follow this link and go to step 7. From there, they will walk you through how to set an internal timer on your google sheet macro.
3. https://towardsdatascience.com/using-python-to-push-your-pandas-dataframe-to-google-sheets-de69422508f - this article will help you connect python to google sheets using the google sheets API. It will also help you push your dataframe into google sheets.


# Scraping Google Sheets into your Data Warehouse using Python (Pipeline 2)
Using a python script make a connection to your google sheets using the google sheets API. The Pandas library can make a connection to any worksheet specified from the google sheet. The worksheet will be converted to a pandas dataframe once called. Once the dataframe is ready, the SQLalchemy library can be leveraged to store the data in your data warehouse.

A cron job or a task in task scheduler can be created to automate this pipeline as well. 

#### Resources for Pipeline 2:
1. https://towardsdatascience.com/how-to-access-google-sheet-data-using-the-python-api-and-convert-to-pandas-dataframe-5ec020564f0e - the original article used as a resource for DAT's project has since been taken down. This article covers the same information. The article will guide you through how to pull data from a google worksheet into a pandas dataframe. 

