from fastapi import APIRouter
from .workspace import router as workspace_router
from .service import router as service_router
from .environment import router as environment_router
from .flag import router as flag_router
from .apikey import router as api_key_router
from .feature import router as feature_router
from .stream import router as stream_router

v1 = APIRouter(prefix="/v1")

v1.include_router(workspace_router)
v1.include_router(service_router)
v1.include_router(environment_router)
v1.include_router(flag_router)
v1.include_router(api_key_router)
v1.include_router(feature_router)
v1.include_router(stream_router)

router = APIRouter()


@router.get("/ping")
def ping():
    return {"message": "pong"}


router.include_router(v1)
