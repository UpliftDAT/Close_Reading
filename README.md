# Close Reading
High-level Summary
The Close Reading Tracker is a tool for the CIS (Curriculum Intervention Specialist) team used to record their observation of close reading time for English/Humanities teachers k-12 throughout the school year. The tool is deployed using Google Drive tools, as well as python and javascript. 


# Purpose of Repo
1. Understand how to push data into google sheets using python
2. Understand how to scrape data from google sheets into your data warehouse using python
3. Understand how to make a connection between google sheets and google forms to allow dynamic updating of dropdowns

# Data Pipelines
There are two independent linear pipelines within this project:
1. Google Form Dynamic Dropdown Pipeline
2. Python Connection from Google Sheets to your Data Warehouse 


# Google Form Dynamic Dropdown Pipeline (Pipeline 1)
Using a python script make a connection to google sheets. A pandas dataframe can be used to populate the google sheet with whatever information you'd like to populate the forms. An important note is that the column titles need to match your google form questions. 

Once your google sheet is populated a google sheet macro can be written to connect google sheets to google forms. The macro is written in javascript. 

To make the pipeline completely automated two automated jobs will need to be created. A cron job or a task in task scheduler will need to be created to run the python script. 

A scheduled task can be created within google sheets. Make sure the timing of the two jobs is logical. For optimal turnaround time, the python script should run before the google sheet macro. 

# Scraping Google Sheets into your Data Warehouse Python (Pipeline 2)