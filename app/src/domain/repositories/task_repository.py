from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from app.src.domain.entities.task import Task

class TaskRepository(ABC):
  @abstractmethod
  async def get(self, **filters: Any) -> Task | None:
    pass

  @abstractmethod
  async def list(self, **filters: Any) -> list[Task]:
    pass

  @abstractmethod
  async def add(self, task: Task) -> Task:
    pass

  @abstractmethod
  async def update(self, **filters: Any) -> Task:
    pass

  @abstractmethod
  async def delete(self, task_id: UUID) -> None:
    pass