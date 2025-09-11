import pytest
from uuid import uuid4
import datetime
from datetime import datetime, timezone
from src.domain.entities.task import Task
from src.adapters.repositories.in_memory_task_repository import InMemoryTaskRepository
from src.domain.repositories.task_repository import TaskRepository
from src.use_cases.list_task_use_case import ListTaskUseCase

@pytest.fixture
def repo() -> TaskRepository:
  return InMemoryTaskRepository()

@pytest.fixture
def list_task_use_case(repo) -> ListTaskUseCase:
  return ListTaskUseCase(repo)

@pytest.mark.asyncio
async def test_list_task_use_case(list_task_use_case, repo):
  tasks = [
      Task(id=uuid4(), user_id=uuid4(), title="Task 1", description="First task", created_at=datetime.now(timezone.utc)),
      Task(id=uuid4(), user_id=uuid4(), title="Task 2", description="Second task", created_at=datetime.now(timezone.utc)),
  ]
  await repo.seed(tasks)

  result = await list_task_use_case()

  assert len(tasks) == len(result)
  assert set([t.title for t in tasks]) == set([t.title for t in result])
  assert set([t.description for t in tasks]) == set([t.description for t in result])
  assert set([t.created_at for t in tasks]) == set([t.created_at for t in result])