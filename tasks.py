import os
import pathlib
from invoke import (
    task,
)

ROOT_PATH = pathlib.Path(__file__).resolve().parent
ROOT_PATH_STR = str(ROOT_PATH)


@task()
def clean(context):
    """
    Clean the project

    :param context: invoke context
    """
    with context.cd(ROOT_PATH_STR):
        context.run('git clean -fd')
        context.run('git clean -fdX')


@task()
def pytest(context, pty=True):
    """
    Run unit tests

    :param context: invoke context
    :param pty: True to run in a terminal, pass --no-pty to disable
    """
    with context.cd(ROOT_PATH_STR):
        # HACK: Poke the environment within invoke to make 'invoke pytest' work
        # as expected without having to rely on pip or a VE.   The
        # sys.path.append() and site.addsitedir() suggested workarounds do not
        # accomplish this.  Pythonista purists will understandably balk at
        # this, and I can sympathize, however this is a quick way for me to get
        # things moving forward.
        # TODO: Organize the project properly so this is no longer necessary.
        os.environ["PYTHONPATH"] = ROOT_PATH_STR
        context.run('pytest --log-cli-level=DEBUG', pty=pty)


@task()
def flake8(context):
    """
    Run the flake8 format checker

    :param context: invoke context
    """
    with context.cd(ROOT_PATH_STR):
        context.run('flake8')


@task()
def mypy(context):
    """
    Run mypy static code analysis

    :param context: invoke context
    """
    with context.cd(ROOT_PATH_STR):
        context.run('mypy --config-file setup.cfg ./src')


@task(pre=[pytest, flake8, mypy])
def all(context):
    """
    Run all tasks other than clean
    """
    pass
