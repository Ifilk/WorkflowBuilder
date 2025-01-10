from setuptools import setup, find_packages

setup(
    name='workflow_builder',
    version='0.1',
    author='Ifilk',
    author_email='suanxc@yeah.net',
    description='WorkflowBuilder is a tool for building and executing workflows. '
                'It allows users to create complex workflows by defining configuration classes, '
                'task classes, and workflows, and can easily manage and execute these workflows. ',
    long_description=open('README.txt').read(),
    packages=find_packages(),
    install_requires=[
        'toml',
    ]
)
