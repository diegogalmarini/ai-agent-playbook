from carousel_style import *

REPO = "github.com/diegogalmarini/ai-agent-playbook"

GEMINI = [
    cover("Mañana, 1 de diciembre", "Google apaga\nun modelo.", "Mi SaaS dependía de él.", "Y el vigilante que debía avisarme llevaba días fallando en silencio."),
    score("Las fechas", [("Google mueve su página de avisos", "4 nov", INK), ("Lo detectamos", "12 nov", MARK), ("Días que quedaban", "19", MARK)], "El control fallaba y no lo decía.", ring=2, big=110),
    steps("Lo que hice", [("Medir antes de cambiar", "Tope de 30 $ y carpetas de prueba reservadas."), ("132 borradores de prueba", "Costaron 20,21 $ en total."), ("Cambiar con respaldo", "Al día siguiente, otro modelo y respaldos ya medidos.")]),
    score("El resultado", [("Coste por escritura, antes", "0,150 $", GREY), ("Con el modelo nuevo", "0,071 $", GREEN)], "Menos de la mitad, y medido con datos reales.", ring=1, big=120),
    quote("La regla nueva", "El vigilante también avisa", "cuando el que falla es él.", None),
    closing("Tu turno", "Si tu producto depende de un modelo de IA, ¿sabes qué día deja de existir?", "Cada proveedor publica cuándo retira sus modelos. Apúntalo antes de que te lo recuerde un error.", "Te leo en los comentarios."),
]

SILENT = [
    cover("Un error que nadie vio", "9 meses\nfallando.", "Sin un solo aviso.", "Una búsqueda devolvía «sin resultados». En realidad era un error 404."),
    code("Por qué", "El error que no parece un error", "try {\n  return await embed(texto)\n} catch {\n  return []    // el bug\n}", "Para el resto del sistema, simplemente no había resultados."),
    score("Las fechas", [("El modelo empieza a fallar", "14 ene", MARK), ("Lo cerramos, tras una auditoría", "10 oct", GREEN)], "El arreglo técnico fue rápido. Lo importante fue la regla.", ring=0, big=110),
    steps("Las reglas que salieron de ahí", [("Nunca tapar un fallo", "con un valor vacío. Cada error avisa."), ("«Sin resultados» no es «no pude»", "Son dos respuestas distintas."), ("Las alertas, primero a un agente", "A mí solo me llega lo que pide una decisión.")]),
    quote("La frase", "Un sistema que falla en silencio", "no falla una vez. Falla todos los días.", None),
    closing("Tu turno", "¿Cuántos «sin resultados» de tu producto son errores?", "La lista completa para revisarlo está gratis en GitHub: " + REPO, "Te leo en los comentarios."),
]

BRIEF_EN = [
    cover("What I measured", "87% of my\nagent spend…", "…was re-reading context.", "$1,150 in five days, in my own projects. Not thinking. Re-reading.", swipe="Swipe  →", tsize=130),
    score("Same work, two ways", [("16 long jobs, main agent", "~$392", MARK), ("Same jobs, helper with a brief", "$118", GREEN)], "70% less. With the same large model, 72%.", ring=1, big=120),
    score("Where it went", [("Full re-reads from scratch", "66", MARK), ("What they cost", "$385", MARK)], "A huge session after a break, or a model switch halfway, re-reads everything.", ring=None, big=130),
    code("The template", "The brief I give a helper", "# Goal\n<what «done» looks like>\n# Context (only what's needed)\n<files, decisions taken>\n# Do\n1. <step>\n# Do NOT\n- production, delete, spend\n# Verify before reporting\n<test, build, request>\n# Report\ndone · NOT VERIFIED", "The helper starts cold and never needs the chat."),
    steps("Three habits I changed", [("New session, new task", "Don't drag old context into new work."), ("No model switch mid-session", "It forces a full re-read."), ("Long jobs go to a helper", "With everything it needs, in writing.")]),
    closing("Your turn", "Do you measure what each AI session costs?", "The full brief template is free on GitHub: " + REPO, "Tell me in the comments."),
]

SCOPE = [
    cover("Un error que repito", "Querer que\nun programa\nlo haga todo.", "Y terminar haciéndolo indefinido.", "Lo dije en noviembre, hablando de una de mis apps de imágenes con IA.", tsize=120),
    steps("Cómo pasó", [("Empezó con un trabajo claro", "Convertir y redimensionar fotos. Aún es lo que más uso."), ("Le fui sumando cosas", "Cada una tenía sentido sola."), ("Juntas, sin un trabajo claro", "Difícil de explicar. Más difícil de vender.")], mark_first=False),
    quote("Me pasó otra vez", "Un agente de atención al cliente", "que empecé como producto propio encaja mejor como módulo de otro.", "Lo vi tarde."),
    steps("Dos reglas antes de abrir un proyecto", [("Un solo trabajo por producto", "Si no lo puedo decir en una frase, no está claro."), ("¿Es un módulo de algo que ya existe?", "Preguntarlo antes de crear un producto nuevo.")]),
    closing("Tu turno", "¿Qué producto tienes que hace demasiadas cosas?", "Construir es lo fácil. Lo difícil es decidir qué no construir.", "Te leo en los comentarios."),
]

if __name__ == "__main__":
    for name, deck in [("05-gemini-es", GEMINI), ("07-fallos-silenciosos-es", SILENT), ("04-subagent-brief-en", BRIEF_EN), ("08-un-trabajo-por-producto-es", SCOPE)]:
        print(render(name, deck))

MVPS = [
    cover("Octubre de 2025 · lo que aprendí", "5 productos\nen 5 semanas.", "Los terminé todos.\nCasi nadie los quiso.", "Esto es lo que cambié desde entonces en cómo decido qué construir."),
    score("Mi nota de aquel mes", [("Ejecución", "10/10", GREEN), ("Interés del público", "2/10", MARK)], "Lo hice todo bien… menos lo que importaba.", ring=1, big=150),
    listing("Los cinco", ["TokenWatcher", "NutriChefAI", "MixMasterAI", "LegalClaro", "VozActiva"], right="terminado", note="Los posts que los presentaban apenas tuvieron interacción. Hoy no todos siguen en marcha."),
    quote("Lo que me costó aceptar", "Nadie compra una app más.", "Compra a alguien que convierte un problema concreto en algo que funciona.", "La app es solo la prueba."),
    steps("El orden que sigo ahora", [("El problema", "de alguien con nombre y apellido."), ("La versión más pequeña", "que lo resuelve. Nada más."), ("Contarlo con números", "cuando ya funciona para esa persona.")]),
    closing("Tu turno", "¿Cuántos productos tienes terminados que nadie te pidió?", "Los proyectos que hoy me dan ingresos nacieron de un problema concreto de alguien, no de una idea mía.", "Te leo en los comentarios."),
]
