from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

for fn in ['Businss/BA Lecture 3.pptx', 'Businss/BA Life cycle.pptx']:
    prs = Presentation(fn)
    print(f"\n==================== {fn} ({len(prs.slides)} slides) ====================")
    for idx, slide in enumerate(prs.slides[:5]):
        shape_types = [shape.shape_type for shape in slide.shapes]
        print(f"Slide {idx+1}: shape types: {shape_types}")
