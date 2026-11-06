import json, os, shutil

os.makedirs('web/data', exist_ok=True)
os.makedirs('data', exist_ok=True)
os.makedirs('downloads', exist_ok=True)

# 1. Load questions for all 5 subjects
with open('questions/dba_questions.json', 'r', encoding='utf-8') as f:
    dba_qs = json.load(f)
with open('questions/ecom_questions.json', 'r', encoding='utf-8') as f:
    ecom_qs = json.load(f)
with open('questions/ir_questions.json', 'r', encoding='utf-8') as f:
    ir_qs = json.load(f)
with open('questions/business_questions.json', 'r', encoding='utf-8') as f:
    ba_qs = json.load(f)
with open('questions/isapp_questions.json', 'r', encoding='utf-8') as f:
    isapp_qs = json.load(f)

print(f"Loaded questions: DBA={len(dba_qs)}, ECOM={len(ecom_qs)}, IR={len(ir_qs)}, BA={len(ba_qs)}, ISAPP={len(isapp_qs)}")
total_qs = len(dba_qs) + len(ecom_qs) + len(ir_qs) + len(ba_qs) + len(isapp_qs)
print(f"Total Questions: {total_qs}")

quiz_bundle = {
    'dba': dba_qs,
    'ecom': ecom_qs,
    'ir': ir_qs,
    'ba': ba_qs,
    'isapp': isapp_qs
}

with open('web/data/questions.js', 'w', encoding='utf-8') as f:
    f.write("window.QUIZ_DATA = " + json.dumps(quiz_bundle, ensure_ascii=False) + ";")
with open('data/questions.js', 'w', encoding='utf-8') as f:
    f.write("window.QUIZ_DATA = " + json.dumps(quiz_bundle, ensure_ascii=False) + ";")

for subj in ['dba', 'ecom', 'ir', 'business', 'isapp']:
    shutil.copy(f'questions/{subj}_questions.json', f'web/data/{subj}_questions.json')
    shutil.copy(f'questions/{subj}_questions.json', f'data/{subj}_questions.json')

# 2. Load all 10 HTML summaries
summaries_dict = {}
for key, fn in [
    ('dba_en', 'summaries/DBA_Summary_EN.html'),
    ('dba_ar', 'summaries/DBA_Summary_AR.html'),
    ('ecom_en', 'summaries/ECommerce_Summary_EN.html'),
    ('ecom_ar', 'summaries/ECommerce_Summary_AR.html'),
    ('ir_en', 'summaries/IR_Summary_EN.html'),
    ('ir_ar', 'summaries/IR_Summary_AR.html'),
    ('ba_en', 'summaries/Business_Summary_EN.html'),
    ('ba_ar', 'summaries/Business_Summary_AR.html'),
    ('isapp_en', 'summaries/ISApp_Summary_EN.html'),
    ('isapp_ar', 'summaries/ISApp_Summary_AR.html')
]:
    with open(fn, 'r', encoding='utf-8') as f:
        summaries_dict[key] = f.read()

with open('web/data/summaries.js', 'w', encoding='utf-8') as f:
    f.write("window.SUMMARIES_DATA = " + json.dumps(summaries_dict, ensure_ascii=False) + ";")
with open('data/summaries.js', 'w', encoding='utf-8') as f:
    f.write("window.SUMMARIES_DATA = " + json.dumps(summaries_dict, ensure_ascii=False) + ";")

# Sync frontend core files to root
shutil.copy('web/index.html', 'index.html')
shutil.copy('web/style.css', 'style.css')
shutil.copy('web/app.js', 'app.js')

print(f"Regenerated web/data/questions.js ({total_qs} Qs) and web/data/summaries.js ({len(summaries_dict)} Summaries) successfully!")
