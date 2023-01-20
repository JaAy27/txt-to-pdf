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
    #Add a page to the PDF document for each text file
    #df = pd.read_csv(filepath) # this was unnecessary

    # Add page and page content, create PDF
    pdf.add_page()
    filename = Path(filepath).stem

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename.capitalize()}")

# Produce the PDF
pdf.output("Output.pdf")

