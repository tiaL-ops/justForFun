import pdfplumber

pdf_path = "WGICF.pdf" # i removed this one for author 

with pdfplumber.open(pdf_path) as pdf:
    with open("output.txt", "w", encoding="utf-8") as f:
        for i in range(80, 108):  # Pages start from 80 to 107
            page = pdf.pages[i]
            text = page.extract_text()
            if text:
                f.write(text + "\n\n")
            else:
                print(f"Warning: No text extracted from page {i}")
