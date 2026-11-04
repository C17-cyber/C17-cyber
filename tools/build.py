#!/usr/bin/env python3
"""Build an original, SVG-first C17 Cyber GitHub profile.
Reference layout: Victor Studios' image-led GitHub profile. All artwork and copy here are new.
Change CONTENT below, run python tools/build.py, commit README.md and assets/.
"""
from pathlib import Path
from html import escape as E
import math, random, textwrap, os

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
for p in [ROOT, ASSETS, ASSETS/'dark', ASSETS/'light', ROOT/'.github'/'workflows', ROOT/'tools']:
    p.mkdir(parents=True,exist_ok=True)

# -- EDIT HERE: verified or user-provided destinations --
LINKS = [
    ('GITHUB', 'https://github.com/C17-cyber', 'GH'),
    ('IMORTEL', 'https://imortel.fr', 'WEP'),
    ('PVP4CARRY', 'https://pvp4carry.fr', 'WEB'),
    ('LINKEDIN', 'https://www.linkedin.com/in/m%E1%B4%80%CA%80%E1%B4%A1%E1%B4%80%C9%B4/', 'IN'),
]
PROJECTS = [
    ('C17CHAT', 'PRIVATE MESSAGING', 'Anonymous communication. E2EE, offline networking and privacy-first research.', 'IN DEVELOPMENT', 'https://github.com/C17-cyber', 'mesh'),
    ('PVP4CARRY', 'WEB PLATFORM', 'Destiny 2 services platform, custom website and Discord integration.', 'WEBSITE LIVE', 'https://pvp4carry.fr', 'web'),
    ('IMORTEL', 'WEB PLATFORM', 'Modern web experience featuring responsive design, smooth animations and immersive UI. 2024', 'WEBSITE LIVE', 'https://imortel.fr', 'orbit'),
]
CAPABILITIES = [
    ('CRYPTOGRAPHY', 'E2EE, key exchange, digital signatures, HKDF and secure protocol research.', 'crypto'),
    ('P2P & MIXNETS', 'Offline-first messaging, peer discovery and decentralized routing architectures.', 'mesh'),
    ('PRIVACY ENGINEERING', 'Metadata minimization, anonymity threats, Tor and privacy-focused design.', 'shield'),
    ('DEFENSIVE SECURITY', 'Wazuh, SIEM, log analysis, hardening, FIM and threat detection labs.', 'radar'),
    ('NETWORK SECURITY', 'Segmentation, VLANs, ACLs, DNS, firewalls and infrastructure security.', 'network'),
    ('FORENSICS / CTF', 'Digital forensics, reverse engineering, traffic analysis and technical challenges.', 'forensic'),
]
WORK = [
    ('WAZUH LAB', 'Detection engineering', 'FIM / log analysis / security alerts', 'wazuh'),
    ('KEYCLOAK + GLPI', 'Identity and access', 'SSO, centralized service management', 'identity'),
    ('NETWORK DEFENSE', 'Secure infrastructure', 'VLAN segmentation / ACL / syslog', 'network'),
    ('DEBIAN / HTTPS', 'Self-hosted architecture', 'Reverse proxy / TLS / WordPress', 'server'),
    ('DFIR / CTF', 'Practical challenges', 'Forensics / ransomware / steganography', 'forensic'),
    ('DEV + AUTOMATION', 'Full-stack development', 'React / Vite / Docker / n8n', 'web'),
]
MILESTONES = [
    ('HACKERVERSE CTF', 'EC-COUNCIL  /  2026', '2,000 / 2,000 points', '#58 Worldwide     Grandmaster', 'ctf'),
    ('EHE CERTIFICATION', 'EC-COUNCIL', 'Ethical Hacking Essentials', 'Cybersecurity & ethical hacking fundamentals', 'diploma'),
    ('CRYPTO RESEARCH', 'CURRENT FOCUS', 'Noise · X25519 · ML-KEM', 'Protocols & anonymity systems: study / exploration', 'crypto'),
]

DARK = dict(bg='#0B0D14', card='#121521', tile='#161A28', edge='#343044', text='#F3F1FF', muted='#ABB0C5', accent='#AD86FF', bright='#73DAF8', subtle='#211B37', gradient2='#4B2E82')
LIGHT = dict(bg='#F5F6FA', card='#FFFFFF', tile='#F8F9FD', edge='#D9DCE8', text='#151625', muted='#555D70', accent='#6F42B8', bright='#007EAD', subtle='#F0E9FF', gradient2='#B6A4EA')

def svg(w, h, body, defs='', bg=None):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><defs>{defs}</defs>{('<rect width="100%" height="100%" fill="'+bg+'"/>') if bg else ''}{body}</svg>'''

def save(path,content):
    p=ASSETS / path
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding='utf-8')

def rect(x,y,w,h,fill,rx=14,stroke='none',sw=1,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def txt(x,y,s,size=22,color='#fff',weight=500,anchor='start',family='Inter, Segoe UI, Arial, sans-serif',extra=''):
    return f'<text x="{x}" y="{y}" font-family="{E(family)}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" {extra}>{E(s)}</text>'

def line(x1,y1,x2,y2,color='#fff',sw=1,opacity=1,extra=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" opacity="{opacity}" {extra}/>'

def dot(x,y,r,fill): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'

def icon(name,x,y,c,s=52):
    X=x+s/2;Y=y+s/2
    lead=f'<g stroke="{c}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" fill="none">'
    if name in ('mesh','network'):
        points=[(x+8,y+12),(x+s-9,y+10),(x+14,y+s-10),(x+s-10,y+s-13),(X,Y)]
        edges=[(0,4),(1,4),(2,4),(3,4),(0,1),(2,3)]
        lead+=''.join(line(*points[a],*points[b],c,2,.9) for a,b in edges)
        lead+=''.join(f'<circle cx="{a}" cy="{b}" r="4" fill="{c}" stroke="none"/>' for a,b in points)
    elif name in ('crypto','shield','identity'):
        lead+=f'<path d="M {X} {y+6} L {x+s-8} {y+17} V {y+s*.54} Q {x+s-9} {y+s-4} {X} {y+s-3} Q {x+9} {y+s-4} {x+8} {y+s*.54} V {y+17} Z"/>'
        lead+=f'<rect x="{X-9}" y="{Y-3}" width="18" height="16" rx="3"/><path d="M {X-6} {Y-3} V {Y-8} a 6 6 0 0 1 12 0 v 5"/>'
    elif name=='web':
        lead+=f'<rect x="{x+6}" y="{y+9}" width="{s-12}" height="{s-18}" rx="4"/>'
        lead+=line(x+6,y+19,x+s-6,y+19,c,2)
        for a in [12,17,22]: lead+=dot(x+a,y+14,1.4,c)
        lead+=f'<path d="M {x+18} {Y-1} l -6 6 6 6 M {x+s-18} {Y-1} l 6 6 -6 6"/>'
    elif name in ('radar','forensic','ctf'):
        lead+=f'<circle cx="{X}" cy="{Y}" r="{s*.38}"/><circle cx="{X}" cy="{Y}" r="{s*.22}"/>'
        lead+=f'<path d="M {X} {Y} L {x+s-5} {y+8}"/><circle cx="{X}" cy="{Y}" r="3" fill="{c}"/>'
    elif name=='server':
        for i in range(3): lead+=f'<rect x="{x+8}" y="{y+6+i*15}" width="{s-16}" height="12" rx="3"/><circle cx="{x+17}" cy="{y+12+i*15}" r="2" fill="{c}"/>'
    elif name=='orbit':
        lead+=f'<ellipse cx="{X}" cy="{Y}" rx="{s*.4}" ry="{s*.17}" transform="rotate(-30 {X} {Y})"/>'
        lead+=f'<circle cx="{X}" cy="{Y}" r="{s*.17}"/><circle cx="{X+18}" cy="{Y-15}" r="4" fill="{c}"/>'
    elif name=='diploma':
        lead+=f'<path d="M {x+5} {y+20} L {X} {y+6} L {x+s-5} {y+20} L {X} {y+36} Z"/><path d="M {x+14} {y+29} V {y+40} Q {X} {y+49} {x+s-14} {y+40} V {y+29}"/>'
    else:
        lead+=f'<circle cx="{X}" cy="{Y}" r="{s*.33}"/>'
    return lead+'</g>'

def wrap_words(s,max_chars=33,max_lines=3):
    ls=textwrap.wrap(s,width=max_chars,break_long_words=False,break_on_hyphens=False)
    if len(ls)>max_lines:
        ls=ls[:max_lines];ls[-1]=ls[-1].rstrip('., ')+'...'
    return ls

def lines_of_text(x,y,text,theme,size=19,width=32,dy=28,max_lines=3):
    return ''.join(txt(x,y+i*dy,l,size,theme['muted'],430) for i,l in enumerate(wrap_words(text,width,max_lines)))

def core_defs(c):
    return f'''<linearGradient id="aurora" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="{c['accent']}" stop-opacity="0.05"/><stop offset="0.5" stop-color="{c['gradient2']}" stop-opacity="0.65"/><stop offset="1" stop-color="{c['bright']}" stop-opacity="0.22"/></linearGradient><linearGradient id="glow" x1="0" x2="1"><stop stop-color="{c['accent']}"/><stop offset="1" stop-color="{c['bright']}"/></linearGradient><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="{c['edge']}" stroke-width="0.7" opacity="0.45"/></pattern>'''

def frame(w,h,c,withgrid=True):
    b=rect(.8,.8,w-1.6,h-1.6,c['card'],22,c['edge'],1.4)
    if withgrid:b+=rect(1,1,w-2,h-2,'url(#grid)',22,extra='opacity=".18"')
    b+=line(29,h-13,105,h-13,c['accent'],3,.7)
    b+=line(w-101,13,w-29,13,c['accent'],2,.5)
    return b

def header_hero():
    c=DARK; w=960;h=305
    defs=core_defs(c)+'''<radialGradient id="heroAura" cx="76%" cy="50%" r="70%"><stop offset="0" stop-color="#683BBD" stop-opacity="0.4"/><stop offset=".66" stop-color="#10111D" stop-opacity="0.3"/><stop offset="1" stop-color="#0B0D14" stop-opacity="0"/></radialGradient><filter id="softGlow"><feGaussianBlur stdDeviation="11"/></filter>'''
    b=rect(0,0,w,h,c['bg'],20)+rect(0,0,w,h,'url(#heroAura)',20)
    b+=rect(9,9,w-18,h-18,'none',15,c['edge'],1.3)
    b+=rect(28,25,10,10,c['accent'],2)+txt(49,35,'C17 / RESEARCH INTERFACE',14,c['muted'],700,extra='letter-spacing="2"')
    b+=txt(34,133,'C17',109,c['text'],900,extra='letter-spacing="-7"')
    b+=txt(277,133,'CYBER',109,c['text'],830,extra='letter-spacing="-6"')
    b+=rect(34,148,565,5,'url(#glow)',2)
    b+=txt(35,192,'CRYPTOGRAPHY  /  DECENTRALIZATION  /  PRIVACY',18,c['muted'],600,extra='letter-spacing="1"')
    b+=txt(35,240,'SECURE SYSTEMS. MINIMAL TRUST. MAXIMUM RESILIENCE.',16,c['bright'],650,extra='letter-spacing="1.1"')
    b+=txt(36,274,'IDENTITY : C17-CYBER',13,c['muted'],530,extra='letter-spacing="1.4"')
    b+=txt(594,274,'GITHUB // 2026',13,c['muted'],530,extra='letter-spacing="1.4"')
    # right: subtle cryptographic rings and a packet flow -- abstract identity, no copyrighted icons
    b+=f'<g transform="translate(784 150)"><circle r="113" stroke="{c["accent"]}" stroke-width="1.4" stroke-dasharray="7 10" fill="none" opacity=".8"/><circle r="88" stroke="{c["bright"]}" stroke-width="1" fill="none" opacity=".35"/><circle r="61" stroke="{c["accent"]}" stroke-width="1.2" stroke-dasharray="5 7" fill="none" opacity=".65"/><circle r="29" stroke="{c["accent"]}" stroke-width="1.5" fill="none"/><circle r="7" fill="{c["bright"]}"/><path d="M -114 0 H 115 M 0 -114 V 115" stroke="{c["edge"]}" opacity=".55"/><circle r="8" cx="88" cy="0" fill="{c["accent"]}"><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="10s" repeatCount="indefinite"/></circle><g transform="rotate(45)"><rect x="-76" y="-76" width="152" height="152" rx="6" stroke="{c["accent"]}" fill="none" opacity=".23"/></g></g>'
    # terminal text blips
    for i in range(18):
        rng=random.Random(100+i)
        x=681+(i%6)*42;y=46+(i//6)*84
        b+=txt(x,y,'01'[rng.randrange(2)],10,c['muted'],500,extra='opacity=".26"')
    return svg(w,h,b,defs)

save('hero.svg',header_hero())

def label_svg(name,sub,c):
    w,h=960,112;defs=core_defs(c)
    b=rect(0,0,w,h,c['bg'],10)+txt(6,56,name,39,c['text'],830,extra='letter-spacing="-1.2"')
    b+=txt(7,86,sub,14,c['muted'],520,extra='letter-spacing="1.0"')
    b+=line(0,104,w,104,c['edge'],1.6)
    b+=line(0,104,157,104,c['accent'],3)
    b+=txt(935,58,'C17 /',14,c['accent'],800,'end')
    return svg(w,h,b,defs)

sections=[
('s01','PRODUCTS & PROJECTS','01 / WHAT I AM BUILDING'),
('s02','FOCUS AREAS','02 / WHAT I RESEARCH AND ENGINEER'),
('s03','SELECTED WORK','03 / LABS, SYSTEMS AND APPLICATIONS'),
('s04','CERTIFICATIONS & CTF','04 / EDUCATION, CHALLENGES AND MILESTONES'),
('s05','MY TOOLKIT','05 / CRYPTOGRAPHIC AND ENGINEERING STACK'),
('s06','BUILDING IN PUBLIC','06 / GITHUB CONTRIBUTION ACTIVITY'),
]

for th, c in [('dark',DARK),('light',LIGHT)]:
    for sid,name,sub in sections:save(f'{th}/{sid}.svg',label_svg(name,sub,c))

def pill(label,icontext,c):
    w,h=202,49
    defs=core_defs(c)
    b=rect(1,1,w-2,h-2,c['card'],11,c['edge'],1.5)
    b+=rect(13,10,30,29,c['subtle'],7)
    b+=txt(28,29,icontext,10,c['accent'],760,'middle')
    b+=txt(55,31,label,15,c['text'],740,extra='letter-spacing=".65"')
    return svg(w,h,b,defs)
for th,c in [('dark',DARK),('light',LIGHT)]:
    for name,href,ic in LINKS:save(f'{th}/l-{name.lower()}.svg',pill(name,ic,c))

def now_card(c):
    w,h=960,104
    b=frame(w,h,c,False)
    b+=rect(24,29,90,42,c['subtle'],10)+txt(69,56,'NOW',16,c['accent'],790,'middle')
    b+=txt(137,44,'BUILDING C17CHAT',24,c['text'],800)
    b+=txt(137,74,'Private messaging  /  P2P research  /  E2EE  /  privacy-first architecture',17,c['muted'],530)
    b+=dot(914,51,6,c['accent'])
    return svg(w,h,b,core_defs(c))
for th,c in [('dark',DARK),('light',LIGHT)]:save(f'{th}/now.svg',now_card(c))

def project_card(item,c,typ='project'):
    name,category,description,status,url,iconname=item
    w,h=305,244
    b=frame(w,h,c)
    b+=rect(18,17,112,22,c['subtle'],6)+txt(74,32,category[:19],11,c['accent'],780,'middle')
    b+=icon(iconname,235,29,c['accent'],49)
    b+=txt(20,98,name,27,c['text'],850,extra='letter-spacing="-.45"')
    b+=lines_of_text(20,134,description,c,16,33,26,3)
    b+=line(20,212,281,212,c['edge'],1.4)
    b+=dot(28,225,4,c['bright'] if 'LIVE' in status else c['accent'])
    b+=txt(40,230,status,11,c['muted'],740,extra='letter-spacing=".3"')
    return svg(w,h,b,core_defs(c))

def capability_card(item,c):
    name,desc,ic=item
    w,h=305,215
    b=frame(w,h,c)
    b+=icon(ic,229,16,c['accent'],56)
    b+=txt(19,96,name,22 if len(name)<17 else 19,c['text'],790)
    b+=lines_of_text(19,131,desc,c,16,34,24,3)
    return svg(w,h,b,core_defs(c))

def work_card(item,c):
    name,category,desc,ic=item
    w,h=305,205
    b=frame(w,h,c)
    b+=icon(ic,231,24,c['accent'],49)
    b+=txt(20,94,name,22,c['text'],810)
    b+=txt(20,125,category.upper(),12,c['accent'],650,extra='letter-spacing="1"')
    b+=lines_of_text(20,160,desc,c,15,35,22,2)
    return svg(w,h,b,core_defs(c))

def milestone_card(item,c):
    name,category,top,sub,ic=item
    w,h=305,226
    b=frame(w,h,c)
    b+=icon(ic,232,24,c['accent'],48)
    b+=txt(18,69,name,22,c['text'],820)
    b+=txt(18,99,category,11,c['accent'],750,extra='letter-spacing=".6"')
    b+=txt(18,141,top,21,c['text'],700)
    b+=lines_of_text(18,169,sub,c,14,34,22,2)
    return svg(w,h,b,core_defs(c))

for th,c in [('dark',DARK),('light',LIGHT)]:
    for i,it in enumerate(PROJECTS,1):save(f'{th}/p{i}.svg',project_card(it,c))
    for i,it in enumerate(CAPABILITIES,1):save(f'{th}/sv{i}.svg',capability_card(it,c))
    for i,it in enumerate(WORK,1):save(f'{th}/w{i}.svg',work_card(it,c))
    for i,it in enumerate(MILESTONES,1):save(f'{th}/m{i}.svg',milestone_card(it,c))

def stack_svg(c):
    w,h=960,330
    b=frame(w,h,c)
    groups=[
      ('CRYPTOGRAPHIC PRIMITIVES',['X25519','Ed25519','Noise','HKDF','BLAKE3','ChaCha20','ML-KEM']),
      ('PRIVACY & NETWORKS',['Tor','Nym / Mixnets','P2P','BLE Mesh','TLS','Zero Trust']),
      ('SECURITY LAB',['Wazuh','Keycloak','GLPI','Kali Linux','Syslog','DFIR']),
      ('DEVELOPMENT',['Python','Bash','React','Vite','Docker','Node.js','Linux'])
    ]
    for i,(head,tags) in enumerate(groups):
        y=22+i*73
        b+=txt(23,y+14,head,13,c['accent'],760,extra='letter-spacing="1.25"')
        x=23
        for tag in tags:
            wid=max(72,min(152,18+len(tag)*9.15))
            if x+wid>939:break
            b+=rect(round(x,1),y+24,round(wid,1),31,c['tile'],7,c['edge'],1)
            b+=txt(round(x+wid/2,1),y+45,tag,14,c['text'],590,'middle')
            x+=wid+10
    return svg(w,h,b,core_defs(c))
for th,c in [('dark',DARK),('light',LIGHT)]:save(f'{th}/stack.svg',stack_svg(c))

def cta_svg(c):
    w,h=960,155
    b=rect(0,0,w,h,c['card'],18,c['edge'],1.2)
    b+=rect(0,0,w,h,'url(#aurora)',18)
    b+=txt(30,55,'BUILD SOMETHING SECURE.',35,c['text'],820)
    b+=txt(30,88,'C17 CYBER  /  OPEN TO RESEARCH, COLLABORATION & ENGINEERING',16,c['muted'],600)
    b+=rect(714,51,205,51,c['accent'],11)
    b+=txt(816,83,'CONNECT ON GITHUB',14,c['bg'],850,'middle')
    b+=txt(30,129,'github.com/C17-cyber',14,c['muted'],530)
    return svg(w,h,b,core_defs(c))
for th,c in [('dark',DARK),('light',LIGHT)]:save(f'{th}/cta.svg',cta_svg(c))

# SVG placeholders will be replaced by Platane/snk GitHub Action on each scheduled run.
for th,c in [('dark',DARK),('light',LIGHT)]:
    w,h=960,175
    b=frame(w,h,c)
    b+=txt(27,44,'GITHUB CONTRIBUTIONS',17,c['text'],800)
    b+=txt(27,69,'C17 Contribution',13,c['muted'])
    r=random.Random(197)
    for i in range(51):
        for j in range(4):
            n=r.randrange(7)
            col=[c['tile'],c['subtle'],c['subtle'],c['accent'],c['accent'],c['bright'],c['accent']][n]
            b+=rect(25+i*17.8,84+j*17,12.7,12.7,col,2,extra='opacity=".55"')
    save(f'snake-{th}.svg',svg(w,h,b,core_defs(c)))

# README mirrors the information architecture and visual rhythm of the reference.
def picture(basename,alt,width='100%',h=None):
    siz=f'width="{width}"' if not h else f'height="{h}"'
    return f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/{basename}.svg"/><img src="assets/light/{basename}.svg" {siz} alt="{E(alt)}"/></picture>'

def row_cards(prefix,items,cols=3):
    out=[]
    for i in range(0,len(items),cols):
        out+=['<p align="center">']
        for j in range(i,min(i+cols,len(items))):
            it=items[j]
            if prefix=='p':href=it[4]
            elif prefix in ('sv','w','m'):href=''
            img=picture(f'{prefix}{j+1}',it[0],'32%')
            if href:out.append(f'<a href="{href}">{img}</a>')
            else:out.append(img)
        out.append('</p>')
    return '\n'.join(out)

r=[]
r.append('<!-- C17 Cyber / original vector graphics. Modify CONTENT in tools/build.py to regenerate the cards. -->')
r.append('<div align="center">')
r.append('<a href="https://github.com/C17-cyber"><img src="assets/hero.svg" width="100%" alt="C17 Cyber — Cryptography, decentralization, privacy and engineering"/></a>')
r.append('')
for label,href,icontext in LINKS:
    r.append(f'<a href="{href}">{picture("l-"+label.lower(),label,h="35")}</a>')
r.append('</div>')
r.append('<br/>')
r.append(picture('now','Now: building C17Chat, private messaging, peer to peer research and encryption'))
r.append('<br/><br/>')
r.append(picture('s01','Products and projects'))
r.append(row_cards('p',PROJECTS))
r.append('<br/>')
r.append(picture('s02','Focus areas'))
r.append(row_cards('sv',CAPABILITIES))
r.append('<br/>')
r.append(picture('s03','Selected technical work'))
r.append(row_cards('w',WORK))
r.append('<br/>')
r.append(picture('s04','Certifications and CTF milestones'))
r.append(row_cards('m',MILESTONES))
r.append('<br/>')
r.append(picture('s05','My toolkit'))
r.append(picture('stack','Cryptography and cybersecurity tools'))
r.append('<br/><br/>')
r.append(picture('s06','Building in public'))
r.append('<picture><source media="(prefers-color-scheme: dark)" srcset="assets/snake-dark.svg"/><img src="assets/snake-light.svg" width="100%" alt="C17 Cyber GitHub contributions; animated snake generated by GitHub Actions"/></picture>')
r.append('<br/><br/>')
r.append('<a href="https://github.com/C17-cyber">'+picture('cta','Connect with C17 Cyber on GitHub')+'</a>')
r.append('')
r.append('<!-- E2EE and post-quantum algorithm mentions describe research interests, not claims of certified implementation. -->')
(ROOT/'README.md').write_text('\n'.join(r)+'\n',encoding='utf-8')

# Action runs on schedule and manually to regenerate actual personal contributions; initial static placeholder is in assets/.
action='''name: C17 contributions animation
on:
  workflow_dispatch:
  schedule:
    - cron: "15 2 * * *"
permissions:
  contents: write
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Generate animated contribution snakes
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: C17-cyber
          outputs: |
            assets/snake-dark.svg?palette=github-dark&color_snake=%23AD86FF&color_dots=%2312151F,%23291C42,%234D307C,%237453B0,%23B79BFF
            assets/snake-light.svg?palette=github-light&color_snake=%236F42B8&color_dots=%23F4F2F9,%23D8CAF0,%23BDA6E7,%239770D0,%236F42B8
      - name: Commit generated animation
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "chore: update C17 contribution animations"
          file_pattern: 'assets/snake-*.svg'
'''
(ROOT/'.github'/'workflows'/'snake.yml').write_text(action,encoding='utf-8')

config='''# C17 CYBER — PERSONALIZE THIS PROFILE

This repository is designed to be the `C17-cyber/C17-cyber` GitHub profile repository.

## How to install

1. Create a **public** GitHub repository named `C17-cyber` under your `C17-cyber` account.
2. Copy `README.md`, `assets/` and `.github/` from this package into the repository root.
3. Commit and push. Your profile will immediately display the graphics.
4. Open **Actions** → **C17 contributions animation** → **Run workflow**. This replaces the placeholder activity graph with the real animated contribution snake.
5. In **Settings** → **Actions** → **General**, ensure workflow token permissions permit repository contents to be written if the workflow cannot commit.

## Easy edits

- Top links: `tools/build.py` → `LINKS`.
- Projects/sites: `tools/build.py` → `PROJECTS`.
- Skill cards: `CAPABILITIES`.
- Labs and work: `WORK`.
- CTF / diploma / credentials: `MILESTONES`.
- Theme: `DARK` and `LIGHT`.
- Run `python tools/build.py` to recreate the graphics and README.

**Current links to review:** `imortel.fr` portfolio and `linkedin.com/in/imortel` were previously associated with your online profile. Update them if they no longer represent your new C17 identity.

**Accuracy:** Hackerverse ranking is a user-reported result, not independently verified by this generator. The BTS SIO SISR is a diploma, not an industry cybersecurity certification. Research topics are interests, not proof of completed cryptography implementations. C17Chat / UberBoxing are marked in development, not as publicly shipped products.

**Technical note:** GitHub README pages support images, SVG and animated SVG, but not arbitrary React, JavaScript or Three.js execution. Assets are self-contained and require no external image service. Only the scheduled snake uses a GitHub Action and a third-party open-source generator.

**Design:** layout closely follows the reference's overall section arrangement: hero → links → current status → 3-column projects → offerings/focus → selected work → toolbox → contribution snake → CTA. Artwork and editorial text are original to C17 Cyber.
'''
(ROOT/'EDIT_ME.md').write_text(config,encoding='utf-8')
# build.py generator copy: when in tools/build.py, ROOT should be parent.parent not script parent / subdir.
code=Path(__file__).read_text(encoding='utf-8').replace("ROOT = Path(__file__).resolve().parent.parent", "ROOT = Path(__file__).resolve().parent.parent")
(ROOT/'tools'/'build.py').write_text(code,encoding='utf-8')
print('GENERATED',sum(1 for _ in ROOT.rglob('*') if _.is_file()),'files', ROOT)
