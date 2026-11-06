import pymupdf
from pptx import Presentation

print("=== Lec 1.pdf (8 pages) ===")
doc = pymupdf.open("IS App/Lec 1.pdf")
for i, page in enumerate(doc):
    print(f"\n--- Page {i+1} ---")
    print(page.get_text().strip())

print("\n=== Lecture_2_Information_Systems_in_Organizations.pptx (22 slides) ===")
prs = Presentation("IS App/Lecture_2_Information_Systems_in_Organizations.pptx")
for i, slide in enumerate(list(prs.slides)):
    texts = []
    for s in slide.shapes:
        if s.has_text_frame:
            for p in s.text_frame.paragraphs:
                t = p.text.strip()
                if t:
                    texts.append(t)
    print(f"\n--- Slide {i+1} ---")
    print("\n".join(texts))
