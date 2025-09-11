import uuid
import pytest
from app.src.adapters.repositories.in_memory_task_repository import InMemoryTaskRepository
from app.src.domain.entities.task import Task
from app.src.domain.repositories.task_repository import TaskRepository
from app.src.domain.exceptions.task_not_found import TaskNotFound
from app.src.use_cases.create_task_use_case import CreateTaskUseCase

@pytest.fixture
def repo() -> TaskRepository:
  return InMemoryTaskRepository()

@pytest.fixture
def create_task_use_case(repo) -> CreateTaskUseCase:
  return CreateTaskUseCase(repo)

@pytest.mark.asyncio
async def test_create_task_use_case(create_task_use_case):
  task = Task(id = uuid.uuid4(), user_id = uuid.uuid4(), title = "Test Task", description = "Some details")

  result = await create_task_use_case(task=task)
  assert result.id == task.id
  assert result.title == task.title
  assert result.description == task.description
