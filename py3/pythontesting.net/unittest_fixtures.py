import unittest
import inspect


def logPoint(context):
    'utility function used for module functions and class methods'
    callingFunction = inspect.stack()[1][3]
    print ('in %s - %s()' % (context, callingFunction))


def setUpModule():
    'called once, before anything else in this module'
    logPoint('module %s' % __name__)


def tearDownModule():
    'called once, after everything else in this module'
    logPoint('module %s' % __name__)


class TestFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        'called once, before any tests'
        logPoint('class %s' % cls.__name__)

    @classmethod
    def tearDownClass(cls):
        'called once, after all tests, if setUpClass successful'
        logPoint('class %s' % cls.__name__)

    def setUp(self):
        'called multiple times, before every test method'
        self.logPoint()

    def tearDown(self):
        'called multiple times, after every test method'
        self.logPoint()

    def test_m1(self):
        'a test'
        self.logPoint()

    def test_m2(self):
        'another test'
        self.logPoint()

    def logPoint(self):
        'utility method to trace control flow'
        callingFunction = inspect.stack()[1][3]
        currentTest = self.id().split('.')[-1]
        print('in %s - %s()' % (currentTest, callingFunction))

class TestAddCleanup(TestFixtures):
    def setUp(self):
        TestFixtures.setUp(self)
        # --- add a cleanup method fixture for all tests
        def cleanup_a():
            self.logPoint()
        self.addCleanup(cleanup_a)

    def test_m1(self):
        TestFixtures.test_m1(self)
        # --- add a cleanup method fixture for just this test
        def cleanup_b():
            self.logPoint()
        self.addCleanup(cleanup_b)
    def test_m2(self):
        TestFixtures.test_m2(self)

class TestSkip(TestFixtures):
    def setUp(self):
        TestFixtures.setUp(self)
        currentTest = self.id().split('.')[-1]
        if currentTest == 'test_2':
            self.skipTest('reason for skipping')
            # the 'reason' will displayed if '-v/--verbose' flag used

class DemoException(Exception):
    'exception to demostrate fixture/test failures'
    pass

class TestExceptionInSetUp(TestFixtures):
    def setUp(self):
        TestFixtures.setUp(self)
        raise DemoException

class TestExceptionInTearDownClass(TestFixtures):
    @classmethod
    def tearDownClass(cls):
        TestFixtures.tearDownClass()
        raise DemoException

if __name__ == '__main__':
  unittest.main()
  # unittest.main(argv=['ignored', '-v'], exit=False)

# Run:
# $ python -m unittest -q unittest_fixtures.TestFixtures
# $ python -m unittest -q unittest_fixtures.TestAddCleanup
# $ python -m unittest -q unittest_fixtures.TestSkip
# $ python -m unittest -q unittest_fixtures.TestExceptionInSetUp
# $ python -m unittest -q unittest_fixtures.TestExceptionInTearDownClass
