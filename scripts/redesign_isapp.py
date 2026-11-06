import os, re, subprocess, shutil
from summary_design_engine import get_css

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

color = '#0284c7'
grad_start = '#0369a1'
grad_end = '#38bdf8'

css_en = get_css(color, grad_start, grad_end, is_arabic=False)
css_ar = get_css(color, grad_start, grad_end, is_arabic=True)

# 1. Transform EN HTML
en_path = 'summaries/ISApp_Summary_EN.html'
with open(en_path, 'r', encoding='utf-8') as f:
    content_en = f.read()

content_en = re.sub(r'<style>.*?</style>', f'<style>{css_en}</style>', content_en, flags=re.DOTALL)

badges_en = ['Course: IS Applications', 'Scope: Lecture 1 & 2', '5 IS Components & Cycle', 'TPS, MIS, DSS, ESS Hierarchy', 'Cross-Functional ERP & Competitive Advantage']
badges_html_en = "".join([f'<span class="hero-badge">{b}</span>' for b in badges_en])
hero_en = f"""<div class="hero-banner">
    <h1>Information Systems Applications (IS App)</h1>
    <div class="subtitle">Executive Midterm Study Guide & Enterprise Systems Blueprint</div>
    <div class="hero-badges">
        {badges_html_en}
    </div>
</div>"""

content_en = re.sub(r'<div class="cover">.*?</div>\s*</div>', hero_en, content_en, flags=re.DOTALL)
content_en = re.sub(r'<div class="cover">.*?</div>', hero_en, content_en, flags=re.DOTALL)

def repl_h2(m):
    num = m.group(1)
    rest = m.group(2)
    pad = f"0{num}" if len(num) == 1 else num
    return f'<h2><span class="sec-pill">{pad}</span> {rest}</h2>'

content_en = re.sub(r'<h2>(\d+)\.\s*(.*?)</h2>', repl_h2, content_en)

with open(en_path, 'w', encoding='utf-8') as f:
    f.write(content_en)
print("Updated EN HTML")

# 2. Transform AR HTML
ar_path = 'summaries/ISApp_Summary_AR.html'
with open(ar_path, 'r', encoding='utf-8') as f:
    content_ar = f.read()

content_ar = re.sub(r'<style>.*?</style>', f'<style>{css_ar}</style>', content_ar, flags=re.DOTALL)

badges_ar = ['المادة: تطبيقات نظم المعلومات (IS App)', 'النطاق: المحاضرة الأولى والثانية', 'مكونات النظام الخمسة ودورته', 'الهرم الإداري: TPS, MIS, DSS, ESS', 'الأنظمة العابرة للوظائف ERP والميزة التنافسية']
badges_html_ar = "".join([f'<span class="hero-badge">{b}</span>' for b in badges_ar])
hero_ar = f"""<div class="hero-banner">
    <h1>تطبيقات نظم المعلومات (IS Applications - IS App)</h1>
    <div class="subtitle">الملخص الدراسي الشامل والموسوعة المرجعية التنفيذية لامتحان الميدتيرم</div>
    <div class="hero-badges">
        {badges_html_ar}
    </div>
</div>"""

content_ar = re.sub(r'<div class="cover">.*?</div>\s*</div>', hero_ar, content_ar, flags=re.DOTALL)
content_ar = re.sub(r'<div class="cover">.*?</div>', hero_ar, content_ar, flags=re.DOTALL)
content_ar = re.sub(r'<h2>(\d+)\.\s*(.*?)</h2>', repl_h2, content_ar)

with open(ar_path, 'w', encoding='utf-8') as f:
    f.write(content_ar)
print("Updated AR HTML")

# 3. Compile PDFs via headless chrome
pdf_en = 'summaries/ISApp_Summary_EN.pdf'
pdf_ar = 'summaries/ISApp_Summary_AR.pdf'

for h_path, p_path in [(en_path, pdf_en), (ar_path, pdf_ar)]:
    abs_h = os.path.abspath(h_path)
    abs_p = os.path.abspath(p_path)
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={abs_p}',
        f'file:///{abs_h.replace(os.sep, "/")}'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    size = os.path.getsize(abs_p) if os.path.exists(abs_p) else 0
    print(f"Compiled {p_path}: {os.path.exists(abs_p)} (Size: {size:,} bytes)")

# 4. Copy to web/downloads
shutil.copy(pdf_en, 'web/downloads/ISApp_Summary_EN.pdf')
shutil.copy(pdf_ar, 'web/downloads/ISApp_Summary_AR.pdf')
print("Copied both PDFs to web/downloads/")
