# PTE 模考长图 → 逐题裁剪 · 交接文档 (SOP)

> 收到这份文档的会话请注意：你会拿到 **APEUni PTE 学术类模考**的整页长截图（每个部分一张长图）。
> 你的任务：把每张长图**逐题裁剪**成单独图片（**每题都要带答案/评分**），供 **PTE Core** 刷题用。
> 这份文档给你完整的**方法、脚本、命名规范、和踩过的坑**。照着做即可复现，无需从零摸索。
>
> **English:** You are receiving full-page screenshots of APEUni PTE Academic mock exams. Slice each into
> one image per question (each **including its answer/feedback**), organized for **PTE Core** practice.
> This doc gives you the exact method, ready-to-run scripts, naming conventions, and the pitfalls already found.
>
> **⚠️ 裁剪范围以用户当次说的为准 / Scope is whatever the user says THIS TIME：** 下面 §2 的表格记录的是
> **某一次**的取舍（口语只留 DI）。这不是死规则——后来有一轮用户明确说"这次是完整卷子，所有题型都要裁"，
> 于是口语的 RA/RS/RTS/ASQ 和写作 SWT/WE 也全裁了（见 §11）。**每次开工前先确认用户这次要不要"全裁"**，
> 不要预设上一轮的范围就是这一轮的范围。

---

## 0. 一句话总则 / TL;DR

- **听力(Listening) + 阅读(Reading)：每一道题都裁。**
- **口语(Speaking)：默认只裁 DI（Describe Image / 看图说话）**，其它口语题型（RS/RL/ASQ/SGD/RA…）默认**不裁**——
  **除非用户这次说了要全部裁**（见上方⚠️ 和 §11）。
- **写作(Writing)：默认不在范围内**，除非用户这次明确要（见 §11）。
- 每张裁剪图 = 从**题号标题**（例：`11. HIW #216 T Cell`）裁到该题的**评分行**（例：`评分详情 x/x分 … 答题用时 xx:xx`）。
- **去掉**：页脚、翻页条、盖在题上的站点顶部导航条、右侧浮动按钮。
- **绝不编造**：被导航条挡住、图里看不到的内容，**不要脑补**，加提示条标注并记录到「已知缺口」。

---

## 1. 背景 / Context

APEUni 模考成绩页（`答案 & 评分详情`）里，每个部分（口语/写作/阅读/听力）是**一张很长的截图**，一张图里**有很多道题**，每题结构大致是：

```
N. 题型 #题库编号 标题                                    查看原题 >
[音频播放器 / 图表 / 图片 / 文章正文]
Question: …            Choices: …            答案：…            你的答案：…
(题型标签)  (评分详情 x/x分)  (查看翻译)   答题用时 xx:xx           分享
──────────────── 下一题 ────────────────
```

同一部分题目多时会分页 → 你可能拿到 `听力1.jpeg`、`听力2.jpeg` 两张甚至更多，**题号要跨图连续**（第 1 张是 1–10，第 2 张接着 11–15…）。

**有些批次还会额外给你几个 `.docx` 文件**（如 `听力.docx`/`口语.docx`/`写作.docx`），里面塞的是**单独截的「AI 评分」弹窗图**（每张图是一次浏览器截图，弹窗浮在灰色蒙层上）。这是因为长截图里这些题只显示了精简的评分胶囊（`评分详情 x/x分`），点开弹窗才能看到 Content/Pronunciation/Fluency 细分和逐词颜色标注/语法批改，需要单独处理，见 §11。

---

## 2. PTE 题型速查表（决定裁不裁）/ Question-type taxonomy

平台标题里的**题型代码**决定它属于哪个部分。**按下表判断该不该裁**：

> **范围说明 / Scope note：** 这些图是 **PTE 学术类(Academic)** 的模考。用户实际考的是 **PTE Core**。下表「裁不裁」
> 是**某一次**任务的取舍（口语只留 DI，写作不裁）——**不是通用规则**。**如果用户说这次要全裁**（完整卷子/所有题型），
> 就按 §11 的方法把 RA/RS/RTS/ASQ/SWT/WE 等也全部裁出来。**永远以用户当次最新说的为准。**

| 代码 | 全称 | 所属部分 | 默认裁不裁（除非用户说全裁）|
|---|---|---|---|
| DI | Describe Image 看图说话 | Speaking | ✅ 默认就裁 |
| RS | Repeat Sentence | Speaking | ❌ 默认跳过，用户要求全裁时裁 |
| RA | Read Aloud | Speaking | ❌ 默认跳过，用户要求全裁时裁 |
| RL | Retell Lecture | Speaking | ❌ 默认跳过，用户要求全裁时裁 |
| ASQ | Answer Short Question | Speaking | ❌ 默认跳过，用户要求全裁时裁 |
| SGD / RTS (C) | Respond to a Situation | Speaking | ❌ 默认跳过，用户要求全裁时裁 |
| SWT (C) | Summarize Written Text | Writing | ❌ 默认不在范围，用户要求时裁 |
| WE (C) | Write Essay | Writing | ❌ 默认不在范围，用户要求时裁 |
| FIB (R&W) | Reading & Writing: Fill in the Blanks | Reading | ✅ 裁 |
| FIBD&D / FIB(R) | Reading: Fill in Blanks (拖拽) | Reading | ✅ 裁 |
| MCM-R | Multiple-choice, Multiple-answer (Reading) | Reading | ✅ 裁 |
| MCS-R | Multiple-choice, Single-answer (Reading) | Reading | ✅ 裁 |
| RO | Re-order Paragraphs | Reading | ✅ 裁 |
| SST (C) | Summarize Spoken Text | Listening | ✅ 裁 |
| FIB-L | Listening: Fill in the Blanks | Listening | ✅ 裁 |
| HCS | Highlight Correct Summary | Listening | ✅ 裁 |
| MCM-L / MCS-L | Multiple-choice (Listening) | Listening | ✅ 裁 |
| SMW | Select Missing Word | Listening | ✅ 裁 |
| HIW | Highlight Incorrect Words | Listening | ✅ 裁 |
| WFD | Write From Dictation | Listening | ✅ 裁 |

> 标题里带 `(C)` 后缀（如 `SST (C)`、`RTS (C)`、`SWT (C)`、`WE (C)`）是**平台自己标的**，表示这题是按 **PTE Core**
> 版本的题型/评分规则出的——Academic 模考里混入的 Core 专项题，直接保留这个标记即可，不用管它，正常裁。

---

## 3. 交付物结构 & 命名 / Output layout & naming

**两个顶层文件夹**（原图一个、成品一个；成品下再按部分分子文件夹）：

```
original_screenshots/                 # 原始整页长图 + docx，原封不动，只搬进来
    听力1.jpeg 听力2.jpeg 阅读1.jpeg 阅读2.jpeg 口语2.jpeg 口语3.jpeg  SST.png …
    (若有) 听力.docx 口语.docx 写作.docx   ← AI 评分弹窗图的来源，见 §11

cropped_questions/                    # 逐题裁剪成品（要交付的）
    listening/    L01_… L02_… …       # 听力：每题一张（题号跨图连续）
    reading/      R01_… R02_… …       # 阅读：每题一张
    speaking_DI/  DI01_… DI02_… …     # 口语只留 DI 时用这个文件夹名
    speaking/     S01_… S02_… …       # 口语全裁时用这个文件夹名（见 §11）
    writing/      W01_… W02_… …       # 写作全裁时用这个文件夹名（见 §11）
```

**命名规则：** `前缀+序号[b]_题型_题库编号_标题.png`

- 前缀：听力 `L`、阅读 `R`；口语——只裁 DI 时用 `DI`，全裁时统一用 `S`（题型仍写在文件名里，如 `S01_RA_771_…`）；写作 `W`。
- 序号：**两位补零**，跨图连续（`L01`…`L15`）。
- 题型/编号/标题：来自标题行（`11. HIW #216 T Cell` → `L11_HIW_216_T_Cell`）。
- 标题里空格→`_`；去掉 `#`；`&` 去掉或写成词（`FIBD&D`→`FIBDD`）；`(C)` 后缀写成 `-C`（`RTS (C)`→`RTS-C`）；
  撇号直接删掉（`Year's`→`Years`）；文件名只留 `A-Za-z0-9-_`。
- 没有独立标题的（如 `WFD #3208 WFD`、`RS #1637 RS`、`ASQ #1391 ASQ`）就省略标题：`L13_WFD_3208.png`。
- **`b` 后缀**：该题的补充「AI 评分详情」弹窗截图（来自 docx，见 §11），紧跟主图之后，如 `S01b_RA_771_….png`。

例：`L07_HCS_81_What_Democracy_Breeds.png`、`R05_FIB_1040_Drought-resistant_Crops.png`、`DI04_949_Crop_Distribution.png`、
`S19_DI_696_Trailing_Sails.png` + `S19b_DI_696_Trailing_Sails.png`（弹窗）。

---

## 4. 环境准备 / Tooling（一次性）

```bash
pip install --quiet Pillow numpy scipy      # scipy 在 §11 弹窗裁剪时会用到
apt-get install -y tesseract-ocr          # OCR，用来自动定位每题的题号
python3 -c "import docx"                  # 如果批次给了 .docx，装 python-docx 读取/解压里面的截图
pip install --quiet python-docx
# 中文提示条要用到 CJK 字体（多数环境自带）：
fc-list :lang=zh | head           # 找到类似 /usr/share/fonts/truetype/wqy/wqy-zenhei.ttc 即可
```

---

## 5. 核心方法（照顺序做）/ The pipeline

裁剪的难点只有一个：**精确找到每题的上下边界**。用 **OCR 定位题号** 解决竖直边界，用**固定内容列**解决水平边界。

### 步骤 A — 看每张图的尺寸
```python
from PIL import Image
for f in ['听力1.jpeg', ...]:
    print(f, Image.open(f).size)   # 例：2372 x 11049
```

### 步骤 B — OCR 定位每题题号（得到每题的顶端 Y）
把每张长图 OCR 成 TSV，抓出「以数字开头 + 靠左 + 含题型代码/`#`」的行，就是题号行。

```python
# detect_headers.py  ——  用法: python3 detect_headers.py 听力1.jpeg 听力2.jpeg ...
import csv, re, subprocess, sys
from collections import defaultdict
TYPES=r'(SST|MCM|MCS|HCS|FIB|HIW|WFD|SMW|RS|DI|RA|RL|RTS|ASQ|RO|SGD|SWT|FIBD)'
def headers(fn):
    base='/tmp/hdr_'+re.sub(r'\W','',fn)
    subprocess.run(['tesseract',fn,base,'tsv'],stderr=subprocess.DEVNULL)
    rows=list(csv.DictReader(open(base+'.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE))
    lines=defaultdict(list)
    for r in rows:
        if r.get('level')=='5' and r['text'].strip():
            lines[(r['block_num'],r['par_num'],r['line_num'])].append(r)
    out=[]
    for ws in lines.values():
        ws=sorted(ws,key=lambda w:int(w['left'])); text=' '.join(w['text'] for w in ws)
        top=min(int(w['top']) for w in ws); first=ws[0]['text'].strip(); left=int(ws[0]['left'])
        m=re.match(r'^(\d{1,2})[.,]?$',first)
        if m and 750<=left<=1050:                        # 靠左的题号列（比旧版更宽，兼容不同缩放）
            num=int(m.group(1))
            if 1<=num<=60 and (re.search(TYPES,text) or '#' in text):
                out.append((top,num,text[:80]))
    out.sort(); seen=set(); final=[]
    for top,num,text in out:
        if num in seen: continue
        seen.add(num); final.append((top,num,text))
    return final
for fn in sys.argv[1:]:
    print(f'== {fn} =='); [print(f'  y={t:6d} #{n:2d} {tx}') for t,n,tx in headers(fn)]
```
> ⚠️ OCR 会把 `11.` 读成 `11,`、把标题读花（`T Cell Bane >`）。**题号(数字)基本准，标题要人工核对**。用 y 值定边界，用眼睛核对标题拼写。

**核对技巧**：与其一张一张开原图核对标题，不如把每题标题行切一条窄图（`[y-15, y+75]` 高、内容列宽）、**同一张源图的所有题目纵向拼成一张 montage**，一次看完一整页的标题，效率高很多（§8 也用同样思路做 contact sheet）。

**竖直边界间距异常 ≠ 漏检**：有的题（尤其带很长「解析」的 FIB/FIBD&D）会比同类型其它题占用多 2倍以上的高度，纯属内容长，**先目视确认再下结论**，不要假设是 OCR 漏掉了一道题。

### 步骤 B2 — 把 OCR 结果拼成 MANIFEST（关键衔接）
步骤 B 每题给你一行 `y=… #编号 11. HIW #216 T Cell Bane >`。把它解析成生成脚本要的元组 `(序号, 题型, 编号, 标题, 题号Y)`：
```python
import re
def parse_header(num, y, text):
    # text 形如 "11. HIW #216 T Cell Bane >"，尾部常是 OCR 读花的「查看原题 >」
    m=re.search(r'#\s*(\d+)\s+(.*)$', text)               # 抓 #编号 及其后的标题
    m2=re.search(r'\b([A-Z][A-Za-z-]*(?:-[A-Z])?)\s*#', text)  # 抓 # 前的题型代码
    typ=m2.group(1) if m2 else '?'
    qid=m.group(1) if m else '?'
    title=(m.group(2) if m else '').strip()
    title=re.sub(r'\s*[>》].*$','',title)                  # 去掉尾部 OCR 垃圾
    # 若标题==题型(如 "WFD #3208 WFD") 视为无标题
    if title.upper()==typ.upper(): title=''
    return (num, typ, qid, title, y)
# 打印出来，人工核对拼写(尤其人名/术语)，再粘进生成脚本的 MANIFEST
```
**必须人工核对**：自动解析出的标题**经常带 OCR 尾巴**（例：`T Cell Bane`、`Time Famine SaRE`——那串乱码是读花的「查看原题」），需手动删成 `T Cell`、`Time Famine`；无标题的（`WFD #3208 WFD`）留空。题型/编号偶尔也会读错，一并核对。核对无误后再固化进 MANIFEST。

**特殊情况：**
- **OCR 漏检某题的题号**（少见）：从相邻两题的 y 之间估一个值，或用图片查看器量出该题标题的 y，手动补进 MANIFEST。宁可手补，也别漏题。
- **一个部分分 3 张以上图**：`MANIFEST` 里把 3 张都列上，**题号继续往后编**（第 3 张接着第 2 张，别从 1 重来）。
- **题号跨图**：每张图内部用「下一题题号Y」定下边界；**每张图的最后一题**用 `compute_end`（步骤 D）。

### 步骤 C — 水平内容列（X 范围）
APEUni 页面内容居中在一列里，但**具体像素值每套图都可能不同**（同样 2372 宽的图，这套实测内容是
`X=[808,1995]`，上一套是 `[835,1912]`——**别照抄数值，每次重新量**）：

```python
# 用列密度找左右边界：真正内容起止处密度会从~0跳到两位数以上；
# 卡片外框线（左右各一条 100% 高的竖线）密度是 100%，要排除在内容之外。
import numpy as np
from PIL import Image
a = np.asarray(Image.open('听力1.jpeg').convert('RGB'))
band = a[1200:12000]                     # 挑一段跳过页头页脚的内容区
col = (band.min(axis=2)<245).sum(axis=0)
H = band.shape[0]
for x in range(700, 2100):
    pct = col[x]/H*100
    if 1 < pct < 99:                      # 排除0%(空白)和100%(卡片边框线)
        print(x, f'{pct:.1f}%')           # 第一个/最后一个出现的 x 附近就是内容真实边界
```

### 步骤 D — 竖直边界
- **上边界** = `题号Y − 26`（留点头顶空白，别切到标题）。
- **下边界（非本图最后一题）** = `下一题题号Y − 24`（含完本题评分行，停在下一题之前）。
- **下边界（本图最后一题）** = 用「评分行」定位，**排除翻页条和页脚**。
  评分行左侧永远有个 **青色 `评分详情` 胶囊**；取页脚之前**最后一处青色胶囊**的 Y，+48 即可。

```python
def compute_end(a, start):        # a=整张图ndarray, start=最后一题题号Y
    H=a.shape[0]; sub=a[start:H].astype(int)
    R,G,B=sub[:,:,0],sub[:,:,1],sub[:,:,2]
    dark=(sub.max(axis=2)<90).mean(axis=1)
    # ⚠️ 见 §6.9：不能只看单行 dark>0.4 就判定页脚起点，必须要求「持续变暗」
    # （真页脚是几百像素高的实心块；DI 图表的黑色外框只有 1~2 行，会被误判）
    n=len(dark); win=40
    csum=np.cumsum(np.insert(dark,0,0.0)); footer=n
    for i in range(n-win):
        if dark[i]>0.4 and (csum[i+win]-csum[i])/win>0.4:
            footer=i; break
    teal=(G>140)&(R<130)&(B>120)&(G-R>45)                                  # 青色胶囊
    z=teal[:footer, XL:XL+180].sum(axis=1)                              # 只看最左侧(评分详情胶囊)
    rows=np.where(z>6)[0]
    return start + (int(rows[-1])+48 if len(rows) else footer-30)
```
> 为什么不用「最后一块内容」：**翻页条(`< 1 2 >`)是居中的**，会被当成最后一块而误留；页脚是深色全宽。用「最左侧青色胶囊」这个语义锚点最稳。

### 步骤 E — 去站点顶部导航条（**最重要的坑，见 §6.1**）
整页截图里**有时**会夹着一条站点导航条（`课程 社区 APP 机构版 留学 … 考试报名优惠¥2089 … PTE Core` + 大猩猩头像），
出现在**截图时的滚动位置**。**但不是每套图都会撞见这个问题**——本 SOP 附带的两套参考实现里，一套确实撞上了
（R01/R14），另一套逐张检查后确认**完全没有**导航条压内容的情况。**不要预设一定有问题，也不要预设一定没问题，
两种可能都要用下面的方法实测排查。**

**检测**（它有个独特特征：**内容伸进左边距 `x<815`**，而正常题目内容从 `x≈835` 才开始；且整行**偏白**、不是深色页脚）。
> 这个函数是**发现工具**，不是终判：它返回**所有候选带**（可能既有图片最顶部的站点头，也有中间那条真正的导航条）。**你必须把候选带在蒙太奇上肉眼确认**，挑出真正压在题目区的那条，**再把它的 (y0,y1) 硬编码进生成脚本的 `NAV`**（§7）。别让脚本盲涂。
```python
def navbar_candidates(a):          # 返回候选带 [(y0,y1), ...]，每条已上下放宽
    W=a.shape[1]; nw=(a.min(axis=2)<220); dark=(a.max(axis=2)<90)
    leftmargin=nw[:,430:815].sum(axis=1); frac=nw.sum(axis=1)/W; dk=dark.sum(axis=1)/W
    m=(leftmargin>35)&(frac<0.45)&(dk<0.10)
    rows=np.where(m)[0]
    if not len(rows): return []
    # 把匹配行按间隔>60聚成若干段（避免把顶部站点头和中间导航条并成一大段）
    bands=[]; s=p=int(rows[0])
    for r in rows[1:]:
        r=int(r)
        if r-p>60: bands.append((s,p)); s=r
        p=r
    bands.append((s,p))
    # 每段上下放宽以盖全胶囊/头像；很矮的噪声段(<15px)丢掉
    return [(a0-40, b0+45) for a0,b0 in bands if b0-a0>=15]
```
**处理**：**先肉眼确认每条候选带压在哪**（做一张对比蒙太奇，见下），再决定：
- 压在**空白/间隙**上 → 直接涂白：`a[y0:y1, 830:1917] = 255`（背景本就是白，无缝）。
- 压在**真正的题目内容**上（选项、正文…）→ **原图里这段内容已经丢了**，涂白也救不回。**此时不要静默涂白**，要按 §6.1 加**提示条**并记录到「已知缺口」。
- 图片**最顶部**的站点头（题目开始前）→ 一般不落在任何一题的裁剪范围里，忽略即可。

```python
# 蒙太奇：把每张图疑似导航条位置切一条 170px 高的带子，竖排出来一次看清
import numpy as np
slices=[('听力1.jpeg',1080,1250), ...]  # 用步骤B的y推断导航条大概位置
imgs=[]; sep=np.full((6,1070,3),255,np.uint8)
for fn,a0,b0 in slices:
    imgs.append(np.asarray(Image.open(fn).convert('RGB'))[a0:b0,835:1905]); imgs.append(sep.copy())
Image.fromarray(np.vstack(imgs)).save('/tmp/navbar_montage.png')   # 然后打开看
```

**如何确认「这套图完全没有导航条撞内容」**：对每张源图，在 `x=430:815` 这个左边距做「非背景色」扫描（见步骤E的
`navbar_candidates`），**同时**在 `x>1995`（内容区右边界之外）也扫一遍非白像素。如果所有命中的行都在题1开始之前
（页头区）或题末评分行之后（页脚区），且候选带经蒙太奇肉眼确认都是无害的（卡片分割线、图表图例颜色块误触发等），
就可以下结论「这一批没有导航条覆盖问题」，写进交付 README，不用为每题加提示条。

### 步骤 F — 去右侧浮动按钮（`预约老师分析` 之类）
右侧有个浮动圆/胶囊按钮，也只在某个 Y 出现一次，会在裁剪右缘留一小条。检测后**只涂右缘那一小条**（注意别涂到正文文字）：
```python
def floatbtn_bands(a):            # 返回若干 (y0,y1)
    mx=a.max(axis=2); mn=a.min(axis=2); sat=(mx-mn>60)&(mx>120)   # 饱和色块
    z=sat[:,1915:2110].sum(axis=1); rows=np.where(z>18)[0]
    bands=[]; 
    if len(rows):
        s=p=rows[0]
        for r in rows[1:]:
            if r-p>70: bands.append((s,p)); s=r
            p=r
        bands.append((s,p))
    return [(a0,b0) for a0,b0 in bands if b0-a0>=60]
# 涂：a[y0:y1, 1892:1917]=255  （若该 Y 右侧是正文文字，改成更靠右或跳过，别切字）
```
> ⚠️ 这个「饱和色块」检测容易在**题目正文本身有彩色标注**时误报（打勾/叉/高亮词的颜色也是「饱和色」）。
> 命中后一定要肉眼看一眼那个位置的原图，确认是不是真的浮动按钮，而不是正文里的彩色答案标注。

### 步骤 G — SST / 弹窗类评分详情（单题弹窗，非批量）
若单独截了**某一道**题的「AI 评分」弹窗（白色对话框浮在灰底上），把**白色对话框**裁出来即可（去掉左右灰底），命名挂到对应题：`L01b_SST_712_AI_scoring_detail.png`。**如果是一整批题目都有弹窗**（docx 里几十张图那种），用 §11 的批量方法，不要一张张手工来。

### 步骤 H — 生成 + 质检
把上面拼成一个生成脚本（见 §7 的 `crop_all.py` 模板），跑完后**务必做一张 contact sheet 逐张核对边界**（§8）。

---

## 6. 已知陷阱清单 / Pitfalls（务必逐条自查）

### 6.1 站点导航条压住真内容 → 内容已丢，**不许脑补** ⭐最关键
某一套图里出现过两处（供你识别同类情况；**不代表每套图都会遇到**，见步骤E最后一段「如何确认完全没有」）：
- **R01 (FIB #1076)**：导航条正好压住 Choices 的**第 3/4/5 行干扰项列表**。正确答案在正文里内嵌可见（`has shed / commitment / urgency`），但**干扰项彻底没了**。
- **R14 (MCS-R #45)**：导航条压住**选项 A 整行**（而 A 恰是正确答案）。B/C/D 可见。

**正确处理**：涂掉导航条后，在原位画一条**黄色提示条**，写清「**哪里被挡 + 已知的正确答案 + 去平台『查看原题』补全**」，并在 README 记一笔。示例代码：
```python
from PIL import ImageDraw, ImageFont
FONT='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
f=ImageFont.truetype(FONT,29)
def banner(im, x0,y0,x1,y1, lines):     # lines=[(文字,颜色), ...]
    d=ImageDraw.Draw(im); d.rectangle([x0,y0,x1,y1], fill=(255,247,220), outline=(224,170,60), width=3)
    cy=y0+16
    for txt,color in lines: d.text((x0+22,cy),txt,font=f,fill=color); cy+=41
```
> ⚠️ **绝对不要**用记忆/训练数据去补选项文字——可能和平台版本不符，会误导备考。只标注、只写已知正确答案，剩下交给手上有平台的人抄。

### 6.2 翻页条 `< 1 2 >`
每页最后一题下面有居中的翻页条，**不要裁进去**。用 §5-D 的青色胶囊锚点自然排除。

### 6.3 深色页脚
页面底部深色页脚，别裁进去。`dark>0.4` 检测其起点，但见 §6.9——**必须要求持续变暗**，别被一行黑线骗过。

### 6.4 右侧浮动按钮
见 §5-F。

### 6.5 OCR 误读
`11.`→`11,`，标题读花。**题号数字可信，标题人工核对拼写**（尤其人名/术语，如 `Momaday`）。

### 6.6 缩放/分辨率不同
若新图不是之前那批的宽度，或宽度一样但版式不同，`X` 范围、各种阈值要按 §5-C 的方法重测。**别照抄像素值，照抄方法。**

### 6.7 跨图题号连续
一个部分分多张图时，第 2 张接着第 1 张的题号编号（不要每张都从 1 开始）。

### 6.8 口语/写作范围以用户当次说的为准
见文档开头的⚠️和 §2：默认口语只留 DI、写作不裁，**但用户说这次要全裁就全裁**（§11）。别凭上一轮的印象预设范围。

### 6.9 DI 图表的黑色外框会骗过「页脚检测」⭐本轮新发现
`compute_end`（§5-D）如果只用「单行暗像素占比 > 40%」判定页脚起点，会被 **DI 看图说话题的柱状图/折线图黑色外框线**
误伤——图表顶部那条实心黑边往往在题目开始后几十像素就出现，一旦被误判成「页脚」，`compute_end` 会在题目刚开始时
就掐断，裁出一张只有几十像素高的废图（图表和后面的答案全丢了）。

**必须**改成「持续变暗」判定：往下再看一个窗口（如 40 行），窗口内平均暗像素占比也要 > 40% 才算真页脚（真页脚是
几百像素高的实心块，图表外框只有 1~2 行）。见 §5-D 代码里的 `compute_end`。

**排查方法**：裁完后，**凡是靠 `compute_end` 定下边界的题**（也就是每张源图里的最后一题）都要打开看一眼，
尤其是图表/图片类题型（DI），确认图表和答案区完整、没有缺失。

### 6.10 长截图里出现的「诡异分割线」不一定是导航条
有的整页长图会在某个几乎固定的绝对 Y 值（比如多张不同内容、不同长度的图恰好都在 y≈6997 附近）出现一条贯穿全宽的
细线，乍看很像 §6.1 的导航条重复出现（因为它也会让 `x<815` 的左边距扫描触发）。**先肉眼确认**：如果那条线只是
题目卡片之间的分隔线，或图表图例本身的颜色块巧合触发了检测，且**没有吞掉任何文字/图形内容**，就不用处理，
不算「已知缺口」。只有确认线条下方/上方的内容确实被真实覆盖丢失时，才按 §6.1 处理。

---

## 7. 生成脚本模板 / Generator template

**用法**：先跑 §5-B/§5-B2 得到并人工核对每题的 `(序号, 题型, 编号, 标题, 题号Y)`，填进下面的 `MANIFEST`；用 §5-E 的 `navbar_candidates` + 蒙太奇确认后，把「压在空白上的」导航条带填进 `NAV`、浮动按钮填进 `FLOAT`，再跑本脚本。
> 被导航条压住**真内容**的题（R01/R14 那种）**不要**走这个通用循环——它们要单独加提示条（见 §6.1），否则会被静默涂白。

```python
from PIL import Image, ImageDraw, ImageFont
import numpy as np, os, re
XL, XR, TOP_PAD = 835, 1912, 26   # ⚠️ 每套图都要按 §5-C 重新实测，别照抄

# 每张源图：文件名 -> 该图里要裁的题 [(序号, 题型, 编号, 标题, 题号Y), ...]（跨图连续编号）
MANIFEST = {
 '听力1.jpeg': [(1,'SST','712','Environmental Conservation',941), (2,'MCM-L','102','Time Famine',1386), ...],
 '听力2.jpeg': [(11,'HIW','216','T Cell',934), ...],
 # 阅读同理；口语只放 DI 那几题（若用户要求全裁，参照 §11 把其它题型也列进来）
}
PREFIX = {'听力1.jpeg':'L','听力2.jpeg':'L','阅读1.jpeg':'R','阅读2.jpeg':'R','口语2.jpeg':'DI','口语3.jpeg':'DI'}
OUTDIR = {'L':'cropped_questions/listening','R':'cropped_questions/reading','DI':'cropped_questions/speaking_DI'}
# 导航条压空白 -> 涂白；压内容 -> 见 §6.1 单独处理，别放这
NAV   = {'听力1.jpeg':[(1103,1182)], '听力2.jpeg':[(3243,3322)], ...}   # 若确认这批没有，留空字典即可
FLOAT = {'阅读1.jpeg':[(2843,2948,1866)], ...}   # (y0,y1,x_left)，若确认没有，留空字典即可

def load(fn):
    a=np.asarray(Image.open(fn).convert('RGB')).copy()
    for y0,y1 in NAV.get(fn,[]):        a[y0:y1, XL-5:XR+5]=255
    for y0,y1,xl in FLOAT.get(fn,[]):   a[y0:y1, xl:XR+5]=255
    return a

def compute_end(a,start):              # 见 §5-D；已含 §6.9 的「持续变暗」修复
    H=a.shape[0]; sub=a[start:H].astype(int); R,G,B=sub[:,:,0],sub[:,:,1],sub[:,:,2]
    dark=(sub.max(axis=2)<90).mean(axis=1)
    n=len(dark); win=40; csum=np.cumsum(np.insert(dark,0,0.0)); footer=n
    for i in range(n-win):
        if dark[i]>0.4 and (csum[i+win]-csum[i])/win>0.4: footer=i; break
    teal=(G>140)&(R<130)&(B>120)&(G-R>45); z=teal[:footer, XL:XL+180].sum(axis=1)
    rows=np.where(z>6)[0]; return start+(int(rows[-1])+48 if len(rows) else footer-30)

def san(s): return re.sub(r'[^A-Za-z0-9-]+','_',s).strip('_')

for fn, items in MANIFEST.items():
    a=load(fn); im=Image.fromarray(a); pre=PREFIX[fn]; out=OUTDIR[pre]; os.makedirs(out,exist_ok=True)
    for i,(num,typ,qid,title,top) in enumerate(items):
        ct=max(0,top-TOP_PAD)
        cb=items[i+1][4]-TOP_PAD+2 if i+1<len(items) else compute_end(a,top)
        name='_'.join([f'{pre}{num:02d}',typ,qid]+([san(title)] if title else []))+'.png'
        im.crop((XL,ct,XR,cb)).save(os.path.join(out,name)); print(name)
```

---

## 8. 质检 / QA（不可跳过）

1. **数量**：听力/阅读题数对不对？口语范围（DI-only 还是全裁）符合用户这次的要求吗？跨图题号是否连续无缺号？
   （写脚本核对：把所有文件名的序号 parse 出来，跟 `1..N` 做集合差，缺号/多号一眼看出。）
2. **Contact sheet**：把所有成品缩略拼成一张大图，一次性核对每张的**上下边界**（有没有切到标题、有没有混进下一题、有没有页脚/翻页条）。图多的话按 section 分成几张 sheet，别一张塞几十张挤成马赛克看不清。
```python
import glob, os
from PIL import Image, ImageDraw
files=sorted(glob.glob('cropped_questions/*/*.png'))
CW,CH,cols=300,420,5; rows=(len(files)+cols-1)//cols
sheet=Image.new('RGB',(cols*CW,rows*CH),(230,230,230)); d=ImageDraw.Draw(sheet)
for i,f in enumerate(files):
    im=Image.open(f); im.thumbnail((CW-12,CH-40)); r,c=divmod(i,cols)
    sheet.paste(im,(c*CW+6,r*CH+34)); d.text((c*CW+8,r*CH+12),os.path.basename(f)[:-4],fill=(0,0,0))
sheet.save('/tmp/contact_sheet.png')
```
3. **抽查全分辨率**：每个部分挑首题、尾题、含图表的题（DI）、疑似被导航条/浮动按钮影响的题，打开原图核对。
   **尤其是每张源图里靠 `compute_end` 定边界的最后一题**（§6.9 的坑只在这里出现）。
4. **已知缺口**：所有「被导航条挡住」的题都加了提示条并写进 README 了吗？如果排查后确认这批没有这个问题，
   也要在 README 里明说「已排查，无此问题」，别让读的人以为你没查。
5. **弹窗（若有 docx）**：§11 裁出来的每张弹窗，标题里的 `#题库编号` 是否和它挂靠的主图一致？
   **不要假设 docx 里图片的顺序 = 题号顺序**——务必逐张核对 ID，见 §11 的教训。

---

## 9. Git 规范 / Git

- **分支命名**：不要随机名，用**英文含义 + 时间戳**。例：`claude/pte-core-crop-YYYYMMDD-HHMMSS`。
- 原图（含 docx）`git mv` 进 `original_screenshots/`（保留改名记录）。
- commit 信息说清做了什么；**不要主动开 PR**（除非被明确要求）。
- push：`git push -u origin <branch>`，网络失败按 2/4/8/16s 退避重试。

---

## 10. 完成标准 / Definition of Done

- [ ] 原图（含 docx）全部搬进 `original_screenshots/`，未改动。
- [ ] `cropped_questions/` 下按用户这次要求的范围齐全、命名规范、题号连续。
- [ ] 每张都从题号裁到评分行；无页脚、无翻页条、无导航条、无浮动按钮残留。
- [ ] 若有 docx 弹窗图，已按 §11 裁出并挂到正确的题目（ID 逐张核对过）。
- [ ] 被导航条挡住的内容都加了**黄色提示条** + README「已知缺口」记录，**没有脑补编造**；若排查后确认无此问题，也在 README 里写明。
- [ ] 跑过 contact sheet 并逐张目检通过，尤其是每张源图的最后一题（§6.9）。
- [ ] 一份**中英双语 README** 说明结构 + 题目清单 + 已知缺口（或"已排查，无"）。
- [ ] 已 commit 并 push 到规范命名的分支。

---

## 11. 批量弹窗截图（docx 里的「AI 评分详情」）处理方法 ⭐本轮新增

**背景**：口语的 RA/RS/DI/RTS 和写作的 SWT/WE，主长截图里只显示精简评分胶囊（如 `RA V6.0` `评分详情 20/90分`），
**没有** Content/Pronunciation/Fluency 细分、AI 语音识别逐词颜色标注、语法批改这些细节。这些细节只有点开弹窗才
显示，所以用户会**额外**截一批「弹窗」图（一次一题，浏览器截图，弹窗浮在灰色蒙层上），塞进 `.docx` 文件里给你
（`word/media/imageN.png`）。SST/SWT/WE 的弹窗则是表格式评分（`单项/得分/建议` 三列 + Content/Form/Grammar/
Spelling/Vocabulary 几行）。ASQ 通常没有这类弹窗（对/错判分，主图已完整）。

### 11.1 从 docx 拿到图片
```bash
mkdir -p extract && unzip -o 口语.docx -d extract   # docx 本质是 zip
ls extract/word/media/            # image1.png, image2.png, ...
```

### 11.2 裁出白色弹窗（去掉灰色蒙层 + 露出的浮动按钮）
弹窗背景是**均匀灰色蒙层**（RGB 常见在 130~140），弹窗本身是白底圆角卡片。**弹窗的宽高会因内容多少而变**
（RA 内容长，卡片可能顶到视口底部；RS 内容短，卡片矮很多；SWT/WE 的卡片宽度跟 RA/RS 的还不一样）——
**不要用一个固定的裁剪框套所有图**，用下面两阶段投影法逐张动态检测：

```python
import numpy as np
from PIL import Image

def largest_run(mask):
    idx = np.where(mask)[0]
    if len(idx) == 0: return None
    runs=[]; s=p=idx[0]
    for v in idx[1:]:
        if v-p>5: runs.append((s,p)); s=v
        p=v
    runs.append((s,p)); runs.sort(key=lambda r:r[1]-r[0])
    return runs[-1]

def modal_bbox(a):
    H,W,_=a.shape
    # 从图像最左/最右各15px窄条、多个高度采样，取中位数当"蒙层灰"参考色
    # （用多个 y 采样，避免正好采到浮动按钮或导航头）
    ys=[int(H*f) for f in (0.3,0.5,0.7)]
    samples=[]
    for y in ys:
        samples.append(a[y,0:15].reshape(-1,3)); samples.append(a[y,W-15:W].reshape(-1,3))
    bg=np.median(np.concatenate(samples,0).astype(int),axis=0)
    is_bg=(np.abs(a.astype(int)-bg).max(axis=2)<20)
    top,bottom=largest_run(is_bg.mean(axis=1)<0.5)              # 第一阶段：整行找上下边界
    sub=is_bg[top:bottom+1]
    left,right=largest_run(sub.mean(axis=0)<0.5)                # 第二阶段：只在弹窗行范围内找左右边界
    return left,top,right,bottom

a = np.asarray(Image.open('extract/word/media/image1.png').convert('RGB'))
l,t,r,b = modal_bbox(a)
Image.open('extract/word/media/image1.png').crop((l-5,t-5,r+5,b+5)).save('out.png')
```
> **不要用连通域(connected component)标注法**——弹窗和背景上的**半透明防盗水印**（贯穿全图的斜向文字水印）
> 会把弹窗区域和背景区域"连"成一整块，导致包围盒直接变成整张图。两阶段投影法（先整行再整列）没有这个问题。

**极少数图会检测失败**（比如恰好有个搜索框/tooltip 之类的杂项 UI 元素叠在弹窗左上角，把参考色采样带偏，或让
包围盒往左上多包出一截）。**这时不要硬套自动结果**：肉眼看一下这张图，参考同类型（同样是 RA/RS/RTS/…）其它
张的框选值手动填一个，或者干脆往下移一点跳过那个杂项元素（反正裁掉的顶部通常只是「口语提升目标」推广横幅，
不是考题内容，裁掉不影响）。

### 11.3 把每张弹窗对应到正确的题目 ⭐容易犯错的地方
**不要假设 docx 里图片的顺序 = 题目的自然顺序！** 亲测遇到过顺序错位（比如三道 RTS 里，`image23.png` 对应
第 24 题而不是第 23 题，`image24.png` 对应第 23 题）。

**每张弹窗左上角通常有 `#题库编号 评分详情`**（如 `#771 评分详情`），这个题库编号在主截图的标题里也有
（`1. RA #771 Venture Capitals`），**用这个 ID 做匹配，不要用图片文件名的顺序**。

有两类弹窗版式要注意：
- **正常版**：弹窗左上角直接就是 `#题库编号 评分详情`，一眼可读。
- **另一种版式**（同一批里偶尔混着出现，可能是平台 A/B 皮肤）：弹窗顶部写的是通用的 `AI 评分` 而不是
  `#题库编号`，这种要往下滚动看**评分表格里的 `建议` 列**（会写 `RA V6.0` 之类的版本号）或者**直接读
  转写文本内容**，跟主截图里题目原文的开头几个词做匹配来确认对应哪一题。
- 写作(SWT/WE)的弹窗有时背景蒙层没完全遮住底图，**主截图的标题行会直接透在弹窗上方/周围**（如
  `1. SWT (C) #61 Psychotherapy`），这种最好认，直接读。

**建议流程**：先批量裁出每张弹窗左上角一小条区域（`#题库编号 评分详情` 那几行）拼成 montage 一次看完，
能读到 ID 的直接匹配；读不到 ID 的（"AI 评分"版式）逐张打开看转写文本内容，跟主图比对确认。**全部确认完
再批量裁剪+命名**，避免张冠李戴。

### 11.4 命名 & 归档
确认好 `docx图片编号 → 题目序号` 的映射后，按 §3 的规则命名为 `{前缀}{序号}b_{题型}_{编号}[_{标题}].png`，
存进对应的 `cropped_questions/{listening,reading,speaking,writing}/` 子目录，**紧挨着它的主图**（文件名排序
自然会排在一起，如 `S01_RA_771_….png` 和 `S01b_RA_771_….png`）。

### 11.5 完整性交叉核对
弹窗数量应该等于「主截图里评分胶囊不够详细、需要弹窗补充细节的题型」的题目总数（比如这一轮是
RA+RS+DI+RTS+SST+SWT+WE 共 29 题，docx 里也正好给了 29 张图）。**如果数量对不上**，说明可能漏了某题的
弹窗，或者 docx 里混进了不相关的图——回头检查，缺的题目在最终报告里告诉用户，让用户回平台补截。

---

## 附：参考实现 / Reference implementation
- **只裁听力/阅读全部 + 口语仅 DI** 的参考：`pte-002-1-0704` 仓库，分支 `claude/pte-core-crop-20260704-033730`
  （`cropped_questions/` 是成品，README 有完整题目清单和「已知缺口」示例，R01/R14 是提示条的实际范例）。
- **全题型裁剪（含口语全部题型 + 写作）+ docx 弹窗批量处理** 的参考：本仓库 `pte-003-0707`，本分支
  （§11 的方法就是在这一轮总结出来的；这一轮排查后确认**没有**导航条压内容的问题，是「排查后确认无」的范例）。
