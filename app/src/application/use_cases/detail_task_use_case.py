from src.domain.entities.task import Task
from uuid import UUID
from src.domain.repositories.task_repository import TaskRepositoryInterface
from src.domain.exceptions.task_not_found import TaskNotFound

class DetailTaskUseCase:
  def __init__(self, task_repository: TaskRepositoryInterface):
    self.__task_repository = task_repository

  async def __call__(self, task_id: UUID) -> Task:
    task = await self.__task_repository.get(task_id=task_id)
    if not task:
      raise TaskNotFound
    return task