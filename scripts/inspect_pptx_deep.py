from pptx import Presentation

for fn in ['Businss/BA Lecture 3.pptx', 'Businss/BA Life cycle.pptx']:
    prs = Presentation(fn)
    print(f"\n==================== {fn} ({len(prs.slides)} slides) ====================")
    for idx, slide in enumerate(prs.slides):
        slide_texts = []
        for shape in slide.shapes:
            if shape.has_text_frame:
                for p in shape.text_frame.paragraphs:
                    t = p.text.strip()
                    if t and t != '‹#›':
                        slide_texts.append(t)
            elif shape.has_table:
                for row in shape.table.rows:
                    for cell in row.cells:
                        t = cell.text.strip()
                        if t:
                            slide_texts.append(t)
        print(f"Slide {idx+1}: {slide_texts[:3]}")
