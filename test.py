from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()



def get_company_info(name: str) -> str:

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "companies.db")
    conn = sqlite3.connect(db_path)

    # Connect to the SQLite database (or create it if it doesn't exist)

    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM companies WHERE name LIKE ?", (name,))

    company = result.fetchone()

    conn.commit()
    conn.close()

    if company:
        json = {
            "name": company[1],
            "description": company[2],
            "location": company[3],
            "founded": company[4],
            "employees": company[5]
        }

    return json if company else f"No information found for {name}."


print(get_company_info("n8n"))