import pygame,random
pygame.init()
RGB_WHITE: tuple = (255, 255, 255)
RGB_BLACK: tuple = (0, 0, 0)
RGB_GREEN: tuple = (0, 255, 0)
RGB_RED: tuple = (255, 0, 0)
RGB_YELLOW: tuple =(255, 255, 0)
RGB_PINK: tuple = (255, 0, 255)

ARRAY_SIZE = 50
MAIN_ARRAY = [0] * ARRAY_SIZE
COLOR_ARRAY = [RGB_PINK] * ARRAY_SIZE

START_POINT_X = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
MAX_VALUE = SCREEN_HEIGHT
START_POINT_Y = SCREEN_HEIGHT
LINE_WIDTH = (SCREEN_WIDTH - ARRAY_SIZE - 1) // (ARRAY_SIZE - 1)
SPACING = SCREEN_WIDTH / ARRAY_SIZE
DELAY_TIME = 5
RUN = True

pygame.display.set_caption("SORTING METHODS VISUALISER")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def generate_list_array():
    MAIN_ARRAY = list(range(ARRAY_SIZE))
    random.shuffle(MAIN_ARRAY)
def generate_random_array():
    for i in range(1, ARRAY_SIZE):
        COLOR_ARRAY[i]= RGB_GREEN
        MAIN_ARRAY[i]= random.randrange(1, SCREEN_HEIGHT)
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
        for j in range(i+1,arr_size):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        update_window()
def shell_sort(arr): #dziala za szybko ->
    arr_size = len(arr)
    gap = arr_size//2
    while gap > 0 :
        for i in range (gap,arr_size):
            temp_variable = arr[i]
            j=i
            while j >= gap and arr[j-gap] > temp_variable:
                arr[j] = arr[j-gap]
                update_window()
                j -= gap
            arr[j] = temp_variable
        gap //= 2
    #array_window_update(arr)
def merge_sort(arr):
    arr_size = len(arr)
    if arr_size > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        #pygame.event.pump()
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                update_window()
                i += 1
            else:
                arr[k] = R[j]
                update_window()
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            update_window()
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            update_window()
            j += 1
            k += 1
def quick_sort(arr, min, max):
    def quick_sort_partition(arr, min, max):

        i = (min - 1)
        pivot = arr[max]
        for j in range(min, max):
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[max] = arr[max], arr[i + 1]
        update_window()
        return (i + 1)
    if min < max:
        partition = quick_sort_partition(arr, min, max)
        #array_window_update(arr)
        quick_sort(arr, min, partition - 1)
        quick_sort(arr, partition + 1, max)
def heap_sort(arr):
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
    for i in range(arr_size, -1, 1):
        heapify(arr, arr_size, i)
    for i in range(arr_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        update_window()
def draw_in_window():
    for i in range(1, ARRAY_SIZE):
        pygame.draw.line(screen, COLOR_ARRAY[i], (i * SPACING, SCREEN_HEIGHT), (i * SPACING, SCREEN_HEIGHT - MAIN_ARRAY[i]), LINE_WIDTH)
def update_window():
    screen.fill(RGB_BLACK)
    draw_in_window()
    pygame.display.flip()
    pygame.time.delay(DELAY_TIME) #zmienic zmienna z dupy
#main
while RUN:
    screen.fill(RGB_BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                insertion_sort(MAIN_ARRAY)#DZIALA
                #selection_sort(MAIN_ARRAY)
                #shell_sort(MAIN_ARRAY)
                #merge_sort(MAIN_ARRAY)
                #quick_sort(MAIN_ARRAY, 0, ARRAY_SIZE - 1)
                #heap_sort(MAIN_ARRAY) #rysowanie nie dziala poprawnie
    draw_in_window()
    pygame.display.update()
pygame.quit()





