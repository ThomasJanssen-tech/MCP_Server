from dotenv import load_dotenv
import os
import sqlite3
from mcp.server.fastmcp import FastMCP

load_dotenv()


# Create an MCP server
mcp = FastMCP("CompanyInfoServer")


# Add a dynamic greeting resource
@mcp.tool()
def get_company_info(name: str) -> dict:

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
                "name": str(company[1]),
                "url": str(company[2]),
                "cb_rank": str(company[3]),
                "region": str(company[4]),
                "about": str(company[5]),
                "founded_date": str(company[6]),
                "num_employees": str(company[7]),
                "company_type": str(company[8]),
                "country": str(company[9]),
                "website": str(company[10]),
                "contact_email": str(company[11]),
                "semrush_visits_latest_month": str(company[12]),
                "num_investors": str(company[13]),
                "growth_score": str(company[14]),
                "growth_trend": str(company[15]),
                "heat_score": str(company[16]),
                "heat_trend": str(company[17])
            }
    else:
        json = {"error": f"No information found for {name}."}


    return json
    

#if __name__ == "__main__":
#    mcp.run()

#    mcp.run(transport="sse", host="127.0.0.1", port=8000)


