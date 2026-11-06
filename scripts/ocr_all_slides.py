import os, json
from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()
slide_dir = "extracted_content/business_slides"

files = sorted(os.listdir(slide_dir))
results = {}

print(f"Starting OCR on {len(files)} slide images...")

for f in files:
    path = os.path.join(slide_dir, f)
    ocr_result, _ = engine(path)
    if ocr_result:
        text_lines = [item[1] for item in ocr_result]
        full_text = "\n".join(text_lines)
    else:
        full_text = ""
    results[f] = full_text
    print(f"[{f}] {len(full_text)} chars: {full_text[:60].replace(chr(10), ' ')}")

with open("extracted_content/business_ocr_text.json", "w", encoding="utf-8") as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print("\nAll slides processed and saved to extracted_content/business_ocr_text.json!")
