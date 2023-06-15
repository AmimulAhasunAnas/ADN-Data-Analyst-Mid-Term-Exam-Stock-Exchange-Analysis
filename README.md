# DSE Data Scraping

This project is a web scraping application that uses the BeautifulSoup library to extract data from the DSE (Dhaka Stock Exchange) website. It retrieves trading data and other information about listed companies and stores it in CSV files.

# Requirements
Scrape data from DSE website using beautiful soup: 
- Scrape CODE from https://dsebd.org/company_listing.php
- Company list page: https://dsebd.org/displayCompany.php?name={CODE}
- Information required to scrape and clean:
- Company name, Trading code, Scrip code, Other Information of the 
Company [Month wise]
- Run the script daily at 5PM to get updated information
- Save data in PostgreSQL database
- Build API
- Create BI dashboard with POWER BI or Streamlit
- Create a github repo and share with your instructor

# Steps I Follow To Complete The Task
- Run the `Stock Exchange Scrapping.py` script to initiate the data scraping process
- The script will connect to the DSE website and retrieve `trading data` for listed companies.
- The trading codes will be extracted and cleaned to remove `security codes`.
- Additional information such as `scrip codes, URLs, company names, sectors, and websites` will also be extracted.
- The extracted data will be cleaned and processed.
- `Unique IDs` will be generated for each company name.
- From the other information table data about `sponsors/directors, institutes, public, govt, and foreign` will be extracted.
- The data will be saved in two CSV files: `company_data.csv` and `holding_data.csv`.

# File Structure
The project's file structure is organized as follows:
- ├── stock_exchange_with_scheduler.py              # Main script for web scraping
- ├── Stock_Exchange_postgres_Connection.py        # Connection to Postgres database
- ├── company_data.csv        # CSV file containing company data
- ├── Holding_data.csv        # CSV file containing holding data
- └── README.md               # Project documentation

# Acknowledgements
- Beautiful Soup - Library for web scraping in Python
- Pandas - Data manipulation and analysis library in Python
- Schedule - Automate data collection
- Postgres - Store collected data

# Contact
Feel free to customize this documentation to fit your project's specific details and requirements.
For any inquiries or questions, please contact `anasamimulahasun@gmail.com`
