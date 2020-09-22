import invoke
import pathlib

ROOT_PATH = pathlib.Path(__file__).resolve().parent
ROOT_PATH_STR = str(ROOT_PATH)


@invoke.task()
def clean(context):
    """
    Clean the project

    :param context: invoke context
    """
    with context.cd(ROOT_PATH_STR):
        context.run('git clean -fd')
        context.run('git clean -fdX')


@invoke.task()
def pytest(context, pty=True):
    """
    Run unit tests

    :param context: invoke context
    :param pty: True to run in a terminal, pass --no-pty to disable
    """
    with context.cd(ROOT_PATH_STR):
        context.run('pytest', pty=pty)


@invoke.task()
def flake8(context):
    """
    Run the flake8 format checker

    :param context: invoke context
    """
    with context.cd(ROOT_PATH_STR):
        context.run('flake8')


@invoke.task()
def mypy(context):
    """
    Run mypy static code analysis

    :param context: invoke context
    """
    with context.cd(ROOT_PATH_STR):
        context.run('mypy --config-file setup.cfg ./src')


@invoke.task(pre=[pytest, flake8, mypy])
def all(context):
    """
    Run all tasks other than clean
    """
    pass
