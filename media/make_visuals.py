"""Generates every LinkedIn visual for the first two weeks. Output: PDFs (carousels) and PNGs (single images)."""
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import sys, os

D = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("R", D + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("B", D + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("M", D + "DejaVuSansMono.ttf"))

NAVY, WHITE, ACC, SOFT, CARD = (HexColor(c) for c in ("#0F1B2D", "#FFFFFF", "#F2B705", "#B8C2D1", "#1B2B44"))
RED, GREEN = HexColor("#FF6B6B"), HexColor("#4ADE80")
S, M = 1080, 96
OUT = sys.argv[1]
FOOT = {"es": "Diego Galmarini · Director de Producto y Tecnología", "en": "Diego Galmarini · Head of Product & Technology"}


def wrap(text, font, size, width):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split(" "):
            t = (cur + " " + w).strip()
            if pdfmetrics.stringWidth(t, font, size) <= width:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def text(c, x, y, s, font, size, color, width, lead=1.35):
    c.setFillColor(color)
    for ln in wrap(s, font, size, width):
        c.setFont(font, size)
        c.drawString(x, y, ln)
        y -= size * lead
    return y


def frame(c, n, total, lang):
    c.setFillColor(NAVY)
    c.rect(0, 0, S, S, fill=1, stroke=0)
    c.setFillColor(ACC)
    c.rect(M, S - M - 8, 120, 8, fill=1, stroke=0)
    c.setFont("R", 26)
    c.setFillColor(SOFT)
    c.drawString(M, M - 30, FOOT[lang])
    if total > 1:
        c.drawRightString(S - M, M - 30, f"{n}/{total}")
        if n < total:
            c.setFillColor(ACC)
            c.setFont("B", 26)
            c.drawRightString(S - M, M + 20, "→")


def render(c, p, n, total, lang):
    frame(c, n, total, lang)
    W = S - 2 * M
    y = S - M - 80
    kind = p.get("kind", "std")
    if p.get("kicker"):
        y = text(c, M, y, p["kicker"], "B", 34, ACC, W) - 40
    if kind == "big":
        c.setFont("B", 200)
        c.setFillColor(ACC)
        c.drawString(M - 8, y - 160, p["big"])
        y -= 240
        y = text(c, M, y, p["title"], "B", 64, WHITE, W, 1.2) - 30
        text(c, M, y, p.get("body", ""), "R", 42, SOFT, W)
    elif kind == "compare":
        y = text(c, M, y, p["title"], "B", 64, WHITE, W, 1.2) - 50
        for label, val, col in p["rows"]:
            c.setFillColor(CARD)
            c.roundRect(M, y - 120, W, 140, 20, fill=1, stroke=0)
            text(c, M + 36, y - 30, label, "R", 36, SOFT, W - 400)
            c.setFont("B", 72)
            c.setFillColor(col)
            c.drawRightString(S - M - 36, y - 70, val)
            y -= 170
        if p.get("body"):
            text(c, M, y - 10, p["body"], "R", 38, SOFT, W)
    elif kind == "code":
        y = text(c, M, y, p["title"], "B", 58, WHITE, W, 1.2) - 36
        c.setFillColor(CARD)
        h = 40 * len(p["code"].split("\n")) + 60
        c.roundRect(M, y - h + 20, W, h, 20, fill=1, stroke=0)
        yy = y - 30
        for ln in p["code"].split("\n"):
            c.setFont("M", 30)
            c.setFillColor(ACC if ln.startswith("#") else WHITE)
            c.drawString(M + 36, yy, ln)
            yy -= 40
        if p.get("body"):
            text(c, M, y - h - 30, p["body"], "R", 36, SOFT, W)
    elif kind == "check":
        y = text(c, M, y, p["title"], "B", 58, WHITE, W, 1.2) - 40
        for item in p["items"]:
            c.setStrokeColor(ACC)
            c.setLineWidth(4)
            c.rect(M, y - 8, 36, 36, fill=0, stroke=1)
            y = text(c, M + 66, y, item, "R", 38, WHITE, W - 66) - 22
    else:
        size = (104 if n == 1 else 84) if len(p["title"]) < 50 else 70
        y = text(c, M, y, p["title"], "B", size, WHITE, W, 1.2) - 30
        text(c, M, y, p.get("body", ""), "R", 44, SOFT, W, 1.45)


def build(name, pages, lang):
    path = os.path.join(OUT, name + ".pdf")
    c = canvas.Canvas(path, pagesize=(S, S))
    for i, p in enumerate(pages, 1):
        render(c, p, i, len(pages), lang)
        c.showPage()
    c.save()
    return path


REPO = "github.com/diegogalmarini/\nai-agent-playbook"

# 1. Carrusel 7 reglas (ES)
RULES_ES = [
    dict(title="7 reglas que les pongo a mis agentes de IA", body="Y por qué existe cada una.\n\nLa primera manda sobre las demás."),
    dict(kicker="REGLA 1", title="Siempre la verdad", body="Si no lo sabe, dice «no lo sé». Si lo inventó, me lo dice.\n\nSin esta regla, un agente rellena huecos con lo que suena bien."),
    dict(kicker="REGLA 2", title="Nada va a producción ni se publica sin mi «dale»", body="El agente prepara, prueba y me lo deja listo. La decisión es mía."),
    dict(kicker="REGLAS 3 Y 4", title="No borra datos sin mi OK. No gasta dinero sin mi sí", body="Ni en modelos, ni en suscripciones, ni en servicios. Lo que no se puede deshacer, lo decido yo."),
    dict(kicker="REGLA 5", title="Las claves nunca van al chat ni al repositorio", body="Ni contraseñas, ni tokens, ni claves de API. Y nunca «git add -A»."),
    dict(kicker="REGLA 6", title="Los datos reales de clientes no salen a terceros", body="No sin confirmarlo conmigo antes. La confianza de un cliente no se cambia por ir más rápido."),
    dict(kicker="REGLA 7", title="Lo que no se comprobó se dice «no verificado»", body="«Funciona» significa que se probó entero. Si no, se dice qué falta."),
    dict(kicker="CÓMO TRABAJAN", title="Un orquestador, varios expertos y un revisor", body="El orquestador fija el objetivo. Subagentes expertos hacen cada parte. Otro agente comprueba que sea correcto y verdadero."),
    dict(kicker="GRATIS", title="La plantilla, lista para copiar en tu repo", body=REPO + "\n\nCópiala como AGENTS.md o CLAUDE.md.\n¿Qué regla le añadirías tú?"),
]
RULES_EN = [
    dict(title="7 rules I give my AI agents", body="And why each one exists.\n\nThe first one overrides the rest."),
    dict(kicker="RULE 1", title="Always the truth", body="If it does not know, it says so. If it made something up, it tells me.\n\nWithout this rule, an agent fills the gaps with whatever sounds right."),
    dict(kicker="RULE 2", title="Nothing goes live without my go-ahead", body="The agent prepares, tests and hands it over. The decision is mine."),
    dict(kicker="RULES 3 AND 4", title="No deleting data without my OK. No spending without my yes", body="Not on models, subscriptions or services. What cannot be undone, I decide."),
    dict(kicker="RULE 5", title="Keys never go into the chat or the repo", body="No passwords, tokens or API keys. And never «git add -A»."),
    dict(kicker="RULE 6", title="Real client data never goes to third parties", body="Not without checking with me first. A client's trust is not traded for speed."),
    dict(kicker="RULE 7", title="Anything unchecked is labelled «not verified»", body="«It works» means tested end to end. If not, it says what is missing."),
    dict(kicker="HOW THEY WORK", title="One orchestrator, several experts, one reviewer", body="The orchestrator sets the goal. Expert subagents do each part. Another agent checks it is correct and true."),
    dict(kicker="FREE", title="The template, ready to copy into your repo", body=REPO + "\n\nCopy it as AGENTS.md or CLAUDE.md.\nWhich rule would you add?"),
]

# 2. Carrusel encargo / coste (ES)
BRIEF_ES = [
    dict(kind="big", big="87 %", title="de mi gasto en agentes fue releer contexto", body="1.150 dólares en cinco días. No en pensar: en releer."),
    dict(kind="compare", title="El mismo trabajo, de dos formas", rows=[("16 trabajos largos, agente principal", "~392 $", RED), ("Los mismos, ayudante con encargo y contexto limpio", "118 $", GREEN)], body="Un 70 % menos. Con el mismo modelo grande, un 72 %."),
    dict(kicker="DÓNDE SE IBA", title="66 relecturas completas: 385 $", body="Volver a una sesión enorme tras una pausa, o cambiar de modelo a mitad, obliga a releerlo todo desde cero."),
    dict(kind="code", title="La plantilla de encargo", code="# Objetivo\n<cómo se ve «terminado»>\n# Contexto (solo lo necesario)\n<archivos, decisiones tomadas>\n# Haz\n1. <paso>\n# No hagas\n- producción, borrar, gastar\n# Comprueba antes de informar\n<test, build, petición>\n# Informa\nhecho · NO VERIFICADO", body="El ayudante empieza en frío y no necesita la conversación."),
    dict(kind="check", title="Tres hábitos que cambié", items=["Sesión nueva al cambiar de tarea.", "No cambiar de modelo a mitad de sesión.", "Los encargos largos, a un ayudante, con todo por escrito."]),
    dict(kicker="GRATIS", title="La plantilla completa, en GitHub", body=REPO + "\n\n¿Mides lo que te cuesta cada sesión de IA?"),
]
BRIEF_EN = [
    dict(kind="big", big="87%", title="of my agent spend went on re-reading context", body="$1,150 in five days. Not thinking: re-reading."),
    dict(kind="compare", title="Same work, two ways", rows=[("16 long jobs, main agent", "~$392", RED), ("Same jobs, helper with a brief and clean context", "$118", GREEN)], body="70% less. With the same large model, 72%."),
    dict(kicker="WHERE IT WENT", title="66 full re-reads: $385", body="Going back to a huge session after a break, or switching models halfway, forces a re-read from scratch."),
    dict(kind="code", title="The brief template", code="# Goal\n<what «done» looks like>\n# Context (only what is needed)\n<files, decisions taken>\n# Do\n1. <step>\n# Do NOT\n- production, delete, spend\n# Verify before reporting\n<test, build, request>\n# Report\ndone · NOT VERIFIED", body="The helper starts cold and never needs the chat."),
    dict(kind="check", title="Three habits I changed", items=["A new session when the task changes.", "No switching models mid-session.", "Long jobs go to a helper, everything in writing."]),
    dict(kicker="FREE", title="The full template, on GitHub", body=REPO + "\n\nDo you measure what each AI session costs?"),
]

# 3. Post gemini (imagen única)
GEMINI = [dict(kind="compare", kicker="MODELO RETIRADO · 1 DIC 2026", title="Medir antes de cambiar", rows=[("Coste de redacción por escritura, antes", "0,150 $", RED), ("Después, con el modelo nuevo", "0,071 $", GREEN), ("132 borradores de prueba (tope 30 $)", "20,21 $", WHITE)], body="Y una regla nueva: el vigilante también avisa cuando el que falla es él.")]

# 4. Post 5 MVPs (imagen única)
MVPS = [dict(kind="compare", kicker="OCTUBRE 2025", title="5 productos en 5 semanas", rows=[("Ejecución", "10/10", GREEN), ("Interés del público", "2/10", RED)], body="Nadie compra una app más. Compra a alguien que convierte un problema concreto en algo que funciona.")]

# 5. Carrusel fallos silenciosos (ES)
SILENT_ES = [
    dict(kind="big", big="9", title="meses fallando sin que nadie lo viera", body="Una búsqueda devolvía «sin resultados». En realidad era un error 404."),
    dict(kind="code", title="El error que no parece un error", code="try {\n  return await embed(texto)\n} catch {\n  return []   # el bug\n}", body="Para el resto del sistema, simplemente no había resultados."),
    dict(kind="check", title="Las reglas que salieron de ahí", items=["Un fallo de un proveedor nunca se tapa con un valor vacío.", "«Sin resultados» y «no pude comprobar» son respuestas distintas.", "Todo vigilante avisa también cuando falla él.", "Las alertas las mira primero un agente; a mí solo me llega lo que pide una decisión."]),
    dict(kind="check", title="Si dependes de un modelo de IA", items=["¿Qué modelos llamas y desde qué archivos?", "¿Cuándo retira cada uno el proveedor?", "¿El reemplazo se midió con tus datos?", "¿Qué ve el usuario si la llamada falla?"]),
    dict(kicker="GRATIS", title="La lista completa, en GitHub", body=REPO + "\n\n¿Cuántos «sin resultados» de tu producto son errores?"),
]

# 6. Post PikMorph (imagen única)
SCOPE = [dict(kind="check", kicker="ANTES DE ABRIR UN PROYECTO", title="Dos reglas que me pongo ahora", items=["Un solo trabajo por producto. Si no lo puedo decir en una frase, no está claro.", "Antes de crear un producto nuevo, preguntar si es un módulo de uno que ya existe."]), ]
SCOPE[0]["title"] = "Construir es lo fácil. Lo difícil es decidir qué no construir."

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, pages, lang in [
        ("01-reglas-agentes-es", RULES_ES, "es"), ("02-rules-agents-en", RULES_EN, "en"),
        ("03-encargo-subagentes-es", BRIEF_ES, "es"), ("04-subagent-brief-en", BRIEF_EN, "en"),
        ("05-gemini-es", GEMINI, "es"), ("06-cinco-mvps-es", MVPS, "es"),
        ("07-fallos-silenciosos-es", SILENT_ES, "es"), ("08-un-trabajo-por-producto-es", SCOPE, "es"),
    ]:
        print(build(name, pages, lang))
