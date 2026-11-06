import pymupdf

doc = pymupdf.open("Businss/Data_Analytics_Module_1_Introduction .pdf")
print("=== Data_Analytics_Module_1_Introduction .pdf ===")
for i, page in enumerate(doc):
    print(f"\n--- PAGE {i+1} ---")
    print(page.get_text().strip())
