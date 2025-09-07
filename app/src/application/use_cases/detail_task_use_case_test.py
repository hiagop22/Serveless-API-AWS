import uuid
import pytest
from app.src.infra.repositories.in_memory_task_repository import InMemoryTaskRepository
from app.src.domain.entities.task import Task
from app.src.domain.repositories.task_repository import TaskRepository
from app.src.domain.exceptions.task_not_found import TaskNotFound
from app.src.application.use_cases.detail_task_use_case import DetailTaskUseCase

@pytest.fixture
def repo() -> TaskRepository:
  return InMemoryTaskRepository()

@pytest.fixture
def detail_task_use_case(repo) -> DetailTaskUseCase:
  return DetailTaskUseCase(repo)

@pytest.mark.asyncio
async def test_detail_task_use_case(detail_task_use_case, repo):
  task = Task(user_id = uuid.uuid4(), title = "Test Task", description = "Some details")
  await repo.seed([task])

  result = await detail_task_use_case(task_id=task.id)
  assert result.id == task.id
  assert result.title == task.title
  assert result.description == task.description

@pytest.mark.asyncio
async def test_task_not_found(detail_task_use_case, repo):
  fake_id = uuid.uuid4()
  
  with pytest.raises(TaskNotFound):
    await detail_task_use_case(fake_id)