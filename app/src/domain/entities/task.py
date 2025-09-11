from datetime import datetime
from uuid import uuid4, UUID

class Task:
  def __init__(self, 
               id: UUID, 
               title: str, 
               user_id: UUID, 
               description: str = None,
               created_at: datetime = None,
               due_date: datetime = None,
               ):
    self.id: UUID = id
    self.title: str = title
    self.description: str = description
    self.user_id: UUID = user_id
    self.created_at: datetime = created_at
    self.due_date: datetime | None = due_date
