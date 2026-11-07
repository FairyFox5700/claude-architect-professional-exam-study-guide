import base64, markdown, os, re, json

ROOT = os.path.dirname(os.path.abspath(__file__))
HTML_OUT = os.path.join(ROOT, "_pdf_build_html")
os.makedirs(HTML_OUT, exist_ok=True)

FONT_PATH = os.path.join(ROOT, "assets", "fonts", "Manrope-Variable.woff2")
with open(FONT_PATH, "rb") as f:
    MANROPE_BASE64 = base64.b64encode(f.read()).decode("ascii")

# Font is embedded as a base64 data URI so rendering never depends on a
# network fetch (this is what caused inconsistent/fallback-font readability
# issues before). It's a variable font, so one @font-face covers the whole
# 400-800 weight range used across the page.
FONT_FACE = f"""
@font-face {{
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 400 800;
  font-display: block;
  src: url(data:font/woff2;base64,{MANROPE_BASE64}) format('woff2-variations');
}}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
__FONT_FACE__
  :root {{
    --navy: #1B2A6B;
    --orange: #E87A2D;
    --peach: #FFE8E0;
    --slate: #24304F;
    --muted: #434E68;
    --green: #2F9E58;
    --green-bg: #EAF7EE;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: 'Manrope', Arial, sans-serif;
    color: var(--slate);
    margin: 0;
    padding: 36px 48px 56px 48px;
    font-size: 12pt;
    font-weight: 500;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }}
  .eyebrow {{
    display: inline-block;
    background: var(--peach);
    color: var(--navy);
    font-weight: 700;
    font-size: 10pt;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 999px;
    margin-bottom: 14px;
  }}
  h1 {{
    color: var(--navy);
    font-size: 22pt;
    font-weight: 800;
    margin: 0 0 4px 0;
    line-height: 1.25;
  }}
  .subtitle {{
    color: var(--muted);
    font-size: 11pt;
    margin: 0 0 20px 0;
  }}
  blockquote {{
    background: #F7F8FC;
    border-left: 4px solid var(--orange);
    margin: 0 0 18px 0;
    padding: 10px 16px;
    color: var(--slate);
    font-size: 11.5pt;
    font-weight: 500;
    border-radius: 0 6px 6px 0;
  }}
  h2 {{
    color: var(--navy);
    font-size: 15pt;
    font-weight: 800;
    margin: 24px 0 12px 0;
    border-bottom: 2px solid var(--peach);
    padding-bottom: 6px;
  }}
  p {{ margin: 6px 0; }}
  ul.plain, ol {{ margin: 6px 0; padding-left: 22px; }}
  ul.plain li {{ margin: 2px 0; }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 18px 0;
    font-size: 10pt;
  }}
  th {{
    background: var(--navy);
    color: #fff;
    text-align: left;
    padding: 6px 8px;
  }}
  td {{
    border-bottom: 1px solid #E5E8F0;
    padding: 6px 8px;
    vertical-align: top;
  }}
  strong {{ color: var(--navy); }}
  a {{ color: var(--orange); text-decoration: none; }}
  hr {{
    border: none;
    border-top: 2px solid var(--peach);
    margin: 20px 0;
  }}
  code {{
    background: #F0F1F6;
    padding: 1px 5px;
    border-radius: 4px;
    font-size: 10pt;
  }}

  /* ---- Question cards ---- */
  .qcard {{
    page-break-inside: avoid;
    margin: 0 0 16px 0;
    border: 1px solid #E3E6F0;
    border-radius: 10px;
    overflow: hidden;
    background: #FCFCFE;
  }}
  .qhead {{
    display: flex;
    gap: 10px;
    align-items: flex-start;
    background: var(--navy);
    color: #fff;
    padding: 8px 14px;
  }}
  .qnum {{
    flex-shrink: 0;
    background: var(--orange);
    color: #fff;
    font-weight: 800;
    font-size: 10pt;
    padding: 3px 10px;
    border-radius: 999px;
    letter-spacing: 0.02em;
  }}
  .qtext {{
    font-weight: 700;
    font-size: 12pt;
    color: #fff;
    line-height: 1.45;
  }}
  .options {{
    list-style: none;
    margin: 0;
    padding: 10px 14px 4px 14px;
  }}
  .options li {{
    display: flex;
    gap: 8px;
    align-items: flex-start;
    margin: 6px 0;
    font-size: 11pt;
    font-weight: 500;
    padding: 5px 8px;
    border-radius: 6px;
  }}
  .options li.correct {{
    background: var(--green-bg);
  }}
  .optletter {{
    flex-shrink: 0;
    background: #EEF0F8;
    color: var(--navy);
    font-weight: 800;
    border-radius: 50%;
    width: 19px;
    height: 19px;
    min-width: 19px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 9pt;
  }}
  .options li.correct .optletter {{
    background: var(--green);
    color: #fff;
  }}
  .opttext {{ padding-top: 1px; }}
  .options li.correct .opttext {{ font-weight: 700; color: var(--slate); }}
  .answerbox {{
    margin: 8px 14px 14px 14px;
    background: #FFF4EC;
    border-left: 4px solid var(--orange);
    border-radius: 0 8px 8px 0;
    padding: 9px 13px;
  }}
  .answer-line {{
    font-weight: 800;
    color: var(--green);
    font-size: 11.5pt;
    margin-bottom: 6px;
  }}
  .answer-line .tag {{
    display: inline-block;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: 8.5pt;
    font-weight: 800;
    color: #fff;
    background: var(--green);
    border-radius: 4px;
    padding: 2px 7px;
    margin-right: 8px;
  }}
  .explanation {{
    color: var(--muted);
    font-size: 10.8pt;
    font-weight: 500;
    line-height: 1.5;
  }}
  .explanation .tag {{
    display: inline-block;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: 8.5pt;
    font-weight: 800;
    color: var(--navy);
    background: var(--peach);
    border-radius: 4px;
    padding: 2px 7px;
    margin-right: 8px;
  }}
</style>
</head>
<body>
<div class="eyebrow">Claude Certified Architect &mdash; Professional</div>
{body}
</body>
</html>
"""


def inline_md(text):
    """Render inline markdown (bold, code, links) and strip the wrapping <p> tag."""
    text = text.strip()
    if not text:
        return ""
    html = markdown.markdown(text, extensions=["fenced_code"])
    html = re.sub(r"^<p>(.*)</p>$", r"\1", html.strip(), flags=re.DOTALL)
    return html


def parse_questions(body_text):
    """Split a page body into the intro (title/blockquote/table) and a list of
    parsed question dicts, rendering each question as a styled card."""
    parts = re.split(r"\n(?=###\s+Q\d+\.)", body_text)
    pre = parts[0]
    q_blocks = parts[1:]

    questions = []
    for block in q_blocks:
        m = re.match(r"###\s+Q(\d+)\.?\s*\n(.*)", block, re.DOTALL)
        if not m:
            continue
        qnum = m.group(1)
        rest = m.group(2)

        ans_m = re.search(r"\*\*Answer:\*\*\s*([A-D])", rest)
        exp_m = re.search(r"\*\*Explanation:\*\*\s*(.+?)(?:\n###\s+Q\d+\.|\Z)", rest, re.DOTALL)

        answer_letter = ans_m.group(1) if ans_m else "?"
        explanation_raw = exp_m.group(1).strip() if exp_m else ""
        explanation_raw = re.sub(r"\n+", " ", explanation_raw).strip()

        qa_text = rest[: ans_m.start()] if ans_m else rest
        opt_matches = re.findall(r"^([A-D])\.\s*(.+)$", qa_text, re.MULTILINE)
        question_text_raw = re.sub(r"^[A-D]\.\s*.+$", "", qa_text, flags=re.MULTILINE).strip()
        question_text_raw = re.sub(r"\n+", " ", question_text_raw).strip()

        questions.append({
            "num": qnum,
            "question": inline_md(question_text_raw),
            "options": [(letter, inline_md(text)) for letter, text in opt_matches],
            "answer": answer_letter,
            "explanation": inline_md(explanation_raw),
        })
    return pre, questions


def render_question_card(q):
    opts_html = ""
    for letter, text in q["options"]:
        correct = "correct" if letter == q["answer"] else ""
        opts_html += (
            f'<li class="{correct}">'
            f'<span class="optletter">{letter}</span>'
            f'<span class="opttext">{text}</span></li>'
        )
    return f"""
    <div class="qcard">
      <div class="qhead"><span class="qnum">Q{q['num']}</span><div class="qtext">{q['question']}</div></div>
      <ul class="options">{opts_html}</ul>
      <div class="answerbox">
        <div class="answer-line"><span class="tag">Correct answer</span>{q['answer']}</div>
        <div class="explanation"><span class="tag">Why</span>{q['explanation']}</div>
      </div>
    </div>
    """


def md_to_html(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    raw_title = m.group(1).strip() if m else os.path.basename(md_path)

    # strip nav link lines so they don't clutter the PDF
    text = re.sub(r"^\[.*Back to.*\].*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\[.*Next:.*\].*$", "", text, flags=re.MULTILINE)

    pre_text, questions = parse_questions(text)

    pre_html = markdown.markdown(pre_text, extensions=["tables", "fenced_code"])
    pre_html = pre_html.replace("<ul>", '<ul class="plain">')

    if questions:
        body = pre_html + "".join(render_question_card(q) for q in questions)
    else:
        body = pre_html

    return raw_title, body


def build(md_path, html_path):
    title, body = md_to_html(md_path)
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    html = TEMPLATE.format(title=title, body=body)
    html = html.replace("__FONT_FACE__", FONT_FACE)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    manifest = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if "_pdf_build_html" in dirpath or ".git" in dirpath:
            continue
        for fn in filenames:
            if fn.lower().endswith(".md"):
                src = os.path.join(dirpath, fn)
                rel = os.path.relpath(src, ROOT)
                rel_html = os.path.splitext(rel)[0] + ".html"
                rel_pdf = os.path.splitext(rel)[0] + ".pdf"
                html_path = os.path.join(HTML_OUT, rel_html)
                build(src, html_path)
                manifest.append({
                    "html": html_path,
                    "pdf": os.path.join(ROOT, "pdf", rel_pdf),
                })
    with open(os.path.join(ROOT, "_pdf_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Built {len(manifest)} HTML files. Manifest written.")


if __name__ == "__main__":
    main()

