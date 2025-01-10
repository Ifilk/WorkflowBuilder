# WorkflowBuilder

## 简介

WorkflowBuilder 是一个用于构建和执行工作流的工具。它允许用户通过定义配置类、任务类和工作流来创建复杂的工作流，并且可以方便地管理和执行这些工作流。

## 安装

确保你已经安装了 Python 3.6+，然后可以通过 pip 安装 WorkflowBuilder：

```bash
pip install workflow_builder
```
## 使用示例

### 配置类

首先，定义一个配置类来存储工作流中需要使用的配置信息。这里我们定义了一个名为 `ExampleConfiguration` 的配置类，其中包含一个 `greeting` 字段。

```python
from workflow_builder import configclass, Configuration

# 参数指定别名
@configclass('example', 'example_config')
class ExampleConfiguration(Configuration):
    greeting: str
```
### 任务类

接下来，定义任务类。每个任务类必须继承自 `Task` 类，并实现 `preprocess` 和 `work` 方法。

#### ExampleTask1

`ExampleTask1` 是一个具体的任务类，它在执行前会从工作流的配置管理器中获取 `ExampleConfiguration`，并在 `work` 方法中返回一个字典，包含处理结果。

```python
class ExampleTask1(Task):
    def __init__(self, task_config: TaskConfig):
        task_config.name = ''
        # task_config.asynchronize = True
        self.config = None

    def preprocess(self, workflow: Workflow):
        self.config = workflow.config_manager[ExampleConfiguration]

    def work(self, workflow):
        return {
            'example_task1': self.config.greeting + ' World'
        }
```
#### ExampleTask

`ExampleTask` 是另一个任务类，它在 `work` 方法中接收来自 `ExampleTask1` 的输出并打印出来。

```python
class ExampleTask(Task):
    def __init__(self):
        ...

    def preprocess(self, workflow: Workflow):
        ...

    def work(self, example_task1):
        print(example_task1)
```
### 工作流

最后，将任务类添加到工作流中，并创建和执行管道。

```python
tasks = [
    ExampleTask1,
    ExampleTask
]

wf = Workflow(tasks)

# 手动指定configs
# workflow = Workflow(tasks, configs=configs)

# 默认从当前目录加载toml:
# workflow = Workflow(tasks, configs_path='.')

pipeline = wf.create_pipeline()
# execute pipeline
pipeline()
```
## 配置文件

默认情况下，工作流会从当前目录加载所有的 toml 配置文件。你可以通过 `configs_path` 参数指定其他路径。

### example.toml 示例

```toml
[example]
greeting = "Hello"
```
## 运行

确保配置文件存在后，运行以下命令即可执行工作流：

```bash
python your_script.py
```

[//]: # (## 贡献)

[//]: # ()
[//]: # (欢迎贡献代码！请先阅读 [贡献指南]&#40;CONTRIBUTING.md&#41;。)

[//]: # ()
[//]: # (## 许可证)

[//]: # ()
[//]: # (本项目采用 MIT 许可证，详情参见 [LICENSE]&#40;LICENSE&#41; 文件。)