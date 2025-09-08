from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from app.src.domain.exceptions.task_not_found import TaskNotFound

def handle_errors(exc: Exception) -> JSONResponse:
  if hasattr(exc, "status_code") and hasattr(exc, "name") and hasattr(exc, "message"):
    return JSONResponse(
      status_code=exc.status_code,
      content={
        "erros": [{
          "title": exc.name,
          "detail": exc.message
        }]
      }
    )
  
  return JSONResponse(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    content={
      "errors": [{
        "title": "Server Error",
        "detail": "Internal server error"
      }]
    }
  )


def exception_container(app: FastAPI) -> None:

  @app.exception_handler(TaskNotFound)
  async def unified_exception_handler(request: Request, exc: Exception):
    return handle_errors(exc)