from fastapi import APIRouter

from applications.controllers.get_persona_prompt_controller import (
    GetPersonaPromptController,
)
from domain.usecases.build_persona_prompt_usecase import BuildPersonaPromptUseCase
from infra.adapters.get_persona_context_adapter import GetPersonaContextAdapter
from infra.adapters.get_persona_rules_adapter import GetPersonaRulesAdapter
from infra.adapters.get_persona_tone_adapter import GetPersonaToneAdapter

router = APIRouter()

_usecase = BuildPersonaPromptUseCase(
    get_persona_rules=GetPersonaRulesAdapter(),
    get_persona_context=GetPersonaContextAdapter(),
    get_persona_tone=GetPersonaToneAdapter(),
)
_controller = GetPersonaPromptController(_usecase)


@router.get("/prompt")
def get_persona_prompt():
    return _controller.handle()
