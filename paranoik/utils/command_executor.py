"""
Contains Command Executor.
"""

import subprocess

from collections import namedtuple

ExecutionStatus = namedtuple('ExecutionStatus', ('output', 'error',
                                                 'returncode'))


class CommandExecutor:
    """
    Wrapper around Popen to execute commands.
    """

    def __init__(self, command, stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE, stdin=subprocess.PIPE):
        """
        :param command: Command that needs to be executed.
        :param stdout: Output stream.
        :param stderr: Error stream.
        :param stdin: Input stream.
        :return:
        """
        self._command = command
        self._stdout = stdout
        self._stderr = stderr
        self._stdin = stdin
        self._process = None

    def start_process(self):
        """
        Starts a process, based on provided command.
        :return:
        """
        self._process = subprocess.Popen(self._command, stdout=self._stdout,
                                         stderr=self._stderr,
                                         stdin=self._stdin)

    def execute(self):
        """
        Starts a process and returns execution status.
        :return: ExecutionStatus
        """
        self.start_process()
        output, error = self._process.communicate()
        return ExecutionStatus(output, error, self._process.returncode)
