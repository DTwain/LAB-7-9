import unittest
from TESTS.test_domain.test_event_class import test_event_class
from TESTS.test_domain.test_person_class import test_person_class
from TESTS.test_domain.test_DTO_classes import test_DTO_classes
from TESTS.test_domain.test_person_event_class import test_person_event_class
from TESTS.test_controlers.test_event_controler import test_event_controler
from TESTS.test_controlers.test_person_controler import test_person_controler
from TESTS.test_controlers.test_report_controler import test_report_controler
from TESTS.test_repo.test_repo_events import test_repo_events
from TESTS.test_repo.test_repo_people import test_repo_people
from TESTS.test_repo.teste_repo_file.test_repo_file_evenimente import test_repo_file_event
from TESTS.test_repo.teste_repo_file.test_repo_file_persoane import test_repo_file_people
from TESTS.test_domain.tests_validation.test_validare_event import test_validare_event
from TESTS.test_domain.tests_validation.test_validare_persoana import test_validare_persoana

def test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_event_class))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_person_class))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_person_event_class))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_DTO_classes))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_event_controler))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_person_controler))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_report_controler))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_repo_events))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_repo_people))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_repo_file_event))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_repo_file_people))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_validare_event))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_validare_persoana))
    unittest.TextTestRunner(verbosity = 1).run(test_suite)

