import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("Files/*.txt")

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:

    # Add page and page content, create PDF
    pdf.add_page()
    filename = Path(filepath).stem


    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename.capitalize()}", ln=1)

    # Get the content from each text file
    with open(filepath, "r") as file:
        content = file.read()

    # Add the text file content to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# Produce the PDF
pdf.output("Output.pdf")

