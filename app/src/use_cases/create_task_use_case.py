from uuid import uuid4
from app.src.domain.entities.task import Task
from app.src.domain.repositories.task_repository import TaskRepository
from app.src.domain.exceptions.task_not_found import TaskNotFound

class CreateTaskUseCase:
  def __init__(self, task_repository: TaskRepository):
    self.__task_repository = task_repository

  async def __call__(self, task: Task) -> Task:
    if task.id is None:
      task.id = uuid4()
    
    task = await self.__task_repository.add(task=task)
    return task