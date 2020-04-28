import unittest
from tests.Tabs.timeline_test import TimelineTest
from tests.Tabs.menu_test import MenuTabTests

# get all tests from Menu and Timeline tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(MenuTabTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TimelineTest)

# create a test suite combining both classes
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
