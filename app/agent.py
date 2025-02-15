import importlib
from app.utils.parser import parse_task
from app.utils.file_utils import write_log

class Agent:
    def __init__(self):
        self.task_mapping = {
            "A1": "app.tasks.task_a1",
            "A2": "app.tasks.task_a2",
            "A3": "app.tasks.task_a3",
            "A4": "app.tasks.task_a4",
            "A5": "app.tasks.task_a5",
            "A6": "app.tasks.task_a6",
            "A7": "app.tasks.task_a7",
            "A8": "app.tasks.task_a8",
            "A9": "app.tasks.task_a9",
            "A10": "app.tasks.task_a10",
            "B3": "app.tasks.task_b3",
            "B4": "app.tasks.task_b4",
            "B5": "app.tasks.task_b5",
            "B6": "app.tasks.task_b6",
            "B7": "app.tasks.task_b7",
            "B8": "app.tasks.task_b8",
            "B9": "app.tasks.task_b9",
            "B10": "app.tasks.task_b10",
        }

    def run_task(self, task_description: str) -> str:
        task_code = parse_task(task_description)
        if task_code not in self.task_mapping:
            raise ValueError("Invalid or unsupported task description.")
        module_name = self.task_mapping[task_code]
        module = importlib.import_module(module_name)
        result = module.run()
        write_log(f"Executed task {task_code} for description: {task_description}")
        return result