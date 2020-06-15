"""SORTING METHODS VISUALISER IN PYTHON"""
import random
import pygame
import pygame_gui


class Colors:
    """Colors used for visualising changes in arrays."""
    BACKGROUND = (0, 0, 0)
    DEFAULT_ARRAY_COLOR = (0, 255, 0)
    HIGHLIGHT_ARRAY_ELEMENT_RED = (255, 0, 0)
    HIGHLIGHT_ARRAY_ELEMENT_YELLOW = (255, 255, 0)
    HIGHLIGHT_ARRAY_ELEMENT_PINK = (255, 0, 255)


class TimeDelay:
    """Stores values of delays for each sorting function"""
    INSERTION_SORT_DELAY = 1
    SELECTION_SORT_DELAY = 0
    SHELL_SORT_DELAY = 20
    MERGE_SORT_DELAY = 10
    QUICK_SORT_DELAY = 20
    HEAP_SORT_DELAY = 5


ARRAY_SIZE = 100
MAIN_ARRAY = [0] * ARRAY_SIZE
COLOR_ARRAY = [Colors.DEFAULT_ARRAY_COLOR] * ARRAY_SIZE

START_POINT_X = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
MAX_VALUE = SCREEN_HEIGHT
START_POINT_Y = SCREEN_HEIGHT
LINE_WIDTH = (SCREEN_WIDTH - ARRAY_SIZE - 1) // (ARRAY_SIZE - 1)
SPACING = SCREEN_WIDTH / ARRAY_SIZE
NUMBER_OF_BUTTONS = 8
BUTTONS_NAMES = ['InsertionSort', 'SelectSort', 'ShellSort', 'MergeSort',
                 'QuickSort', 'HeapSort', 'Randomize', 'ESC']
BUTTONS_ARRAY = [0] * NUMBER_OF_BUTTONS

GUI_BOX_SIZE = (150, 50)
GUI_BOX_STARTING_POSITION_X = 0
GUI_BOX_STARTING_POSITION_Y = 0
GUI_BOX_GAP = 150
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def generate_random_array():
    """Generates randomized array."""
    for i in range(1, ARRAY_SIZE):
        COLOR_ARRAY[i] = Colors.DEFAULT_ARRAY_COLOR
        MAIN_ARRAY[i] = random.randrange(1, (SCREEN_HEIGHT - GUI_BOX_SIZE[1]))


def insertion_sort(array):
    """Sorts array using insertion sort method."""
    array_size = len(array)
    for i in range(1, array_size):
        COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            array[j + 1] = array[j]
            update_window(TimeDelay.INSERTION_SORT_DELAY)
            COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_PINK
            j -= 1
        array[j + 1] = key
        COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_PINK


def selection_sort(array):
    """Sorts array using selection sort method."""
    array_size = len(array)
    for i in range(array_size):
        min_index = i
        COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
        for j in range(i+1, array_size):
            COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            update_window(TimeDelay.SELECTION_SORT_DELAY)
            if array[min_index] > array[j]:
                min_index = j
                COLOR_ARRAY[min_index] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
            else:
                COLOR_ARRAY[j] = Colors.DEFAULT_ARRAY_COLOR
        array[i], array[min_index] = array[min_index], array[i]
        COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_PINK


def shell_sort(array):
    """Sorts array using shell sort method."""
    array_size = len(array)
    gap = [57, 23, 10, 4, 1]
    for index in range(0, len(gap)):
        for i in range(gap[index], array_size):
            temp_variable = array[i]
            j = i
            while j >= gap[index] and array[j - gap[index]] > temp_variable:
                array[j] = array[j - gap[index]]
                COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
                COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
                update_window(TimeDelay.SHELL_SORT_DELAY)
                COLOR_ARRAY[j] = Colors.DEFAULT_ARRAY_COLOR
                COLOR_ARRAY[i] = Colors.DEFAULT_ARRAY_COLOR
                j -= gap[index]
            array[j] = temp_variable


def merge_sort(array, left, right):
    """Sorts array using  merge sort method."""
    def merge(array, left, mid_left, mid_right, right):
        """Sorts given part of array."""
        i = left
        j = mid_right
        temp_variable = []
        pygame.event.pump()
        while i <= mid_left and j <= right:
            COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
            COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
            update_window(TimeDelay.MERGE_SORT_DELAY)
            COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            if array[i] < array[j]:
                temp_variable.append(array[i])
                i += 1
            else:
                temp_variable.append(array[j])
                j += 1
        while i <= mid_left:
            COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
            update_window(TimeDelay.MERGE_SORT_DELAY)
            COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            temp_variable.append(array[i])
            i += 1
        while j <= right:
            COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
            update_window(TimeDelay.MERGE_SORT_DELAY)
            COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            temp_variable.append(array[j])
            j += 1
        j = 0
        for i in range(left, right + 1):
            pygame.event.pump()
            array[i] = temp_variable[j]
            j += 1
            COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_PINK
            update_window(TimeDelay.MERGE_SORT_DELAY)
            if right - left == len(array) - 2:
                COLOR_ARRAY[i] = Colors.DEFAULT_ARRAY_COLOR
            else:
                COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
    mid = (left + right) // 2
    if left < right:
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid,
              mid + 1, right)


def quick_sort(array, min, max):
    """Sorts array using quick sort method."""
    def quick_sort_partition(arr, min, max):
        """Makes partition for quick sort."""
        i = (min - 1)
        pivot = arr[max]
        COLOR_ARRAY[max] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
        for j in range(min, max):
            COLOR_ARRAY[j] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            update_window(TimeDelay.QUICK_SORT_DELAY)
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                COLOR_ARRAY[i] = Colors.DEFAULT_ARRAY_COLOR
            else:
                COLOR_ARRAY[j] = Colors.DEFAULT_ARRAY_COLOR
                COLOR_ARRAY[i] = Colors.DEFAULT_ARRAY_COLOR
            COLOR_ARRAY[j] = Colors.DEFAULT_ARRAY_COLOR
        arr[i + 1], arr[max] = arr[max], arr[i + 1]
        COLOR_ARRAY[max] = Colors.DEFAULT_ARRAY_COLOR
        return i + 1
    if min < max:
        partition = quick_sort_partition(array, min, max)
        quick_sort(array, min, partition - 1)
        quick_sort(array, partition + 1, max)


def heap_sort(array):
    """Sorts array using heap sort method."""
    def heapify(array, array_size, i):
        """Makes heap for heap sort."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        update_window(TimeDelay.HEAP_SORT_DELAY)
        if left < array_size and array[i] < array[left]:
            COLOR_ARRAY[largest] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            largest = left
            update_window(TimeDelay.HEAP_SORT_DELAY)
            COLOR_ARRAY[largest] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
        if right < array_size and array[largest] < array[right]:
            COLOR_ARRAY[largest] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            largest = right
            update_window(TimeDelay.HEAP_SORT_DELAY)
            COLOR_ARRAY[largest] = Colors.HIGHLIGHT_ARRAY_ELEMENT_RED
        if largest != i:
            COLOR_ARRAY[i] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            array[i], array[largest] = array[largest], array[i]
            update_window(TimeDelay.HEAP_SORT_DELAY)
            COLOR_ARRAY[largest] = Colors.HIGHLIGHT_ARRAY_ELEMENT_YELLOW
            heapify(array, array_size, largest)
    array_size = len(array)
    for i in range((array_size // 2), - 1, -1):
        heapify(array, array_size, i)
    for i in range(array_size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        COLOR_ARRAY[i] = Colors.DEFAULT_ARRAY_COLOR
        update_window(TimeDelay.HEAP_SORT_DELAY)
        heapify(array, i, 0)


def draw_in_window():
    """Draws lines corresponding to array values."""
    for i in range(1, ARRAY_SIZE):
        pygame.draw.line(SCREEN, COLOR_ARRAY[i], (i * SPACING, SCREEN_HEIGHT),
                         (i * SPACING, SCREEN_HEIGHT - MAIN_ARRAY[i]),
                         LINE_WIDTH)


def update_window(time_delay):
    """Updates main window depending on given delay time."""
    SCREEN.fill(Colors.BACKGROUND)
    draw_in_window()
    pygame.display.flip()
    pygame.time.delay(time_delay)


def main():
    """Main function."""
    pygame.init()
    pygame.display.set_caption("SORTING METHODS VISUALISER")
    manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    for i in range(0, NUMBER_OF_BUTTONS):
        BUTTONS_ARRAY[i] = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (GUI_BOX_STARTING_POSITION_X + (i * GUI_BOX_GAP),
                 GUI_BOX_STARTING_POSITION_Y),
                GUI_BOX_SIZE), text=BUTTONS_NAMES[i], manager=manager)

    generate_random_array()

    window_opened = True

    while window_opened:
        time_delta = clock.tick(60) / 1000.0
        SCREEN.fill(Colors.BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_opened = False
            manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == BUTTONS_ARRAY[0]:
                        insertion_sort(MAIN_ARRAY)
                    if event.ui_element == BUTTONS_ARRAY[1]:
                        selection_sort(MAIN_ARRAY)
                    if event.ui_element == BUTTONS_ARRAY[2]:
                        shell_sort(MAIN_ARRAY)
                    if event.ui_element == BUTTONS_ARRAY[3]:
                        merge_sort(MAIN_ARRAY, 1, len(MAIN_ARRAY) - 1)
                    if event.ui_element == BUTTONS_ARRAY[4]:
                        quick_sort(MAIN_ARRAY, 0, ARRAY_SIZE - 1)
                    if event.ui_element == BUTTONS_ARRAY[5]:
                        heap_sort(MAIN_ARRAY)
                    if event.ui_element == BUTTONS_ARRAY[6]:
                        generate_random_array()
                    if event.ui_element == BUTTONS_ARRAY[7]:
                        window_opened = False
        manager.update(time_delta)
        manager.draw_ui(SCREEN)
        draw_in_window()
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
