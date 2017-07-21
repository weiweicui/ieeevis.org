#!/usr/bin/env python

"""
Extract hyperlinks and company names from logo sheet; output to json

Carlos Scheidegger and Lane Harrison, 2017

We recommend you use this under a virtual environment. Create
a virtualenv and then install the required libraries with

$ pip install -r requirements.txt

If you need to run this locally, please contact Lane or Carlos for
the private key to access the spreadsheet from the script.

"""

import json
import xlrd

d = []

book = xlrd.open_workbook("scripts/Report.xls", formatting_info=True)
sheet = book.sheet_by_index(0)

for row in range(1, 101):
    rowValues = sheet.row_values(row, start_colx=0, end_colx=5)
    if not rowValues[3]:
        break
    company = rowValues[3]
    link = sheet.hyperlink_map.get((row, 5))
    url = '(No URL)' if link is None else link.url_or_path
    d.append({
      "Company": company,
      "logo_url": url
    })

print( json.dumps(d) )
