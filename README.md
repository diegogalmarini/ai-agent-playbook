# AI Agent Playbook

Reglas, plantillas y skills que uso para trabajar con agentes de IA (Claude Code, Codex, Gemini) en productos reales que llegan a producción.
Todo sale de errores y números medidos en mis proyectos, no de teoría.

*Rules, briefs and skills I use with AI coding agents on real products. Everything here comes from mistakes and numbers measured in my own projects. Templates are in English so any agent can use them as they are.*

| Archivo | Para qué sirve |
| --- | --- |
| [`AGENTS.template.md`](AGENTS.template.md) | Las 7 reglas que pongo en la raíz de cada proyecto. Cópialo como `AGENTS.md` o `CLAUDE.md`. |
| [`briefs/subagent-brief.md`](briefs/subagent-brief.md) | La plantilla de encargo para delegar un trabajo largo a un subagente con el contexto limpio (un 70 % menos de coste en mis mediciones). |
| [`playbooks/no-silent-failures.md`](playbooks/no-silent-failures.md) | Cómo evitar que un fallo quede en silencio, y la lista para cuando un proveedor retira el modelo del que dependes. |
| [`playbooks/context-full-handoff.md`](playbooks/context-full-handoff.md) | Qué hace un agente cuando se le llena el contexto: nunca quedarse a medias. |
| [`skills/linkedin-weekly/SKILL.md`](skills/linkedin-weekly/SKILL.md) | La skill que prepara mi semana de LinkedIn a partir de mis notas. Nunca publica sola. |

## Cómo usarlo en 2 minutos

1. Copia `AGENTS.template.md` a la raíz de tu repo como `AGENTS.md` (y como `CLAUDE.md` si usas Claude Code).
2. Cambia `<OWNER>` por tu nombre.
3. La próxima vez que delegues algo largo, rellena `briefs/subagent-brief.md` antes de lanzarlo.

## Quién soy

Diego Galmarini, Director de Producto y Tecnología. Construyo SaaS con IA que llegan a producción.
[LinkedIn](https://www.linkedin.com/in/diegogalmarini/)

Si te sirve, una estrella ayuda a que lo encuentre más gente. Y si añades una regla buena, abre un PR.

Licencia MIT.
