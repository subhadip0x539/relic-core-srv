import asyncio
import json
from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from internal.deps.common import EventManager, get_event_manager
from internal.deps.auth import get_api_key

router = APIRouter(prefix="/stream")


@router.get("/{api_key}")
async def flag_stream(
    request: Request,
    manager: EventManager = Depends(get_event_manager),
    _: str = Depends(get_api_key),
):
    service_id = request.state.service_id

    queue = await manager.connect(service_id)

    async def event_generator():
        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    message = await asyncio.wait_for(queue.get(), timeout=15)
                    yield f"data: {json.dumps(message)}\n\n"
                except asyncio.TimeoutError:
                    yield ": keep-alive\n\n"
        finally:
            manager.disconnect(service_id, queue)

    return StreamingResponse(event_generator(), media_type="text/event-stream")
