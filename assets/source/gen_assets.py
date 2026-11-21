#!/usr/bin/env python3
"""Generate Lune Linux logo + wallpapers (SVG sources). Usage: gen.py OUTDIR"""
import math, random, sys, pathlib

out = pathlib.Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)


def crescent_path(cx, cy, R, dx, dy, r):
    """Path of circle(R at cx,cy) minus circle(r at cx+dx, cy+dy). Explicit arc geometry."""
    x2, y2 = cx + dx, cy + dy
    d = math.hypot(dx, dy)
    a = (R * R - r * r + d * d) / (2 * d)
    h = math.sqrt(R * R - a * a)
    ux, uy = dx / d, dy / d
    mx, my = cx + a * ux, cy + a * uy
    p1 = (mx - h * uy, my + h * ux)
    p2 = (mx + h * uy, my - h * ux)

    def arc(pa, pb, C, rad, prefer):
        a1 = math.atan2(pa[1] - C[1], pa[0] - C[0])
        a2 = math.atan2(pb[1] - C[1], pb[0] - C[0])
        best = None
        for sweep in (1, 0):
            if sweep == 1:
                delta = (a2 - a1) % (2 * math.pi)
            else:
                delta = -((a1 - a2) % (2 * math.pi))
            am = a1 + delta / 2
            mid = (C[0] + rad * math.cos(am), C[1] + rad * math.sin(am))
            score = prefer(mid)
            if best is None or score > best[0]:
                best = (score, 1 if abs(delta) > math.pi else 0, sweep)
        return best[1], best[2]

    # outer arc: the part FAR from the cutting circle's centre
    lo, so = arc(p1, p2, (cx, cy), R, lambda m: math.hypot(m[0] - x2, m[1] - y2))
    # inner arc: the part of the cutting circle that lies INSIDE the outer circle
    li, si = arc(p2, p1, (x2, y2), r, lambda m: -math.hypot(m[0] - cx, m[1] - cy))
    f = lambda q: f"{q[0]:.2f} {q[1]:.2f}"
    return (f"M {f(p1)} A {R} {R} 0 {lo} {so} {f(p2)} "
            f"A {r} {r} 0 {li} {si} {f(p1)} Z")


# ---------------- logo ----------------
P = crescent_path(256, 256, 190, -88, -50, 158)
logo_white = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <path d="{P}" fill="#ffffff"/>
</svg>
'''
logo_color = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="g" x1="0.15" y1="0.1" x2="0.85" y2="0.95">
      <stop offset="0" stop-color="#fff4d6"/>
      <stop offset="0.55" stop-color="#d8c8ff"/>
      <stop offset="1" stop-color="#8f7cf0"/>
    </linearGradient>
  </defs>
  <path d="{P}" fill="url(#g)"/>
</svg>
'''
(out / "lune-logo-white.svg").write_text(logo_white)
(out / "lune-logo-color.svg").write_text(logo_color)

# ---------------- wallpapers ----------------
W, H = 3840, 2160
rnd = random.Random(7)


def stars(n, light=False):
    s = []
    for _ in range(n):
        x, y = rnd.uniform(0, W), rnd.uniform(0, H * 0.85)
        # fewer stars near the moon glow area is fine; keep it natural
        r = rnd.choice([1.2, 1.5, 1.8, 2.2, 2.8, 3.6])
        o = rnd.uniform(0.25, 0.95)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" opacity="{o:.2f}"/>')
    return "\n    ".join(s)


mcx, mcy, mR = 2700, 760, 330
MP = crescent_path(mcx, mcy, mR, -150, -85, 275)

night = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0" stop-color="#070a1c"/>
      <stop offset="0.5" stop-color="#161339"/>
      <stop offset="1" stop-color="#2d1b52"/>
    </linearGradient>
    <radialGradient id="glow" cx="{mcx+70}" cy="{mcy+40}" r="1300" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#9d8cff" stop-opacity="0.55"/>
      <stop offset="0.35" stop-color="#6a56d8" stop-opacity="0.22"/>
      <stop offset="1" stop-color="#6a56d8" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="haze" cx="900" cy="2100" r="1700" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ff8fb8" stop-opacity="0.30"/>
      <stop offset="0.5" stop-color="#b45fd6" stop-opacity="0.12"/>
      <stop offset="1" stop-color="#b45fd6" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="moon" x1="0.1" y1="0" x2="0.9" y2="1">
      <stop offset="0" stop-color="#fffaf0"/>
      <stop offset="0.6" stop-color="#e2d7ff"/>
      <stop offset="1" stop-color="#a996f5"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#haze)"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <g>
    {stars(420)}
  </g>
  <path d="{MP}" fill="#c9b8ff" opacity="0.65" filter="url(#blur)"/>
  <path d="{MP}" fill="url(#moon)" filter="url(#soft)"/>
  <path d="{MP}" fill="url(#moon)"/>
</svg>
'''

dawn = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.4" y2="1">
      <stop offset="0" stop-color="#cfd9f7"/>
      <stop offset="0.5" stop-color="#e8dbf7"/>
      <stop offset="1" stop-color="#fbd9d2"/>
    </linearGradient>
    <radialGradient id="glow" cx="{mcx+70}" cy="{mcy+40}" r="1200" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.85"/>
      <stop offset="0.4" stop-color="#ffffff" stop-opacity="0.25"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="peach" cx="700" cy="2200" r="1800" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#ffb9a3" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#ffb9a3" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="moon" x1="0.1" y1="0" x2="0.9" y2="1">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="1" stop-color="#f3e8ff"/>
    </linearGradient>
    <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="40"/>
    </filter>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#peach)"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <path d="{MP}" fill="#9a86d6" opacity="0.35" transform="translate(0 40)" filter="url(#shadow)"/>
  <path d="{MP}" fill="url(#moon)"/>
</svg>
'''
(out / "wallpaper-night.svg").write_text(night)
(out / "wallpaper-dawn.svg").write_text(dawn)
print("ok")
