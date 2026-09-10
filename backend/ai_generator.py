import os,re

def clean(text):
    m=re.search(r"```(?:html)?\s*(.*?)```",text,re.I|re.S)
    return m.group(1).strip() if m else text.strip()

def generate_html(prompt):
    key=os.getenv("OPENAI_API_KEY")
    if not key:return demo_html(prompt)
    try:
        from openai import OpenAI
        client=OpenAI(api_key=key)
        instructions=("You are an expert web designer and frontend developer. Generate ONE complete "
        "self-contained HTML document for the user's request. Include CSS and JavaScript inside HTML. "
        "Make it responsive, modern and accessible. Return only HTML, no markdown or explanation.")
        response=client.responses.create(model=os.getenv("OPENAI_MODEL","gpt-5"),instructions=instructions,input=prompt)
        return clean(response.output_text)
    except Exception as e: raise RuntimeError("AI generation failed: "+str(e))

def demo_html(prompt):
    safe=prompt.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Generated Website</title><style>
*{{box-sizing:border-box}}body{{margin:0;font-family:Arial;color:#172033}}nav{{padding:20px 7%;display:flex;justify-content:space-between;border-bottom:1px solid #eee}}
nav a{{margin-left:20px;color:#172033;text-decoration:none}}.hero{{padding:110px 7%;text-align:center;background:#eef4ff}}
h1{{font-size:clamp(42px,7vw,76px);margin:0 auto 20px;max-width:900px}}.hero p{{font-size:20px;max-width:720px;margin:0 auto 30px;line-height:1.6}}
.btn{{display:inline-block;padding:14px 22px;border-radius:9px;background:#2563eb;color:#fff;text-decoration:none;font-weight:bold}}
section{{padding:75px 7%}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}.card{{padding:28px;border:1px solid #e4e8ef;border-radius:16px}}
footer{{padding:35px 7%;background:#111827;color:#fff}}@media(max-width:800px){{.grid{{grid-template-columns:1fr}}}}
</style></head><body><nav><strong>AI Website</strong><div><a href="#home">Home</a><a href="#services">Services</a><a href="#contact">Contact</a></div></nav>
<div class="hero" id="home"><h1>Your AI-Generated Website</h1><p>Built from your idea: {safe}</p><a class="btn" href="#contact">Get Started</a></div>
<section id="services"><h2>What we offer</h2><div class="grid"><div class="card"><h3>Professional Design</h3><p>Modern responsive layouts.</p></div>
<div class="card"><h3>Fast & Responsive</h3><p>Works on phones, tablets and desktops.</p></div><div class="card"><h3>AI Powered</h3><p>Turn your idea into a website.</p></div></div></section>
<section id="contact"><h2>Let's build something great</h2><p>Replace this demo content with your business information.</p></section><footer>© 2026 AI Website Builder</footer></body></html>'''
