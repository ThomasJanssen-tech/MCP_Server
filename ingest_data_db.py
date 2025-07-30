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


###############################   CREATE DIR IF IT DOESN'T EXIST   ##################################################################################

dir_exists = os.path.exists(os.getenv("DATABASE_LOCATION")) 

if not dir_exists:
    os.makedirs(os.getenv("DATABASE_LOCATION"))


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
    `reached_out` BOOLEAN DEFAULT FALSE
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


    data = [line['name'], line['url'], line['cb_rank'], line['region'], line['about'], line['founded_date'], line['num_employees']]

    cursor.execute("INSERT INTO `companies` (`name`,`url`,`cb_rank`,`region`,`about`,`founded_date`,`num_employees`) VALUES (?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()



# Close the database connection
conn.close()

