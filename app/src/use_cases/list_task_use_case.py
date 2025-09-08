from uuid import UUID
from typing import Any, List
from app.src.domain.entities.task import Task
from app.src.domain.repositories.task_repository import TaskRepository

class ListTaskUseCase:
  def __init__(self, task_repository: TaskRepository):
    self.__task_repository = task_repository

  async def __call__(self, **filters: Any) -> List[Task]:
    return  await self.__task_repository.list(**filters)