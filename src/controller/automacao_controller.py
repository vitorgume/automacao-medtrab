from fastapi import APIRouter
from fastapi.params import Depends

from src.models.automacao_model import AutomacaoModel
from src.service.automacao_service import AutomacaoService

router = APIRouter()

automacao_service = AutomacaoService()

def get_automacao_service():
    # Aqui você pode, no futuro, usar cache, escopo de request, etc.
    return AutomacaoService()

@router.post("/integracoes")
def criar_integracao(
        model: AutomacaoModel,
        service: AutomacaoService = Depends(get_automacao_service)
):
    return service.criar_integracao(model)