class TestCase(object):

    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()


class WasRun(TestCase):

    def __init__(self, name):
        TestCase.__init__(self, name)

    def test_method(self):
        self.log = self.log + "testMethod "

    def tear_down(self):
        self.log = self.log + "tearDown "

    def set_up(self):
        self.log = "setUp "


class TestCaseTest(TestCase):

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert "setUp testMethod tearDown " == test.log


TestCaseTest("test_template_method").run()
