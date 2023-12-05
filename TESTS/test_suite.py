import unittest
from TESTS.test_domain.test_event_class import test_event
from TESTS.test_domain.test_person_class import test_person
from TESTS.test_domain.test_DTO_classes import test_DTO_classes
from TESTS.test_controlers.test_event_controler import test_event_controler
from TESTS.test_controlers.test_person_controler import test_person_controler
def test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_event))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_person))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_DTO_classes))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_event_controler))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_person_controler))
    unittest.TextTestRunner(verbosity=2).run(test_suite)

