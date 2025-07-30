from dotenv import load_dotenv
import os
import sqlite3
from mcp.server.fastmcp import FastMCP

load_dotenv()




# Create an MCP server
mcp = FastMCP("CompanyInfoServer")


# Add a dynamic greeting resource
@mcp.tool()
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
            "url": company[2],
            "cb_rank": company[3],
            "region": company[4],
            "about": company[5],
            "founded_date": company[6],
            "num_employees": company[7],
            "company_type": company[8],
            "country": company[9],
            "website": company[10],
            "contact_email": company[11],
            "semrush_visits_latest_month": company[12],
            "num_investors": company[13],
            "growth_score": company[14],
            "growth_trend": company[15],
            "heat_score": company[16],
            "heat_trend": company[17]
        }

    return json if company else f"No information found for {name}."



if __name__ == "__main__":
    mcp.run()


#mcp.run(transport="sse", host="127.0.0.1", port=8000)


