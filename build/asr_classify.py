import sys
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
    return f'unknown({r},{g},{b})'

def find_words(img, x0, y0, x1, y1, line_gap=8, word_gap=6):
    a = np.asarray(img.convert('RGB')).astype(int)
    region = a[y0:y1, x0:x1]
    # non-white mask
    nonwhite = (region.max(axis=2) < 245)
    rows_has = nonwhite.any(axis=1)
    # segment into lines
    lines = []
    in_line = False
    for i, v in enumerate(rows_has):
        if v and not in_line:
            start = i; in_line = True
        if not v and in_line:
            lines.append((start, i)); in_line = False
    if in_line: lines.append((start, len(rows_has)))
    # merge lines separated by very small gaps (accents/descenders)
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
        # merge word fragments separated by small gaps (< word_gap) -> same word (e.g. 'ti' dot separated)
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
            results.append({
                'line': (ls+y0, le+y0), 'x': (ws+x0, we+x0),
                'color': classify_color(avg), 'rgb': tuple(avg.astype(int))
            })
    return results

if __name__ == '__main__':
    fn = sys.argv[1]
    x0,y0,x1,y1 = map(int, sys.argv[2:6])
    im = Image.open(fn)
    res = find_words(im, x0,y0,x1,y1)
    for i,r in enumerate(res):
        print(i, r['color'], r['rgb'], r['line'], r['x'])
