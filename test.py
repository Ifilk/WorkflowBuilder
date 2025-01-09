from workflow_builder import configclass, Configuration, Task, Workflow, TaskConfig


@configclass('example', 'example_config')
class ExampleConfiguration(Configuration):
    greeting: str

class ExampleTask1(Task):
    def __init__(self, task_config: TaskConfig):
        task_config.name = ''
        # task_config.asynchronize = True
        self.config = None

    # process before pipeline creating
    def preprocess(self, workflow: Workflow):
        self.config = workflow.config_manager[ExampleConfiguration]

    def work(self, workflow):
        return {
            'example_task1': self.config.greeting + ' World'
        }

class ExampleTask(Task):
    def __init__(self):
        ...

    def preprocess(self, workflow: Workflow):
        ...

    def work(self, example_task1):
        print(example_task1)

tasks = [
    ExampleTask1,
    ExampleTask
]

wf = Workflow(tasks)
pipeline = wf.create_pipeline()
# execute pipeline
pipeline()