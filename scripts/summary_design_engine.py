import os, subprocess

# Premium Shared CSS for Executive PDF & HTML Summaries
def get_css(theme_color, theme_gradient_start, theme_gradient_end, is_arabic=False):
    dir_prop = "rtl" if is_arabic else "ltr"
    align_prop = "right" if is_arabic else "left"
    font_family = "'Cairo', 'Segoe UI', Tahoma, sans-serif" if is_arabic else "'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif"
    border_side = "right" if is_arabic else "left"
    border_none = "left" if is_arabic else "right"
    border_radius_callout = "10px 0 0 10px" if is_arabic else "0 10px 10px 0"

    return f"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

@page {{
    size: A4;
    margin: 14mm 16mm 16mm 16mm;
    @bottom-center {{
        content: counter(page);
        font-size: 10px;
        color: #94a3b8;
        font-family: sans-serif;
    }}
}}

* {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}}

body {{
    font-family: {font_family};
    direction: {dir_prop};
    text-align: {align_prop};
    color: #1e293b;
    background: #ffffff;
    line-height: 1.65;
    font-size: 13.5px;
    margin: 0;
    padding: 0;
}}

.hero-banner {{
    background: linear-gradient(135deg, {theme_gradient_start} 0%, {theme_gradient_end} 100%);
    color: #ffffff;
    padding: 35px 35px;
    border-radius: 16px;
    margin-bottom: 25px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.15);
    position: relative;
    overflow: hidden;
}}

.hero-banner h1 {{
    font-size: 26px;
    font-weight: 900;
    margin: 0 0 8px 0;
    letter-spacing: -0.3px;
    line-height: 1.3;
}}

.hero-banner .subtitle {{
    font-size: 15px;
    opacity: 0.95;
    font-weight: 500;
    margin: 0 0 16px 0;
}}

.hero-badges {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}}

.hero-badge {{
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.35);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 11.5px;
    font-weight: 600;
    backdrop-filter: blur(4px);
}}

.section-block {{
    margin-bottom: 28px;
    page-break-inside: avoid;
}}

h2 {{
    font-size: 18px;
    font-weight: 800;
    color: {theme_color};
    border-bottom: 2.5px solid {theme_color}22;
    padding-bottom: 8px;
    margin-top: 24px;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 10px;
}}

.sec-pill {{
    background: {theme_color};
    color: #ffffff;
    font-size: 12px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 6px;
    display: inline-block;
}}

h3 {{
    font-size: 14.5px;
    font-weight: 700;
    color: #334155;
    margin-top: 16px;
    margin-bottom: 8px;
}}

p {{
    margin: 0 0 10px 0;
}}

ul, ol {{
    margin: 0 0 12px 0;
    padding-{align_prop}: 22px;
}}

li {{
    margin-bottom: 5px;
}}

.card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 14px 0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
}}

.callout {{
    background: #f8fafc;
    border-{border_side}: 4px solid {theme_color};
    border-{border_none}: none;
    padding: 12px 18px;
    border-radius: {border_radius_callout};
    margin: 14px 0;
    font-size: 13px;
}}

.callout.tip {{
    border-color: #10b981;
    background: #f0fdf4;
}}

.callout.warning {{
    border-color: #f59e0b;
    background: #fffbeb;
}}

.callout.trap {{
    border-color: #ef4444;
    background: #fef2f2;
}}

.callout-title {{
    font-weight: 800;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
}}

.callout.tip .callout-title {{ color: #065f46; }}
.callout.warning .callout-title {{ color: #92400e; }}
.callout.trap .callout-title {{ color: #991b1b; }}
.callout:not(.tip):not(.warning):not(.trap) .callout-title {{ color: {theme_color}; }}

table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 16px 0;
    font-size: 12px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    overflow: hidden;
}}

th, td {{
    padding: 9px 12px;
    text-align: {align_prop};
    border-bottom: 1px solid #e2e8f0;
    border-{border_side}: 1px solid #e2e8f0;
}}

th:last-child, td:last-child {{
    border-{border_side}: none;
}}

tr:last-child td {{
    border-bottom: none;
}}

th {{
    background: #f1f5f9;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 2px solid #cbd5e1;
}}

tr:nth-child(even) {{
    background-color: #f8fafc;
}}

.badge {{
    display: inline-block;
    padding: 2px 7px;
    font-size: 11px;
    font-weight: 700;
    border-radius: 4px;
    background: #e2e8f0;
    color: #334155;
}}

.badge-green {{ background: #d1fae5; color: #065f46; }}
.badge-blue {{ background: #dbeafe; color: #1e40af; }}
.badge-amber {{ background: #fef3c7; color: #92400e; }}
.badge-purple {{ background: #ede9fe; color: #5b21b6; }}

.code-box {{
    background: #0f172a;
    color: #f8fafc;
    padding: 12px 16px;
    border-radius: 8px;
    font-family: 'Consolas', monospace;
    font-size: 12px;
    direction: ltr;
    text-align: left;
    margin: 12px 0;
    overflow-x: auto;
    border: 1px solid #334155;
}}

.page-break {{
    page-break-after: always;
}}
"""

print("Defined executive design engine.")
