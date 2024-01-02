from UTILS.sort import shell_sort, bubble_sort
import unittest

class test_shell_sort(unittest.TestCase):
    def setUp(self) -> None:
        self.__list = [12,4,21,6,7,74,2,2332,4,435]
        self.__string_list = ["ana", "are", "mere", "si", "pere", "si", "gutui"]
        self.__list_of_tuples = [(4,5), (2,3), (0,10), (4,1), (1,2), (0,0)]
        self.__string = "hello"
        self.__dict = {"one":1, "four":4, "two":2, "three":3, "five":5}

    def tearDown(self) -> None:
        self.__list = None
        self.__string_list = None
        self.__list_of_tuples = None
        self.__string = None
        self.__dict = None

    def test_shell_sort(self):
        self.assertEqual(shell_sort(self.__list), [2, 4, 4, 6, 7, 12, 21, 74, 435, 2332])
        self.assertEqual(shell_sort(self.__string_list,key = len, reverse = True), ['gutui', 'pere', 'mere', 'are', 'ana', 'si', 'si'])
        self.assertEqual(shell_sort(self.__list_of_tuples, key = lambda x:x[1]), [(0, 0), (4, 1), (1, 2), (2, 3), (4, 5), (0, 10)])
        self.assertEqual(shell_sort(self.__string), ['e', 'h', 'l', 'l', 'o'])
        self.assertEqual(shell_sort(self.__dict.items(), key = lambda x:x[0]), [('five', 5), ('four', 4), ('one', 1), ('three', 3), ('two', 2)])
        def custom_compare(x, y):
            if x[-1] < y[-1]:
                return False
            return True
        self.assertEqual(shell_sort(self.__dict.items(), key = lambda x:x[0], cmp = custom_compare), [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)])

class test_bubble_sort(unittest.TestCase):
    def setUp(self) -> None:
        self.__list = [12,4,21,6,7,74,2,2332,4,435]
        self.__string_list = ["ana", "are", "mere", "si", "pere", "si", "gutui"]
        self.__list_of_tuples = [(4,5), (2,3), (0,10), (4,1), (1,2), (0,0)]
        self.__string = "hello"
        self.__dict = {"one":1, "four":4, "two":2, "three":3, "five":5}

    def tearDown(self) -> None:
        self.__list = None
        self.__string_list = None
        self.__list_of_tuples = None
        self.__string = None
        self.__dict = None

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.__list), [2, 4, 4, 6, 7, 12, 21, 74, 435, 2332])
        self.assertEqual(bubble_sort(self.__string_list,key = len, reverse = True), ['gutui', 'mere', 'pere', 'ana', 'are', 'si', 'si'])
        self.assertEqual(bubble_sort(self.__list_of_tuples, key = lambda x:x[1]), [(0, 0), (4, 1), (1, 2), (2, 3), (4, 5), (0, 10)])
        self.assertEqual(bubble_sort(self.__string), ['e', 'h', 'l', 'l', 'o'])
        self.assertEqual(bubble_sort(self.__dict.items(), key = lambda x:x[0]), [('five', 5), ('four', 4), ('one', 1), ('three', 3), ('two', 2)])
        def custom_compare(x, y):
            if x[-1] < y[-1]:
                return False
            return True
        self.assertEqual(bubble_sort(self.__dict.items(), key = lambda x:x[0], cmp = custom_compare), [('five', 5), ('three', 3), ("one", 1), ('two', 2), ('four', 4)])