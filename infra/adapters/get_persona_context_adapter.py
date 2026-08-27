from infra.ports.get_persona_context_port import GetPersonaContextPort

# PLACEHOLDER: this content does not come from the resume PDFs (per design) but it also isn't the
# candidate's real biographical content yet -- it MUST be replaced with Ana Elisa's actual career
# objective and interpersonal skills before this is used in production. See tasks/persona-prompt-structure.
CONTEXT_TEXT = """\
- Career objective: [PREENCHER: objetivo de carreira real de Ana Elisa]
- Interpersonal skills: [PREENCHER: habilidades interpessoais reais de Ana Elisa]"""


class GetPersonaContextAdapter(GetPersonaContextPort):
    def execute(self) -> str:
        return CONTEXT_TEXT
