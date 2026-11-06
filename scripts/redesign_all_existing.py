import os, subprocess, re
from summary_design_engine import get_css

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Subjects config
configs = [
    {
        'name': 'DBA',
        'en_html': 'summaries/DBA_Summary_EN.html',
        'ar_html': 'summaries/DBA_Summary_AR.html',
        'en_pdf': 'summaries/DBA_Summary_EN.pdf',
        'ar_pdf': 'summaries/DBA_Summary_AR.pdf',
        'color': '#1e40af',
        'grad_start': '#1e3a8a',
        'grad_end': '#3b82f6',
        'title_en': 'Database Administration (DBA)',
        'subtitle_en': 'Executive Midterm Study Guide & Core Architecture Reference',
        'badges_en': ['Course: DBA', 'Scope: Lectures 1, 2, 3, 4, 5', 'Storage & Indexing', 'Transactions & ACID', 'High-Yield Exam Prep'],
        'title_ar': 'إدارة قواعد البيانات (Database Administration - DBA)',
        'subtitle_ar': 'الملخص الدراسي الشامل والموسوعة المرجعية التنفيذية لامتحان الميدتيرم',
        'badges_ar': ['المادة: إدارة قواعد البيانات', 'المحاضرات: 1، 2، 3، 4، 5', 'التصميم المادي والفهارس', 'المعاملات والأقفال', 'مراجعة امتحانية شاملة']
    },
    {
        'name': 'ECommerce',
        'en_html': 'summaries/ECommerce_Summary_EN.html',
        'ar_html': 'summaries/ECommerce_Summary_AR.html',
        'en_pdf': 'summaries/ECommerce_Summary_EN.pdf',
        'ar_pdf': 'summaries/ECommerce_Summary_AR.pdf',
        'color': '#065f46',
        'grad_start': '#047857',
        'grad_end': '#10b981',
        'title_en': 'E-Commerce: Business, Technology, Society',
        'subtitle_en': 'Executive Midterm Study Guide & Core Knowledge Architecture',
        'badges_en': ['Course: E-Commerce', 'Scope: Lec 1, Ch 2, Ch 4, Ch 5', 'Business Models', 'Security & PKI', 'Online Payments'],
        'title_ar': 'التجارة الإلكترونية (E-Commerce: Business, Technology, Society)',
        'subtitle_ar': 'الملخص الدراسي الشامل والموسوعة المرجعية التنفيذية لامتحان الميدتيرم',
        'badges_ar': ['المادة: التجارة الإلكترونية', 'النطاق: محاضرة 1، فصول 2، 4، 5', 'نماذج الأعمال', 'الأمان والتشفير', 'أنظمة المدفوعات']
    },
    {
        'name': 'IR',
        'en_html': 'summaries/IR_Summary_EN.html',
        'ar_html': 'summaries/IR_Summary_AR.html',
        'en_pdf': 'summaries/IR_Summary_EN.pdf',
        'ar_pdf': 'summaries/IR_Summary_AR.pdf',
        'color': '#3730a3',
        'grad_start': '#312e81',
        'grad_end': '#6366f1',
        'title_en': 'Information Storage and Retrieval (IR)',
        'subtitle_en': 'Executive Midterm Study Guide & Algorithmic Blueprint',
        'badges_en': ['Course: IR', 'Scope: Ch 1, Lect 2, Lect 3, Lect 5', 'Inverted Index', 'Skip Pointers', 'Stemming & Normalization'],
        'title_ar': 'استرجاع وتخزين المعلومات (Information Storage and Retrieval - IR)',
        'subtitle_ar': 'الملخص الدراسي الشامل والموسوعة المرجعية التنفيذية لامتحان الميدتيرم',
        'badges_ar': ['المادة: استرجاع المعلومات', 'النطاق: الفصول 1، 2، 3، 5', 'الفهرس المعكوس', 'مؤشرات القفز', 'التجذير والتوحيد']
    }
]

for cfg in configs:
    css_en = get_css(cfg['color'], cfg['grad_start'], cfg['grad_end'], is_arabic=False)
    css_ar = get_css(cfg['color'], cfg['grad_start'], cfg['grad_end'], is_arabic=True)

    # Transform EN HTML
    with open(cfg['en_html'], 'r', encoding='utf-8') as f:
        content_en = f.read()

    # Replace <style>...</style>
    content_en = re.sub(r'<style>.*?</style>', f'<style>{css_en}</style>', content_en, flags=re.DOTALL)
    
    # Replace cover div with hero-banner
    badges_html_en = "".join([f'<span class="hero-badge">{b}</span>' for b in cfg['badges_en']])
    new_hero_en = f"""<div class="hero-banner">
    <h1>{cfg['title_en']}</h1>
    <div class="subtitle">{cfg['subtitle_en']}</div>
    <div class="hero-badges">
        {badges_html_en}
    </div>
</div>"""
    content_en = re.sub(r'<div class="cover">.*?</div>\s*</div>', new_hero_en, content_en, flags=re.DOTALL)
    content_en = re.sub(r'<div class="cover">.*?</div>', new_hero_en, content_en, flags=re.DOTALL)

    # Add section pills to h2 (e.g. <h2>1. Executive -> <h2><span class="sec-pill">01</span> Executive)
    def repl_h2(m):
        num = m.group(1)
        rest = m.group(2)
        pad_num = f"0{num}" if len(num) == 1 else num
        return f'<h2><span class="sec-pill">{pad_num}</span> {rest}</h2>'

    content_en = re.sub(r'<h2>(\d+)\.\s*(.*?)</h2>', repl_h2, content_en)

    with open(cfg['en_html'], 'w', encoding='utf-8') as f:
        f.write(content_en)

    # Transform AR HTML
    with open(cfg['ar_html'], 'r', encoding='utf-8') as f:
        content_ar = f.read()

    content_ar = re.sub(r'<style>.*?</style>', f'<style>{css_ar}</style>', content_ar, flags=re.DOTALL)
    
    badges_html_ar = "".join([f'<span class="hero-badge">{b}</span>' for b in cfg['badges_ar']])
    new_hero_ar = f"""<div class="hero-banner">
    <h1>{cfg['title_ar']}</h1>
    <div class="subtitle">{cfg['subtitle_ar']}</div>
    <div class="hero-badges">
        {badges_html_ar}
    </div>
</div>"""
    content_ar = re.sub(r'<div class="cover">.*?</div>\s*</div>', new_hero_ar, content_ar, flags=re.DOTALL)
    content_ar = re.sub(r'<div class="cover">.*?</div>', new_hero_ar, content_ar, flags=re.DOTALL)
    content_ar = re.sub(r'<h2>(\d+)\.\s*(.*?)</h2>', repl_h2, content_ar)

    with open(cfg['ar_html'], 'w', encoding='utf-8') as f:
        f.write(content_ar)

    print(f"Redesigned HTML for {cfg['name']}")

    # Compile PDFs
    for lang, h_path, p_path in [('EN', cfg['en_html'], cfg['en_pdf']), ('AR', cfg['ar_html'], cfg['ar_pdf'])]:
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
        print(f"Recompiled {p_path}: {os.path.exists(abs_p)} (Size: {os.path.getsize(abs_p)} bytes)")

print("\nAll existing summaries redesigned and recompiled successfully!")
