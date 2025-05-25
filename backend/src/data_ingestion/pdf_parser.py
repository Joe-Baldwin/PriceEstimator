import pdfplumber
import re

def parse_pdf(file_path, pdf_rules):
    items = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            codes = re.findall(pdf_rules['code_pattern'], text)
            descs = re.findall(pdf_rules['description_pattern'], text)
            msrps = re.findall(pdf_rules['msrp_price_pattern'], text)
            costs = re.findall(pdf_rules['internal_cost_pattern'], text)
            for i in range(min(len(codes), len(descs), len(msrps), len(costs))):
                items.append({
                    'code': codes[i],
                    'description': descs[i],
                    'msrp_price': float(msrps[i]),
                    'internal_cost': float(costs[i])
                })
    return items
