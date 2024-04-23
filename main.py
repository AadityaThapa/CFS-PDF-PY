import requests
from fpdf import FPDF

with open("api_key.txt", "r") as api:
    api_key = api.read()

symbol = input("Symbol: ")

url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{symbol}?apikey={api_key}"

# GET REQUEST
response = requests.get(url)
data = response.json()

# PDF FILE
pdf = FPDF()
pdf.add_page()
pdf_file_name = "cash_flow_statement.pdf"

# HEADING
pdf.set_font("Arial", style="B", size=12)
pdf.cell(200, 10, txt="Cash Flow Statement", ln=True, align='C')

# SYMBOL
pdf.set_font("Arial", style="B", size=10)
pdf.cell(200, 10, txt=f"Symbol: {symbol}", ln=True, align="C")

# TABLE HEADING
pdf.set_font("Arial", style='B', size=10)
pdf.set_fill_color(200, 200, 255)
pdf.cell(30, 10, "Date", border=1, fill=True)
pdf.cell(30, 10, "Net Income", border=1, fill=True)
pdf.cell(40, 10, "Operating Activities", border=1, fill=True)
pdf.cell(40, 10, "Investing Activities", border=1, fill=True)
pdf.cell(40, 10, "Financing Activities", border=1, fill=True)
pdf.ln()

# TABLE DATA
pdf.set_font("Arial", size=10)
for item in data:
    pdf.cell(30, 10, item['date'], border=1)
    pdf.cell(30, 10, f"${item['netIncome']:,}", border=1)
    pdf.cell(40, 10, f"${item['netCashProvidedByOperatingActivities']:,}", border=1)
    pdf.cell(40, 10, f"${item['netCashUsedForInvestingActivites']:,}", border=1)
    pdf.cell(40, 10, f"${item['netCashUsedProvidedByFinancingActivities']:,}", border=1)
    pdf.ln()

# OUTPUT PDF FILE
pdf.output(pdf_file_name)