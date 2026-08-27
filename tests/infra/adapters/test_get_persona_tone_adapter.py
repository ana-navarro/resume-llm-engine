from infra.adapters.get_persona_tone_adapter import TONE_TEXT, GetPersonaToneAdapter


def test_execute_returns_the_hardcoded_tone_text():
    assert GetPersonaToneAdapter().execute() == TONE_TEXT


def test_tone_text_covers_the_three_required_traits():
    lowered = TONE_TEXT.lower()
    assert "professional" in lowered
    assert "empathetic" in lowered
    assert "resolution-oriented" in lowered
