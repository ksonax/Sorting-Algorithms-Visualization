import main
import unittest


class TestColors(unittest.TestCase):
    def setUp(self):
        self.Color = main.Colors()

    def test_BLACK(self):
        self.assertEqual(self.Color.BLACK, (0, 0, 0))

    def test_WHITE(self):
        self.assertEqual(self.Color.WHITE, (255, 255, 255))

    def test_RED(self):
        self.assertEqual(self.Color.RED, (255, 0, 0))

    def test_YELLOW(self):
        self.assertEqual(self.Color.YELLOW, (255, 255, 0))

    def test_PINK(self):
        self.assertEqual(self.Color.PINK, (255, 0, 255))

    def test_GREEN(self):
        self.assertEqual(self.Color.GREEN, (0, 255, 0))


class TestFunctions(unittest.TestCase):
    def test_insertion_sort(self):
        test_array = [0, 3, 22, 1, 4, 6, 9, 8]
        test_correctly_sorted_array = [0, 1, 3, 4, 6, 8, 9, 22]
        main.insertion_sort(test_array)
        for i in range(0, len(test_array)):
            self.assertEqual(test_array[i], test_correctly_sorted_array[i])

    def test_selection_sort(self):
        test_array = [0, 3, 22, 1, 4, 6, 9, 8]
        test_correctly_sorted_array = [0, 1, 3, 4, 6, 8, 9, 22]
        main.selection_sort(test_array)
        for i in range(0, len(test_array)):
            self.assertEqual(test_array[i], test_correctly_sorted_array[i])

    def test_shell_sort(self):
        test_array = [0, 3, 22, 1, 4, 6, 9, 8]
        test_correctly_sorted_array = [0, 1, 3, 4, 6, 8, 9, 22]
        main.shell_sort(test_array)
        for i in range(0, len(test_array)):
            self.assertEqual(test_array[i], test_correctly_sorted_array[i])

    def test_merge_sort(self):
        test_array = [0, 3, 22, 1, 4, 6, 9, 8]
        test_correctly_sorted_array = [0, 1, 3, 4, 6, 8, 9, 22]
        main.merge_sort(test_array, 1, len(test_array)-1)
        for i in range(0, len(test_array)):
            self.assertEqual(test_array[i], test_correctly_sorted_array[i])

    def test_quick_sort(self):
        test_array = [0, 3, 22, 1, 4, 6, 9, 8]
        test_correctly_sorted_array = [0, 1, 3, 4, 6, 8, 9, 22]
        main.quick_sort(test_array, 0, len(test_array) - 1)
        for i in range(0, len(test_array)):
            self.assertEqual(test_array[i], test_correctly_sorted_array[i])

    def test_heap_sort(self):
        test_array = [0, 3, 22, 1, 4, 6, 9, 8]
        test_correctly_sorted_array = [0, 1, 3, 4, 6, 8, 9, 22]
        main.heap_sort(test_array)
        for i in range(0, len(test_array)):
            self.assertEqual(test_array[i], test_correctly_sorted_array[i])


if __name__ == '__main__':
    unittest.main()