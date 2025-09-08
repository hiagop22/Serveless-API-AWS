from uuid import UUID
from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from app.src.domain.entities.task import Task
from app.src.drivers.rest.schemas.task import TaskOutput, TaskInput
from app.src.adapters.repositories.in_memory_task_repository import InMemoryTaskRepository
from app.src.domain.repositories.task_repository import TaskRepository
from app.src.use_cases.create_task_use_case import CreateTaskUseCase
from app.src.use_cases.detail_task_use_case import DetailTaskUseCase
from app.src.use_cases.list_task_use_case import ListTaskUseCase

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_repository() -> TaskRepository:
  return InMemoryTaskRepository()

def create_task_use_case(repository = Depends(get_repository)) -> CreateTaskUseCase:
  return CreateTaskUseCase(repository)

def detail_task_use_case(repository = Depends(get_repository)) -> DetailTaskUseCase:
  return DetailTaskUseCase(repository)

def list_task_use_case(repository = Depends(get_repository)) -> ListTaskUseCase:
  return ListTaskUseCase(repository)

@router.post("/", response_model=TaskOutput, status_code=status.HTTP_201_CREATED)
async def create_task(
  data: TaskInput,
  use_case: Annotated[CreateTaskUseCase, Depends(create_task_use_case)]
):
  return await use_case(data.to_entity())

@router.get("/", response_model=List[TaskOutput])
async def list_task(
  use_case: Annotated[ListTaskUseCase, Depends(list_task_use_case)]
):
  return await use_case()

@router.get("/{task_id}", response_model=TaskOutput)
async def detail_task(
  task_id: UUID,
  use_case: Annotated[DetailTaskUseCase, Depends(detail_task_use_case)]
):
  return await use_case(task_id)