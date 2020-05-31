import pygame,random,pygame_gui
pygame.init()
RGB_WHITE: tuple = (255, 255, 255)
RGB_BLACK: tuple = (0, 0, 0)
RGB_GREEN: tuple = (0, 255, 0)
RGB_RED: tuple = (255, 0, 0)
RGB_YELLOW: tuple =(255, 255, 0)
RGB_PINK: tuple = (255, 0, 255)

ARRAY_SIZE = 100 #max ARRAY_SIZE = SCREEN WIDTH/2
MAIN_ARRAY = [0] * ARRAY_SIZE
COLOR_ARRAY = [RGB_PINK] * ARRAY_SIZE

START_POINT_X = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
MAX_VALUE = SCREEN_HEIGHT
START_POINT_Y = SCREEN_HEIGHT
LINE_WIDTH = (SCREEN_WIDTH - ARRAY_SIZE - 1) // (ARRAY_SIZE - 1)
SPACING = SCREEN_WIDTH / ARRAY_SIZE
DELAY_TIME = 10

GUI_BOX_SIZE = (150,50)
GUI_BOX_STARTING_POSTION_X= 0
GUI_BOX_STARTING_POSTION_Y = 0
GUI_BOX_GAP = 150
pygame.display.set_caption("SORTING METHODS VISUALISER")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#GUI
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
insertion_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((GUI_BOX_STARTING_POSTION_X, GUI_BOX_STARTING_POSTION_Y), (GUI_BOX_SIZE)),text='Insertion(works)',manager=manager)
select_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((GUI_BOX_STARTING_POSTION_X + GUI_BOX_GAP, GUI_BOX_STARTING_POSTION_Y), (GUI_BOX_SIZE)),text='Select(works)',manager=manager)
shell_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((GUI_BOX_STARTING_POSTION_X + 2*GUI_BOX_GAP, GUI_BOX_STARTING_POSTION_Y), (GUI_BOX_SIZE)),text='Shell(works?)',manager=manager)
merge_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((GUI_BOX_STARTING_POSTION_X + 3*GUI_BOX_GAP, GUI_BOX_STARTING_POSTION_Y), (GUI_BOX_SIZE)),text='Merge(works)',manager=manager)
quick_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((GUI_BOX_STARTING_POSTION_X+4*GUI_BOX_GAP, GUI_BOX_STARTING_POSTION_Y), (GUI_BOX_SIZE)),text='Quick(works)',manager=manager)
heap_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((GUI_BOX_STARTING_POSTION_X+5*GUI_BOX_GAP, GUI_BOX_STARTING_POSTION_Y), (GUI_BOX_SIZE)),text='Heap(doesnt work)',manager=manager)
randomize_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((GUI_BOX_STARTING_POSTION_X+6*GUI_BOX_GAP, GUI_BOX_STARTING_POSTION_Y), (GUI_BOX_SIZE)),text='Randomize',manager=manager)
escape_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((GUI_BOX_STARTING_POSTION_X + 7 * GUI_BOX_GAP, GUI_BOX_STARTING_POSTION_Y), (GUI_BOX_SIZE)), text='ESCAPE', manager=manager)
def generate_list_array():
    MAIN_ARRAY = list(range(ARRAY_SIZE))
    random.shuffle(MAIN_ARRAY)
def generate_random_array():
    for i in range(1, ARRAY_SIZE):
        COLOR_ARRAY[i]= RGB_GREEN
        MAIN_ARRAY[i]= random.randrange(1, (SCREEN_HEIGHT - GUI_BOX_SIZE[1]))
generate_random_array()
def insertion_sort(arr):
    arr_size = len(arr)
    for i in range(1, arr_size):
        COLOR_ARRAY[i] = RGB_RED
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            COLOR_ARRAY[j] = RGB_YELLOW
            arr[j + 1] = arr[j]
            update_window()
            COLOR_ARRAY[j] = RGB_PINK
            j -= 1
        arr[j + 1] = key
        COLOR_ARRAY[i] = RGB_PINK
def selection_sort(arr):
    arr_size=len(arr)
    for i in range(arr_size):
        min_index = i
        COLOR_ARRAY[i] = RGB_RED
        for j in range(i+1,arr_size):
            COLOR_ARRAY[j] = RGB_YELLOW
            update_window()
            if arr[min_index] > arr[j]:
                min_index = j
                COLOR_ARRAY[min_index] = RGB_RED
            else:
                COLOR_ARRAY[j] = RGB_GREEN
        arr[i],arr[min_index] = arr[min_index],arr[i]
        COLOR_ARRAY[i] = RGB_PINK
def shell_sort(arr):
    arr_size = len(arr)
    gap = arr_size//2
    while gap > 0 :
        for i in range (gap,arr_size):
            temp_variable = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp_variable:
                arr[j] = arr[j-gap]
                COLOR_ARRAY[j] = RGB_RED
                COLOR_ARRAY[i] = RGB_RED
                update_window()
                COLOR_ARRAY[j] = RGB_GREEN
                COLOR_ARRAY[i] = RGB_GREEN
                j -= gap
            arr[j] = temp_variable
        gap //= 2
def mergesort(array, left, right):
    mid = (left + right) // 2
    if left<right:
        mergesort(array, left, mid)
        mergesort(array, mid + 1, right)
        merge(array, left, mid,
              mid + 1, right)
def merge(array, left, mid_l, mid_r, right):
    i = left
    j = mid_r
    temp_variable = []
    pygame.event.pump()
    while i <= mid_l and j <= right:
        COLOR_ARRAY[i] = RGB_RED
        COLOR_ARRAY[j] = RGB_RED
        update_window()
        COLOR_ARRAY[i] = RGB_YELLOW
        COLOR_ARRAY[j] = RGB_YELLOW
        if array[i] < array[j]:
                temp_variable.append(array[i])
                i += 1
        else:
                temp_variable.append(array[j])
                j += 1
    while i <= mid_l:
        COLOR_ARRAY[i] = RGB_RED
        update_window()
        COLOR_ARRAY[i] = RGB_YELLOW
        temp_variable.append(array[i])
        i += 1
    while j<= right:
        COLOR_ARRAY[j] = RGB_RED
        update_window()
        COLOR_ARRAY[j] = RGB_YELLOW
        temp_variable.append(array[j])
        j += 1
    j = 0
    for i in range(left, right + 1):
        pygame.event.pump()
        array[i] = temp_variable[j]
        j+= 1
        COLOR_ARRAY[i] = RGB_PINK
        update_window()
        if right-left == len(array)-2:
            COLOR_ARRAY[i] = RGB_GREEN
        else:
            COLOR_ARRAY[i] = RGB_YELLOW
def quick_sort(arr, min, max):
    def quick_sort_partition(arr, min, max):

        i = (min - 1)
        pivot = arr[max]
        COLOR_ARRAY[max] = RGB_RED
        for j in range(min, max):
            COLOR_ARRAY[j] = RGB_WHITE
            update_window()
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                COLOR_ARRAY[i] = RGB_GREEN
            else:
                COLOR_ARRAY[j] = RGB_GREEN
                COLOR_ARRAY[i] = RGB_GREEN
            COLOR_ARRAY[j] = RGB_GREEN
        arr[i + 1], arr[max] = arr[max], arr[i + 1]
        COLOR_ARRAY[max] = RGB_GREEN
        return (i + 1)
    if min < max:
        partition = quick_sort_partition(arr, min, max)
        quick_sort(arr, min, partition - 1)
        quick_sort(arr, partition + 1, max)
def heap_sort(arr): #nie działa poprawnie
    def heapify(arr, arr_size, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < arr_size and arr[i] < arr[left]:
            largest = left
        if right < arr_size and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, arr_size, largest)
    arr_size = len(arr)
    for i in range((arr_size // 2) - 1, -1, 1):
        heapify(arr, arr_size, i)
    for i in range(arr_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
def draw_in_window():
    for i in range(1, ARRAY_SIZE):
        pygame.draw.line(screen, COLOR_ARRAY[i], (i * SPACING, SCREEN_HEIGHT), (i * SPACING, SCREEN_HEIGHT - MAIN_ARRAY[i]), LINE_WIDTH)
def update_window():
    screen.fill(RGB_BLACK)
    draw_in_window()
    pygame.display.flip()
    pygame.time.delay(DELAY_TIME)
def main():
    RUN = True
    while RUN:
        time_delta = clock.tick(60) / 1000.0
        screen.fill(RGB_BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == insertion_button:
                        insertion_sort(MAIN_ARRAY)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == select_button:
                        selection_sort(MAIN_ARRAY)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == shell_button:
                        shell_sort(MAIN_ARRAY)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == merge_button:
                        mergesort(MAIN_ARRAY, 1, len(MAIN_ARRAY) - 1)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == quick_button:
                        quick_sort(MAIN_ARRAY, 0, ARRAY_SIZE - 1)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == heap_button:
                        heap_sort(MAIN_ARRAY)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == randomize_button:
                        generate_random_array()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == escape_button:
                        RUN = False
        manager.update(time_delta)
        manager.draw_ui(screen)
        draw_in_window()
        pygame.display.update()
    pygame.quit()
main()
