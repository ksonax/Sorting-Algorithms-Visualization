import main
import unittest


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.test_array = [0, 3, 22, 1, 4, 6, 9, 8]
        self.correctly_sorted_array = sorted(self.test_array)

    def test_insertion_sort(self):
        main.insertion_sort(self.test_array)
        self.assertEqual(self.test_array, self.correctly_sorted_array)

    def test_selection_sort(self):
        main.selection_sort(self.test_array)
        self.assertEqual(self.test_array, self.correctly_sorted_array)

    def test_shell_sort(self):
        main.shell_sort(self.test_array)
        self.assertEqual(self.test_array, self.correctly_sorted_array)

    def test_merge_sort(self):
        main.merge_sort(self.test_array, 1, len(self.test_array)-1)
        self.assertEqual(self.test_array, self.correctly_sorted_array)

    def test_quick_sort(self):
        main.quick_sort(self.test_array, 0, len(self.test_array) - 1)
        self.assertEqual(self.test_array, self.correctly_sorted_array)

    def test_heap_sort(self):
        main.heap_sort(self.test_array)
        self.assertEqual(self.test_array, self.correctly_sorted_array)


if __name__ == '__main__':
    unittest.main()
