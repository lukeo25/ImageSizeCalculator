from pathlib import Path

path = Path('video-converter.html')
text = path.read_text(encoding='utf-8')

old = ".grid{display:grid;grid-template-columns:420px 1fr;gap:24px}.panel{border-radius:22px;padding:20px}.g{margin-bottom:20px}.gt{display:block;color:var(--a);font-weight:700;margin-bottom:10px}.fields{display:grid;grid-template-columns:1fr 1fr;gap:10px}.full{grid-column:1/-1}label{font-size:13px;color:var(--m);font-weight:600}input[type=text],select{width:100%;margin-top:5px;padding:10px;border:0;border-radius:12px;background:var(--b);box-shadow:inset 4px 4px 9px var(--sd),inset -4px -4px 9px var(--sl);font:inherit;color:var(--t)}input[type=range]{width:100%;accent-color:var(--c)}.sv{display:flex;justify-content:space-between}.check{display:flex;align-items:center;gap:8px;margin-top:10px}.drop{border:2px dashed #aab5c2;border-radius:18px;padding:28px 18px;text-align:center;cursor:pointer}.drop.drag{border-color:var(--c)}.drop input{display:none}.drop strong{display:block;font-size:18px;margin-bottom:7px}.drop span{color:var(--m);font-size:13px;line-height:1.45}"

new = ".grid{display:grid;grid-template-columns:minmax(360px,420px) minmax(0,1fr);gap:24px;align-items:start}.panel{min-width:0;border-radius:22px;padding:20px}.g{margin-bottom:20px;min-width:0}.gt{display:block;color:var(--a);font-weight:700;margin-bottom:10px}.fields{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:10px}.fields>label{min-width:0}.full{grid-column:1/-1}label{font-size:13px;color:var(--m);font-weight:600}input[type=text],select{width:100%;min-width:0;margin-top:5px;padding:10px;border:0;border-radius:12px;background:var(--b);box-shadow:inset 4px 4px 9px var(--sd),inset -4px -4px 9px var(--sl);font:inherit;color:var(--t)}input[type=range]{width:100%;accent-color:var(--c)}.sv{display:flex;justify-content:space-between}.check{display:flex;align-items:center;gap:8px;margin-top:10px}.drop{display:block;position:relative;width:100%;min-height:118px;border:2px dashed #aab5c2;border-radius:18px;padding:26px 18px;text-align:center;cursor:pointer;overflow:hidden}.drop.drag{border-color:var(--c)}.drop input{display:none}.drop strong{display:block;font-size:18px;line-height:1.25;margin-bottom:8px}.drop span{display:block;color:var(--m);font-size:13px;line-height:1.45}"

if old not in text:
    raise SystemExit('Expected Video Converter CSS block not found; refusing to rewrite file.')

text = text.replace(old, new, 1)
text = text.replace(".previews{display:grid;grid-template-columns:1fr 1fr;gap:18px}", ".previews{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:18px}", 1)
text = text.replace(".box h2{margin:0 0 10px}", ".box{min-width:0}.box h2{margin:0 0 10px}", 1)
path.write_text(text, encoding='utf-8')
