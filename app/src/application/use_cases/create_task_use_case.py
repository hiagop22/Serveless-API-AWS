from src.domain.entities.task import Task
from src.application.repositories.task_repository import TaskRepositoryInterface

class CreateTaskUseCase:
  def __init__(self, task_repository: TaskRepositoryInterface):
    self.__task_repository = task_repository

  async def __call__(self, task: Task) -> Task:
    task = await self.__task_repository.add(task)
    return task