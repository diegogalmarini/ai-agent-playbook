from carousel_style import *
REPO = "github.com/diegogalmarini/ai-agent-playbook"

RULES_ES = [
    cover("Lo que tienen mis agentes", "7 reglas\npara mis\nagentes de IA.", "Y por qué existe cada una.", "La primera manda sobre las demás.", tsize=130),
    quote("Regla 1", "Siempre la verdad.", "Si no lo sabe, dice «no lo sé». Si lo inventó, me lo dice.", "Sin esta regla, un agente rellena huecos con lo que suena bien."),
    steps("Reglas 2 a 4 · lo decido yo", [("Nada va a producción", "ni se publica sin mi «dale». El agente lo deja listo y probado."), ("No borra datos", "sin mi OK. Lo que no se deshace, lo decido yo."), ("No gasta dinero", "sin mi sí. Ni modelos, ni suscripciones, ni servicios.")], mark_first=False, start=2),
    steps("Reglas 5 a 7 · lo que no sale de casa", [("Las claves, nunca al chat", "ni al repositorio. Y nunca «git add -A»."), ("Los datos de clientes", "no salen a terceros sin confirmarlo conmigo."), ("Lo no comprobado", "se dice «no verificado». «Funciona» es probado entero.")], mark_first=False, start=5),
    steps("Cómo trabajan", [("Un orquestador", "fija el objetivo y reparte."), ("Varios expertos", "hacen cada parte."), ("Un revisor", "comprueba que sea correcto y verdadero.")]),
    closing("Gratis", "¿Qué regla le añadirías tú?", "La plantilla, lista para copiar como AGENTS.md o CLAUDE.md: " + REPO, "Te leo en los comentarios."),
]

RULES_EN = [
    cover("What my agents follow", "7 rules\nfor my\nAI agents.", "And why each one exists.", "The first one overrides the rest.", swipe="Swipe  →", tsize=130),
    quote("Rule 1", "Always the truth.", "If it does not know, it says so. If it made something up, it tells me.", "Without it, an agent fills gaps with what sounds right."),
    steps("Rules 2 to 4 · I decide", [("Nothing goes live", "without my yes. The agent prepares and tests it."), ("No deleting data", "without my OK. What can't be undone, I decide."), ("No spending", "without my yes. Not on models, plans or services.")], mark_first=False, start=2),
    steps("Rules 5 to 7 · what stays in the house", [("Keys never go in the chat", "or the repo. And never «git add -A»."), ("Real client data", "never goes to third parties without asking me."), ("Anything unchecked", "is labelled «not verified». «It works» means tested.")], mark_first=False, start=5),
    steps("How they work", [("One orchestrator", "sets the goal and splits the work."), ("Several experts", "each do one part."), ("One reviewer", "checks it is correct and true.")]),
    closing("Free", "Which rule would you add?", "The template, ready to copy as AGENTS.md or CLAUDE.md: " + REPO, "Tell me in the comments."),
]

BRIEF_ES = [
    cover("Lo que medí", "87 % de mi\ngasto en\nagentes…", "…fue releer contexto.", "1.150 dólares en cinco días, en mis proyectos. No en pensar: en releer.", tsize=120),
    score("El mismo trabajo, de dos formas", [("16 trabajos largos, agente principal", "~392 $", MARK), ("Los mismos, ayudante con encargo", "118 $", GREEN)], "Un 70 % menos. Con el mismo modelo grande, un 72 %.", ring=1, big=120),
    score("Dónde se iba", [("Relecturas completas desde cero", "66", MARK), ("Lo que costaron", "385 $", MARK)], "Volver a una sesión enorme tras una pausa, o cambiar de modelo a mitad, lo relee todo.", ring=None, big=130),
    code("La plantilla", "El encargo que le doy a un ayudante", "# Objetivo\n<cómo se ve «terminado»>\n# Contexto (solo lo necesario)\n<archivos, decisiones tomadas>\n# Haz\n1. <paso>\n# No hagas\n- producción, borrar, gastar\n# Comprueba antes de informar\n<test, build, petición>\n# Informa\nhecho · NO VERIFICADO", "El ayudante empieza en frío y no necesita la conversación."),
    steps("Tres hábitos que cambié", [("Sesión nueva, tarea nueva", "No arrastrar contexto viejo a un trabajo nuevo."), ("No cambiar de modelo a mitad", "Obliga a releerlo todo."), ("Los encargos largos, a un ayudante", "Con todo lo que necesita, por escrito.")]),
    closing("Tu turno", "¿Mides lo que te cuesta cada sesión de IA?", "La plantilla completa, gratis en GitHub: " + REPO, "Te leo en los comentarios."),
]

if __name__ == "__main__":
    for name, deck in [("01-reglas-agentes-es", RULES_ES), ("02-rules-agents-en", RULES_EN), ("03-encargo-subagentes-es", BRIEF_ES)]:
        print(render(name, deck))
