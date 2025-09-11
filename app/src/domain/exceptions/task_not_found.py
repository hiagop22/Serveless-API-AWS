class TaskNotFound(Exception):

  def __init__(self) -> None:
    self.message = f"Task not found"
    self.name = "TaskNotFound"
    self.status_code = 404
    super().__init__(self.message)