import uuid
import pytest
from src.infra.repositories.in_memory_task_repository import InMemoryTaskRepository
from src.domain.repositories.task_repository import TaskRepositoryInterface
from src.domain.exceptions.task_not_found import TaskNotFound
from src.application.use_cases.detail_task_use_case import DetailTaskUseCase

@pytest.fixture
def 