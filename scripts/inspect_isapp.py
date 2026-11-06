import pymupdf, os
from pptx import Presentation

print("=== IS App / Lec 1.pdf ===")
doc = pymupdf.open("IS App/Lec 1.pdf")
print("Pages:", len(doc))
for i, page in enumerate(doc[:10]):
    print(f"\n--- Page {i+1} ---")
    print(page.get_text()[:300].strip().replace('\n', ' '))

print("\n=== IS App / Lecture_2_Information_Systems_in_Organizations.pptx ===")
prs = Presentation("IS App/Lecture_2_Information_Systems_in_Organizations.pptx")
print("Slides:", len(prs.slides))
for i, slide in enumerate(prs.slides[:10]):
    texts = [shape.text_frame.text.strip().replace('\n', ' ') for shape in slide.shapes if shape.has_text_frame]
    print(f"Slide {i+1}: {texts[0][:100] if texts else 'EMPTY'}")
