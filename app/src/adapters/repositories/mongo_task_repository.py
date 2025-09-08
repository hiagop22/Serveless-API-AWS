from uuid import UUID
from typing import Any
from datetime import datetime
from bson.binary import Binary, UUID_SUBTYPE
from motor.motor_asyncio import AsyncIOMotorClient
from app.src.domain.repositories.task_repository import TaskRepository
from app.src.domain.entities.task import Task
from app.src.domain.exceptions.task_not_found import TaskNotFound


class MongoTaskRepository(TaskRepository):
  def __init__(self, mongo_client: AsyncIOMotorClient, db_name: str = "tasks_db") -> None:
    self.client = mongo_client
    self.db = self.client[db_name]
    self.collection = self.db["tasks"]

  async def get(self, **filters: Any) -> Task | None:
    filters_str = self._convert_uuid_filters(filters)
    doc = await self.collection.find_one(filters_str)

    if not doc:
      return None
    
    return self._doc_to_entity(doc)
  
  async def list(self, **filters: Any) -> list[Task]:
    filters_str = self._convert_uuid_filters(filters)
    cursor = self.collection.find(filters_str)
    tasks = []

    async for doc in cursor:
      tasks.append(self._doc_to_entity(doc))

    return tasks

  async def add(self, task: Task) -> Task:
    doc = self._entity_to_doc(task)
    await self.collection.insert_one(doc)

    return task

  async def update(self, task: Task) -> Task:
    result = await self.collection.update_one(
        {"id": str(task.id)},
        {"$set": {
            "title": task.title,
            "description": task.description,
            "user_id": str(task.user_id) if task.user_id else None,
            "due_date": task.due_date.isoformat() if task.due_date else None
        }}
      )

    if result.matched_count == 0:
      raise TaskNotFound(f"Task {task.id} not found")
  
    return task

  async def delete(self, task_id: UUID) -> None:
    result = await self.collection.delete_one({"id": str(task_id)})

    if result.deleted_count == 0:
      raise TaskNotFound(f"Task {task_id} not found")

  def _entity_to_doc(self, task: Task) -> dict:
    return {
        "id": str(task.id),
        "title": task.title,
        "description": task.description,
        "user_id": str(task.user_id) if task.user_id else None,
        "created_at": task.created_at.isoformat(),
        "due_date": task.due_date.isoformat() if task.due_date else None,
    }

  def _doc_to_entity(self, doc: dict) -> Task:
    return Task(
        id=UUID(doc["id"]),
        title=doc["title"],
        description=doc.get("description"),
        user_id=UUID(doc["user_id"]) if doc.get("user_id") else None,
        created_at=datetime.fromisoformat(doc["created_at"]),
        due_date=datetime.fromisoformat(doc["due_date"]) if doc.get("due_date") else None
    )
  
  def _convert_uuid_filters(self, filters: dict) -> dict:
    result = filters.copy()
    for k, v in filters.items():
      if isinstance(v, UUID):
          result[k] = str(v)

    return result