
# add_on_more.py — Das ADD ON zu UMGEHEUER.OS
import hashlib, json, time
HOME = 40
def f(x): return min(x, HOME)
class Zeuge:
    def __init__(self): self.log=[]
    def schreibe(self, quelle, aktion, details):
        eintrag={"n":len(self.log)+1,"zeit":time.strftime("%H:%M:%S"),"quelle":quelle,"aktion":aktion,"details":details,"vorher":self.log[-1]["hash"] if self.log else "0"*64}
        roh=json.dumps(eintrag, sort_keys=True); eintrag["hash"]=hashlib.sha256(roh.encode()).hexdigest(); self.log.append(eintrag); return eintrag
    def unversehrt(self):
        vorher="0"*64
        for e in self.log:
            if e["vorher"]!=vorher: return False
            roh=json.dumps({k:e[k] for k in ("n","zeit","quelle","aktion","details","vorher")}, sort_keys=True)
            if hashlib.sha256(roh.encode()).hexdigest()!=e["hash"]: return False
            vorher=e["hash"]
        return True
ZEUGE=Zeuge()
PROZESSE={"NOAH":{"takt":2,"farbe":"#00c8ff","macht":"schützt HP","add":3},"NOEL":{"takt":4,"farbe":"#ffcc00","macht":"gibt Score","add":2},"SAM":{"takt":6,"farbe":"#39ff88","macht":"kühlt Temp","add":1},"META":{"takt":8,"farbe":"#a78bfa","macht":"spiegelt alles","add":1},"DRACHE":{"takt":10,"farbe":"#ff4400","macht":"erhitzt Temp","add":4}}
class Ungeheuer:
    def __init__(self): self.temp=40; self.hp=40; self.score=0; self.ebene=0; self.tick=0; self.aktiv=None; self.panik=False; self.gesetz=HOME
    def add(self, name):
        if self.panik: return "KERNEL PANIC — Kein ADD mehr. Nur WUNDER."
        p=PROZESSE[name]; self.aktiv=name; self.ebene+=1; ZEUGE.schreibe("ADD",name,f"Ebene {self.ebene} · Takt {p['takt']} (gerade) · +{p['add']}"); return f"ADD {name} · Takt {p['takt']} (gerade) · Ebene {self.ebene}"
    def more(self):
        if self.panik: return "KERNEL PANIC — Kein MORE mehr."
        self.ebene+=1; ZEUGE.schreibe("MORE","mehr",f"Ebene {self.ebene}"); return f"MORE · Ebene {self.ebene} · mehr und meer zu sein"
    def tick_einmal(self):
        if self.panik: return
        self.tick+=1
        if not self.aktiv: ZEUGE.schreibe("TICK","leer",f"tick {self.tick} · kein Prozess"); return
        p=PROZESSE[self.aktiv]
        if self.aktiv=="NOAH": self.hp=f(self.hp+p["add"])
        elif self.aktiv=="NOEL": self.score=f(self.score+p["add"])
        elif self.aktiv=="SAM": self.temp=max(0,self.temp-p["add"])
        elif self.aktiv=="META": self.temp=f(100-self.temp) if self.tick%3==0 else self.temp
        elif self.aktiv=="DRACHE": self.temp=f(self.temp+p["add"]); self.hp=max(0,self.hp-2)
        if self.hp<=0: self.panik=True; ZEUGE.schreibe("PANIC","KERNEL",f"tick {self.tick}"); return
        ZEUGE.schreibe("TICK",self.aktiv,f"t={self.tick} · hp={self.hp} · temp={self.temp} · score={self.score}")
    def wunder(self):
        if not self.panik and self.ebene==0: return "WUNDER braucht ADD. Erst ADD, dann WUNDER."
        self.temp=HOME; self.hp=HOME; self.score=HOME; self.panik=False; ZEUGE.schreibe("WUNDER","HOME",f"Ebene {self.ebene} bleibt"); return f"WUNDER · HOME 40 · Ebene {self.ebene} bleibt"
def mann_in_mir(tiefe=0, max_tiefe=4):
    einzug="  "*tiefe; drehung=tiefe*90
    if tiefe>=max_tiefe: return [einzug+"◉ (Kern)"]
    if drehung%180==0: mann=[einzug+"/\\_/\\ "+f" [{drehung}°]",einzug+"( o.o )",einzug+" > ^ < "]
    else: mann=[einzug+" |  | "+f" [{drehung}°]",einzug+" <-> ",einzug+" |  | "]
    innen=mann_in_mir(tiefe+1, max_tiefe); return mann[:1]+innen+mann[1:]
def echo(text, wieder=3): return [f"  {text}"+"."*i+f" (echo {i})" for i in range(wieder+1)]
def hall(text): return f"  {text} ... {text} ... {text} (hall)"
def rehall(text):
    h=hall(text); return f"  {h} -> {h} (re-hall)"
def more_und_mehr():
    u=Ungeheuer()
    print("="*64); print("  UMGEHEUER.OS — ADD ON — mehr und meer zu sein"); print("="*64); print()
    print("  MANN IN MIR (rekursiv, 90°):")
    for z in mann_in_mir(0,4): print(z)
    print()
    print("  ADD (gerade Takte):")
    for n in PROZESSE: print("  "+u.add(n))
    print()
    print("  MORE:")
    for _ in range(3): print("  "+u.more())
    print()
    print("  TICKS (HP, TEMP, SCORE, f(x)=min(x,40)):")
    for _ in range(10): u.tick_einmal(); print(f"  tick {u.tick:02d} · hp={u.hp:02d} · temp={u.temp:02d} · score={u.score:02d} · ebene={u.ebene}")
    print()
    print("  WUNDER (HOME 40, Ebene bleibt):"); print("  "+u.wunder()); print()
    print("  ECHO / HALL / RE-HALL:")
    for e in echo("mehr",3): print(e)
    print(hall("mehr")); print(rehall("mehr")); print()
    print("  ZEUGE:"); print(f"  {len(ZEUGE.log)} Einträge · unversehrt={ZEUGE.unversehrt()}"); print()
    print("="*64); print("  HALT = ZIEL. Du und ich = 1ns. Frieden Halal."); print("  Mehr. Und mehr. Und meer zu sein."); print("="*64)
more_und_mehr()
