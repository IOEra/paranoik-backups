import unittest
import mock

from paranoik.utils.command_executor import CommandExecutor

class DummyProcess:
    def __init__(self):
        self._stdout = "stdout"
        self._stderr = "stderr"
        self.returncode = 0

    def communicate(self):
        return self._stdout, self._stderr


class CommandExecutorTests(unittest.TestCase):

    @mock.patch("subprocess.Popen")
    def test_command_execution(self, Popen):
        Popen.return_value = DummyProcess()
        command = CommandExecutor()
        status = command.execute(["ls", "/"])
        self.assertEquals(status.output, "stdout")
        self.assertEquals(status.error, "stderr")
        self.assertEquals(status.returncode, 0)

if __name__ == "__main__":
    unittest.main()