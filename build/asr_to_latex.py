import sys, re
import numpy as np
from PIL import Image

def classify_color(rgb):
    r,g,b = rgb
    if max(r,g,b)-min(r,g,b) < 25 and r < 210:
        return 'pause'
    if r > 180 and g < 110 and b < 110:
        return 'red'
    if r < 130 and g > 130 and b < 140:
        return 'green'
    if r > 150 and 90 < g < 200 and b < 110:
        return 'orange'
    return 'unknown'

def find_words(img, x0, y0, x1, y1, line_gap=8, word_gap=6):
    a = np.asarray(img.convert('RGB')).astype(int)
    region = a[y0:y1, x0:x1]
    nonwhite = (region.max(axis=2) < 245)
    rows_has = nonwhite.any(axis=1)
    lines = []
    in_line = False
    for i, v in enumerate(rows_has):
        if v and not in_line:
            start = i; in_line = True
        if not v and in_line:
            lines.append((start, i)); in_line = False
    if in_line: lines.append((start, len(rows_has)))
    merged = []
    for s,e in lines:
        if merged and s - merged[-1][1] < line_gap:
            merged[-1] = (merged[-1][0], e)
        else:
            merged.append((s,e))
    results = []
    for (ls, le) in merged:
        band = nonwhite[ls:le]
        cols_has = band.any(axis=0)
        words = []
        in_w = False
        for i, v in enumerate(cols_has):
            if v and not in_w:
                ws = i; in_w = True
            if not v and in_w:
                words.append((ws, i)); in_w = False
        if in_w: words.append((ws, len(cols_has)))
        merged_words = []
        for s,e in words:
            if merged_words and s - merged_words[-1][1] < word_gap:
                merged_words[-1] = (merged_words[-1][0], e)
            else:
                merged_words.append((s,e))
        for (ws,we) in merged_words:
            wregion = region[ls:le, ws:we]
            wmask = (wregion.max(axis=2) < 245)
            pix = wregion[wmask]
            if len(pix) == 0: continue
            avg = pix.mean(axis=0)
            results.append(classify_color(tuple(avg)))
    return results

MACRO = {'green':'sg','orange':'sy','red':'sr'}

def build_latex(colors, words):
    out = []
    wi = 0
    for c in colors:
        if c == 'pause':
            out.append(r'\pse')
        elif c == 'unknown':
            out.append(f'??[{words[wi] if wi<len(words) else "?"}]')
            wi += 1
        else:
            if wi >= len(words):
                out.append(f'EXTRA_COLOR({c})')
                continue
            out.append(f'\\{MACRO[c]}{{{words[wi]}}}')
            wi += 1
    leftover = words[wi:]
    return ' '.join(out), leftover

if __name__ == '__main__':
    fn = sys.argv[1]
    x0,y0,x1,y1 = map(int, sys.argv[2:6])
    text = sys.argv[6]
    words = text.split()
    im = Image.open(fn)
    colors = find_words(im, x0,y0,x1,y1)
    n_pause = colors.count('pause')
    n_unknown = colors.count('unknown')
    n_colored = len(colors) - n_pause
    print(f"# entries={len(colors)} pause={n_pause} unknown={n_unknown} colored_non_unknown={n_colored-n_unknown} words_given={len(words)}", file=sys.stderr)
    latex, leftover = build_latex(colors, words)
    if leftover:
        print(f"# WARNING: {len(leftover)} words not consumed: {leftover}", file=sys.stderr)
    print(latex)
