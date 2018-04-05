class TestResult(object):

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def test_started(self):
        self.runCount = self.runCount + 1

    def test_failed(self):
        self.errorCount = self.errorCount + 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)


class TestCase(object):

    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()
        return result


class WasRun(TestCase):

    def __init__(self, name):
        TestCase.__init__(self, name)

    def test_method(self):
        self.log = self.log + "testMethod "

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log = self.log + "tearDown "

    def set_up(self):
        self.log = "setUp "


class TestCaseTest(TestCase):

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert "setUp testMethod tearDown " == test.log

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert "1 run, 1 failed", result.summary()

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert "1 run, 1 failed" == result.summary()


TestCaseTest("test_result").run()
TestCaseTest("test_template_method").run()
TestCaseTest("test_failed_result").run()
TestCaseTest("test_failed_result_formatting").run()
