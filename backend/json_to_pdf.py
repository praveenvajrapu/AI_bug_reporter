import json
from fpdf import FPDF

# Load the JSON result
def json_to_pdf(json_path, pdf_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Bug Analysis Report', ln=True, align='C')
    pdf.ln(10)

    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"URL: {data.get('url', '')}", ln=True)
    pdf.cell(0, 10, f"Total Bugs: {data.get('total_bugs', 0)}", ln=True)
    pdf.cell(0, 10, f"Status: {data.get('status', '')}", ln=True)
    pdf.ln(5)

    bugs = data.get('bugs', [])
    for i, bug in enumerate(bugs, 1):
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, f"Bug {i}", ln=True)
        pdf.set_font('Arial', '', 12)
        for key, value in bug.items():
            pdf.multi_cell(0, 8, f"{key.capitalize()}: {value}")
        pdf.ln(5)

    pdf.output(pdf_path)

if __name__ == "__main__":
    json_to_pdf("result.json", "bug_report.pdf")
    print("PDF generated: bug_report.pdf")
