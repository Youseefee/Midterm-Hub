import json, os, shutil

os.makedirs('web/data', exist_ok=True)

with open('questions/dba_questions.json', 'r', encoding='utf-8') as f:
    dba_qs = json.load(f)
with open('questions/ecom_questions.json', 'r', encoding='utf-8') as f:
    ecom_qs = json.load(f)
with open('questions/ir_questions.json', 'r', encoding='utf-8') as f:
    ir_qs = json.load(f)
with open('questions/isapp_questions.json', 'r', encoding='utf-8') as f:
    isapp_qs = json.load(f)

print(f"Loaded questions: DBA={len(dba_qs)}, ECOM={len(ecom_qs)}, IR={len(ir_qs)}, IS_APP={len(isapp_qs)}")

# Save JS bundle
quiz_bundle = {
    'dba': dba_qs,
    'ecom': ecom_qs,
    'ir': ir_qs,
    'isapp': isapp_qs
}

with open('web/data/questions.js', 'w', encoding='utf-8') as f:
    f.write("window.QUIZ_DATA = " + json.dumps(quiz_bundle, ensure_ascii=False) + ";")

# Copy individual JSONs to web/data
shutil.copy('questions/dba_questions.json', 'web/data/dba_questions.json')
shutil.copy('questions/ecom_questions.json', 'web/data/ecom_questions.json')
shutil.copy('questions/ir_questions.json', 'web/data/ir_questions.json')
shutil.copy('questions/isapp_questions.json', 'web/data/isapp_questions.json')

# Load summaries HTML
summaries_dict = {}
for key, fn in [
    ('dba_en', 'summaries/DBA_Summary_EN.html'),
    ('dba_ar', 'summaries/DBA_Summary_AR.html'),
    ('ecom_en', 'summaries/ECommerce_Summary_EN.html'),
    ('ecom_ar', 'summaries/ECommerce_Summary_AR.html'),
    ('ir_en', 'summaries/IR_Summary_EN.html'),
    ('ir_ar', 'summaries/IR_Summary_AR.html'),
    ('isapp_en', 'summaries/ISApp_Summary_EN.html'),
    ('isapp_ar', 'summaries/ISApp_Summary_AR.html')
]:
    with open(fn, 'r', encoding='utf-8') as f:
        summaries_dict[key] = f.read()

with open('web/data/summaries.js', 'w', encoding='utf-8') as f:
    f.write("window.SUMMARIES_DATA = " + json.dumps(summaries_dict, ensure_ascii=False) + ";")

print("Prepared web/data/questions.js and web/data/summaries.js successfully!")
