from uuid import UUID, uuid4
from dataclasses import field
from typing import Optional
from pydantic import BaseModel
from app.src.domain.entities.task import Task
from datetime import datetime, timezone


class TaskOutput(BaseModel):
  id: UUID
  title: str
  description: str
  user_id: UUID
  created_at: datetime
  due_date: datetime | None

  @classmethod
  def from_entity(cls, task: Task):
    return cls(
      id=task.id,
      title=task.title,
      created_at=task.created_at,
    )

class TaskInput(BaseModel):
  id: UUID = field(default_factory=datetime.now(timezone.utc))
  title: str
  description: str
  user_id: Optional[UUID | None] 
  created_at: datetime = field(default_factory=datetime.now(timezone.utc))
  due_date: Optional[datetime | None]

  def to_entity(self) -> Task:
    return Task(
      id=self.id,
      user_id=self.user_id,
      title=self.title,
      description=self.description,
      created_at=self.created_at,
    )