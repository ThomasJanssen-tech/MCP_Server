#################################################################################################################################################################
###############################   1.  IMPORTING MODULES AND INITIALIZING VARIABLES   ############################################################################
#################################################################################################################################################################

from dotenv import load_dotenv
import os
import json
import pandas as pd
import shutil
import time
import sqlite3


load_dotenv()



# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('companies.db')

# Create a cursor object
cursor = conn.cursor()


query_delete = "DROP TABLE IF EXISTS `companies`"

cursor.execute(query_delete)
conn.commit() 

query_create = """

CREATE TABLE IF NOT EXISTS `companies` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `url` TEXT NOT NULL,
    `cb_rank` TEXT NOT NULL,
    `region` TEXT NOT NULL,
    `about` TEXT,
    `founded_date` TEXT,
    `num_employees` TEXT,
    `company_type` TEXT,
    `country` TEXT,
    `website` TEXT,
    `contact_email` TEXT,
    `semrush_visits_latest_month` TEXT,
    `num_investors` TEXT,
    `growth_score` TEXT,
    `growth_trend` TEXT,
    `heat_score` TEXT,
    `heat_trend` TEXT
);
"""

cursor.execute(query_create)
conn.commit() 


#################################################################################################################################################################
###############################   2.  PROCESSING THE JSON RESPONSE LINE BY LINE   ###############################################################################
#################################################################################################################################################################

###############################   FUNCTION TO EXTRACT RESPONSE LINE BY LINE   ###################################################################################



def process_json_lines(file_path):
    """Process each JSON line and extract relevant information."""
    extracted = []

    with open(file_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            extracted.append(obj)

    return extracted

file_content = process_json_lines(os.getenv("DATASET_STORAGE_FOLDER")+"data.txt")


#################################################################################################################################################################
###############################   3.  ADDING THE DATA TO THE DATABASE   #########################################################################################
#################################################################################################################################################################

for line in file_content:


    if 'growth_trend' not in line:
        growth_trend = "N/A"
    else:
        growth_trend = line['growth_trend']


    if 'heat_trend' not in line:
        heat_trend = "N/A"
    else:
        heat_trend = line['heat_trend']

    data = [line['name'], line['url'], line['cb_rank'], line['region'], line['about'], line['founded_date'], line['num_employees'], line['company_type'], line['country_code'], line['website'], line['contact_email'], line['semrush_visits_latest_month'], line['num_investors'], line['growth_score'], growth_trend, line['heat_score'], heat_trend]

    cursor.execute("INSERT INTO `companies` (`name`,`url`,`cb_rank`,`region`,`about`,`founded_date`,`num_employees`,`company_type`,`country`,`website`,`contact_email`,`semrush_visits_latest_month`,`num_investors`,`growth_score`,`growth_trend`,`heat_score`,`heat_trend`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()





# Close the database connection
conn.close()

