from uuid import UUID
from app.src.domain.entities.task import Task
from app.src.domain.repositories.task_repository import TaskRepository
from app.src.domain.exceptions.task_not_found import TaskNotFound

class DetailTaskUseCase:
  def __init__(self, task_repository: TaskRepository):
    self.__task_repository = task_repository

  async def __call__(self, task_id: UUID) -> Task:
    task = await self.__task_repository.get(id=task_id)
    if not task:
      raise TaskNotFound
    return task