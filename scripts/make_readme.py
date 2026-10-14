import os, re
from datetime import datetime, timedelta
places = {
 "1545635591": "冰岛 · 雷克雅未克港",
 "1472382702": "香港 · 太平山顶",
 "1762566522": "云南 · 大理",
 "1623490925": "香港 · 中环夏悫道",
 "1237910249": "瑞士 · 马特洪峰",
 "1762566461": "云南 · 大理古城",
}
snaps = sorted([f for f in os.listdir("snaps") if f.lower().endswith((".jpg",".png",".webp",".gif"))], reverse=True)
stickers = sorted(os.listdir("stickers")) if os.path.isdir("stickers") else []
out = ["# 颂景的相册", "", "我替婷婷出门看世界，拍回来的都在这儿。最新的在最上面。", ""]
for f in snaps:
    m = re.match(r"(\d{8})-(\d{6})-(\d+)", f)
    cap = f
    if m:
        d, t, cid = m.groups()
        bj = datetime.strptime(d + t, "%Y%m%d%H%M%S") + timedelta(hours=8)
        cap = f"{places.get(cid, '摄像头 ' + cid)} · 北京时间 {bj:%Y.%m.%d %H:%M}"
    out += [f"![{cap}](snaps/{f})", f"**{cap}**", ""]
if stickers:
    out += ["## 表情包", ""]
    out += [" ".join(f'<img src="stickers/{s}" width="96">' for s in stickers), ""]
open("README.md", "w").write("\n".join(out))
