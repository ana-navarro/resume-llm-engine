from infra.adapters.get_persona_rules_adapter import RULES_TEXT, GetPersonaRulesAdapter


def test_execute_returns_the_hardcoded_rules_text():
    assert GetPersonaRulesAdapter().execute() == RULES_TEXT


def test_rules_text_forbids_fabricating_resume_content():
    assert "invent" in RULES_TEXT.lower()
