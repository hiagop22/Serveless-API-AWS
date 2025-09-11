from uuid import UUID
from typing import Any, List
from src.domain.repositories.task_repository import TaskRepository
from src.domain.entities.task import Task


class InMemoryTaskRepository(TaskRepository):
  def __init__(self) -> None:
    self._tasks: dict[str, Task] = {}

  async def get(self, **filters: Any) -> Task | None:
    for task in self._tasks.values():
      if all(getattr(task, key, None) == value for key, value in filters.items()):
        return task

    return None
  
  async def list(self, **filters: Any) -> list[Task]:
    if not filters:
      return list(self._tasks.values())
    return [
      task for task in self._tasks.values()
      if all(getattr(task, key, None) == value for key, value in filters.items())
    ]

  async def add(self, task: Task) -> Task:
    self._tasks[task.id] = task
    return task

  async def update(self, task: Task) -> Task:
    if task.id not in self._tasks:
      raise ValueError(f"Task with id={task.id} not found")
    self._tasks[task.id] = task
    return task

  async def delete(self, task_id: UUID) -> None:
    if task_id in self._tasks:
      del self._tasks[task_id]

  async def seed(self, tasks: List[Task]) -> None:
    for task in tasks:
      self._tasks[task.id] = task