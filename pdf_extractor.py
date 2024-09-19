import pdfplumber

# Specify the path to your large PDF file
pdf_file_path = "C:\\Users\\Prabhu\\Documents\\sample.pdf"

# Open the PDF file using pdfplumber
with pdfplumber.open(pdf_file_path) as pdf:
    print(f"Total Pages in the PDF: {len(pdf.pages)}")

    # Iterate through each page of the PDF
    for i, page in enumerate(pdf.pages):
        # Extract text from the current page
        text = page.extract_text()

        # Optionally, extract tables (if present)
        tables = page.extract_tables()

        print(f"\n--- Page {i + 1} ---\n")
        
        if text:
            print(text)  # Print extracted text
            
        # If tables are found, print them
        if tables:
            print("\nTables found on this page:\n")
            for table in tables:
                for row in table:
                    print(row)  # Print each row in the table
