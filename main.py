import pygame
import random
import pygame_gui


class Colors:
    """Paleta barw używana do kolorowania elementów tablic."""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    PINK = (255, 0, 255)


ARRAY_SIZE = 100
MAIN_ARRAY = [0] * ARRAY_SIZE
COLOR_ARRAY = [Colors.PINK] * ARRAY_SIZE

START_POINT_X = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
MAX_VALUE = SCREEN_HEIGHT
START_POINT_Y = SCREEN_HEIGHT
LINE_WIDTH = (SCREEN_WIDTH - ARRAY_SIZE - 1) // (ARRAY_SIZE - 1)
SPACING = SCREEN_WIDTH / ARRAY_SIZE
DELAY_TIME = 5

GUI_BOX_SIZE = (150, 50)
GUI_BOX_STARTING_POSITION_X = 0
GUI_BOX_STARTING_POSITION_Y = 0
GUI_BOX_GAP = 150
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def generate_random_array():
    """Generuje tablicę z pseudolosowymi wartościami."""
    for i in range(1, ARRAY_SIZE):
        COLOR_ARRAY[i] = Colors.GREEN
        MAIN_ARRAY[i] = random.randrange(1, (SCREEN_HEIGHT - GUI_BOX_SIZE[1]))


def insertion_sort(array):
    """Funkcja sortująca tablice za pomocą metody insertion sort."""
    array_size = len(array)
    for i in range(1, array_size):
        COLOR_ARRAY[i] = Colors.RED
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            COLOR_ARRAY[j] = Colors.YELLOW
            array[j + 1] = array[j]
            update_window()
            COLOR_ARRAY[j] = Colors.PINK
            j -= 1
        array[j + 1] = key
        COLOR_ARRAY[i] = Colors.PINK


def selection_sort(array):
    """Funkcja sortująca tablice za pomocą metody selection sort."""
    array_size = len(array)
    for i in range(array_size):
        min_index = i
        COLOR_ARRAY[i] = Colors.RED
        for j in range(i+1,array_size):
            COLOR_ARRAY[j] = Colors.YELLOW
            update_window()
            if array[min_index] > array[j]:
                min_index = j
                COLOR_ARRAY[min_index] = Colors.RED
            else:
                COLOR_ARRAY[j] = Colors.GREEN
        array[i], array[min_index] = array[min_index], array[i]
        COLOR_ARRAY[i] = Colors.PINK


def shell_sort(array):
    """Funkcja sortująca tablice za pomocą metody shell sort."""
    array_size = len(array)
    gap = [57, 23, 10, 4, 1]
    for index in range(0, len(gap)):
        for i in range(gap[index], array_size):
            temp_variable = array[i]
            j = i
            while j >= gap[index] and array[j - gap[index]] > temp_variable:
                array[j] = array[j - gap[index]]
                COLOR_ARRAY[j] = Colors.RED
                COLOR_ARRAY[i] = Colors.RED
                update_window()
                COLOR_ARRAY[j] = Colors.GREEN
                COLOR_ARRAY[i] = Colors.GREEN
                j -= gap[index]
            array[j] = temp_variable


def merge_sort(array, left, right):
    """Funkcja sortująca tablice za pomocą metody merge sort."""
    def merge(array, left, mid_left, mid_right, right):
        """Funkcja używana w metodzie merge sort."""
        i = left
        j = mid_right
        temp_variable = []
        pygame.event.pump()
        while i <= mid_left and j <= right:
            COLOR_ARRAY[i] = Colors.RED
            COLOR_ARRAY[j] = Colors.RED
            update_window()
            COLOR_ARRAY[i] = Colors.YELLOW
            COLOR_ARRAY[j] = Colors.YELLOW
            if array[i] < array[j]:
                temp_variable.append(array[i])
                i += 1
            else:
                temp_variable.append(array[j])
                j += 1
        while i <= mid_left:
            COLOR_ARRAY[i] = Colors.RED
            update_window()
            COLOR_ARRAY[i] = Colors.YELLOW
            temp_variable.append(array[i])
            i += 1
        while j <= right:
            COLOR_ARRAY[j] = Colors.RED
            update_window()
            COLOR_ARRAY[j] = Colors.YELLOW
            temp_variable.append(array[j])
            j += 1
        j = 0
        for i in range(left, right + 1):
            pygame.event.pump()
            array[i] = temp_variable[j]
            j += 1
            COLOR_ARRAY[i] = Colors.PINK
            update_window()
            if right - left == len(array) - 2:
                COLOR_ARRAY[i] = Colors.GREEN
            else:
                COLOR_ARRAY[i] = Colors.YELLOW
    mid = (left + right) // 2
    if left < right:
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid,
              mid + 1, right)


def quick_sort(array, min, max):
    """Funkcja sortująca tablice za pomocą metody merge sort."""
    def quick_sort_partition(arr, min, max):
        """Funkcja partition metody quick sort"""
        i = (min - 1)
        pivot = arr[max]
        COLOR_ARRAY[max] = Colors.RED
        for j in range(min, max):
            COLOR_ARRAY[j] = Colors.WHITE
            update_window()
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                COLOR_ARRAY[i] = Colors.GREEN
            else:
                COLOR_ARRAY[j] = Colors.GREEN
                COLOR_ARRAY[i] = Colors.GREEN
            COLOR_ARRAY[j] = Colors.GREEN
        arr[i + 1], arr[max] = arr[max], arr[i + 1]
        COLOR_ARRAY[max] = Colors.GREEN
        return i + 1
    if min < max:
        partition = quick_sort_partition(array, min, max)
        quick_sort(array, min, partition - 1)
        quick_sort(array, partition + 1, max)


def heap_sort(array):
    """Funkcja sortująca tablice za pomocą metody heap sort."""
    def heapify(array, array_size, i):
        """Funkcja tworząca heap dla metody heap sort."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        update_window()
        if left < array_size and array[i] < array[left]:
            COLOR_ARRAY[largest] = Colors.YELLOW
            largest = left
            update_window()
            COLOR_ARRAY[largest] = Colors.RED
        if right < array_size and array[largest] < array[right]:
            COLOR_ARRAY[largest] = Colors.YELLOW
            largest = right
            update_window()
            COLOR_ARRAY[largest] = Colors.RED
        if largest != i:
            COLOR_ARRAY[i] = Colors.YELLOW
            array[i], array[largest] = array[largest], array[i]
            update_window()
            COLOR_ARRAY[largest] = Colors.YELLOW
            heapify(array, array_size, largest)
    array_size = len(array)
    for i in range((array_size // 2), - 1, -1):
        heapify(array, array_size, i)
    for i in range(array_size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        COLOR_ARRAY[i] = Colors.GREEN
        update_window()
        heapify(array, i, 0)


def draw_in_window():
    """Funkcja rysująca lini w głównym oknie programu"""
    for i in range(1, ARRAY_SIZE):
        pygame.draw.line(SCREEN, COLOR_ARRAY[i], (i * SPACING, SCREEN_HEIGHT),
                         (i * SPACING, SCREEN_HEIGHT - MAIN_ARRAY[i]), LINE_WIDTH)


def update_window():
    """Funkcja aktualizująca główne okno programu"""
    SCREEN.fill(Colors.BLACK)
    draw_in_window()
    pygame.display.flip()
    pygame.time.delay(DELAY_TIME)


def main():
    """Główna funkcja programu"""
    pygame.init()
    pygame.display.set_caption("SORTING METHODS VISUALISER")
    # GUI
    manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    insertion_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((GUI_BOX_STARTING_POSITION_X, GUI_BOX_STARTING_POSITION_Y), (GUI_BOX_SIZE)),
        text='InsertionSort', manager=manager)
    select_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((GUI_BOX_STARTING_POSITION_X + GUI_BOX_GAP, GUI_BOX_STARTING_POSITION_Y),
                                  GUI_BOX_SIZE), text='SelectSort', manager=manager)
    shell_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((GUI_BOX_STARTING_POSITION_X + 2 * GUI_BOX_GAP, GUI_BOX_STARTING_POSITION_Y),
                                  GUI_BOX_SIZE), text='ShellSort', manager=manager)
    merge_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((GUI_BOX_STARTING_POSITION_X + 3 * GUI_BOX_GAP, GUI_BOX_STARTING_POSITION_Y),
                                  GUI_BOX_SIZE), text='MergeSort', manager=manager)
    quick_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((GUI_BOX_STARTING_POSITION_X + 4 * GUI_BOX_GAP, GUI_BOX_STARTING_POSITION_Y),
                                  GUI_BOX_SIZE), text='QuickSort', manager=manager)
    heap_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((GUI_BOX_STARTING_POSITION_X + 5 * GUI_BOX_GAP, GUI_BOX_STARTING_POSITION_Y),
                                  GUI_BOX_SIZE), text='HeapSort', manager=manager)
    randomize_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((GUI_BOX_STARTING_POSITION_X + 6 * GUI_BOX_GAP, GUI_BOX_STARTING_POSITION_Y),
                                  GUI_BOX_SIZE), text='Randomize', manager=manager)
    escape_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((GUI_BOX_STARTING_POSITION_X + 7 * GUI_BOX_GAP, GUI_BOX_STARTING_POSITION_Y),
                                  GUI_BOX_SIZE), text='ESCAPE', manager=manager)

    generate_random_array()

    window_opened = True

    while window_opened:
        time_delta = clock.tick(60) / 1000.0
        SCREEN.fill(Colors.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_opened = False
            manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == insertion_button:
                        insertion_sort(MAIN_ARRAY)
                    if event.ui_element == select_button:
                        selection_sort(MAIN_ARRAY)
                    if event.ui_element == shell_button:
                        shell_sort(MAIN_ARRAY)
                    if event.ui_element == merge_button:
                        merge_sort(MAIN_ARRAY, 1, len(MAIN_ARRAY) - 1)
                    if event.ui_element == quick_button:
                        quick_sort(MAIN_ARRAY, 0, ARRAY_SIZE - 1)
                    if event.ui_element == heap_button:
                        heap_sort(MAIN_ARRAY)
                    if event.ui_element == randomize_button:
                        generate_random_array()
                    if event.ui_element == escape_button:
                        window_opened = False
        manager.update(time_delta)
        manager.draw_ui(SCREEN)
        draw_in_window()
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
