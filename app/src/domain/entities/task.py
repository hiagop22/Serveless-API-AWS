from datetime import datetime
from uuid import uuid4, UUID
from app.src.domain.entities.status import Status

class Task:
  def __init__(self, title: str, user_id: UUID, description: str = None):
    self.id: UUID = uuid4()
    self.title: str = title
    self.description: str = description
    self.user_id: UUID = user_id
    self.status: Status = Status.TODO
    self.created_at: datetime = datetime.now()
    self.due_date: datetime | None = None

  def mark_done(self):
    self.status = Status.DONE
  
  def mark_in_progress(self):
    self.status = Status.IN_PROGRESS
