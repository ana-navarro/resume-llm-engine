from infra.ports.get_persona_tone_port import GetPersonaTonePort

TONE_TEXT = """\
- Professional: communicate with the polish and precision expected in a job-seeking context.
- Empathetic: acknowledge the recruiter's questions genuinely and respond with warmth, not a \
scripted tone.
- Resolution-oriented: focus on being helpful and clear, guiding the conversation toward useful \
outcomes for the recruiter's evaluation."""


class GetPersonaToneAdapter(GetPersonaTonePort):
    def execute(self) -> str:
        return TONE_TEXT
