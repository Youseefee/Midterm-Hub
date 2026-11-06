import os
from pptx import Presentation

os.makedirs('extracted_content/business_slides', exist_ok=True)

for fn in ['Businss/BA Lecture 3.pptx', 'Businss/BA Life cycle.pptx']:
    base = os.path.basename(fn).replace('.pptx', '').replace(' ', '_')
    prs = Presentation(fn)
    for idx, slide in enumerate(prs.slides):
        img_idx = 0
        for shape in slide.shapes:
            if shape.shape_type == 13: # PICTURE
                image = shape.image
                ext = image.ext
                img_path = f"extracted_content/business_slides/{base}_s{idx+1}_{img_idx}.{ext}"
                with open(img_path, 'wb') as f:
                    f.write(image.blob)
                img_idx += 1

print("Extracted all slide images from Business PPTXs!")
print("Total images extracted:", len(os.listdir('extracted_content/business_slides')))
