import subprocess

from collections import namedtuple

ExecutionStatus = namedtuple('ExecutionStatus', ('output', 'error',
                                                 'returncode'))


class CommandExecutor:

    def __init__(self):
        pass

    @staticmethod
    def execute(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                stdin=subprocess.PIPE):
        process = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                   stdin=stdin)
        output, error = process.communicate()
        return ExecutionStatus(output, error, process.returncode)
