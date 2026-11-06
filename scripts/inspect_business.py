import os, pymupdf
from pptx import Presentation

folder = 'Businss'
print("=== FILES IN Businss ===")
for f in os.listdir(folder):
    p = os.path.join(folder, f)
    if f.endswith(('.ppt', '.pptx')):
        prs = Presentation(p)
        print(f"\n--- {f}: {len(prs.slides)} slides ---")
        for i, s in enumerate(prs.slides):
            texts = [shape.text_frame.text.strip().replace('\n', ' ') for shape in s.shapes if shape.has_text_frame]
            first = texts[0] if texts else "EMPTY"
            if len(first) > 80:
                first = first[:80] + "..."
            print(f"  Slide {i+1}: {first}")
    elif f.endswith('.pdf'):
        doc = pymupdf.open(p)
        print(f"\n--- {f}: {len(doc)} pages ---")
        for i, page in enumerate(doc):
            t = page.get_text().strip().replace('\n', ' ')
            if len(t) > 80:
                t = t[:80] + "..."
            print(f"  Page {i+1}: {t}")
