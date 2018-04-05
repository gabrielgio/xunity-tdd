class TestCase(object):

    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):

    def __init__(self, name):
        TestCase.__init__(self, name)

    def test_method(self):
        self.wasRun = 1

    def set_up(self):
        self.wasRun = None
        self.wasSetup = 1


class TestCaseTest(TestCase):

    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def test_set_up(self):
        self.test.run()
        assert self.test.wasSetup


TestCaseTest("test_set_up").run()
TestCaseTest("test_running").run()
