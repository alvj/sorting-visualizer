import tkinter
import random
import time

HEIGHT = 600
BAR_WIDTH = 20
LIST_LENGTH = 40
OFFSET = 5
SPEED = 0.05

# COLORS
BLUE = "#c3dff7"
RED = "#ff9c9c"
GREEN = "#92fc94"

def main():
    canvas = create_canvas((BAR_WIDTH + OFFSET) * LIST_LENGTH, HEIGHT)
    random_list = create_random_list(LIST_LENGTH)
    random_rect_list = draw_list(canvas, random_list)
    sorted_list = []
    sorted_rect_list = []
    selection_sort(canvas, random_list, random_rect_list, sorted_list, sorted_rect_list)
    canvas.mainloop()


def create_canvas(width, height):
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title("Sorting Visualizer")
    top.resizable(False, False)
    canvas = tkinter.Canvas(top, width=width, height=height)
    canvas.pack()
    # Add this so the first bar is not clipped
    canvas.xview_scroll(8, 'units')
    return canvas

def create_random_list(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(1, HEIGHT))
    return random_list

def draw_list(canvas, list):
    rect_list = []
    for i in range(len(list)):
        start_x = (i * BAR_WIDTH) + (OFFSET * i)
        start_y = HEIGHT - list[i]
        end_x = start_x + BAR_WIDTH
        end_y = HEIGHT

        rect = canvas.create_rectangle(
            start_x,
            start_y,
            end_x,
            end_y,
            fill=BLUE,
            width=0)
        rect_list.append(rect)
    return rect_list


def draw_updated_list(canvas, list, rect_list, previous_list_length=0):
    for i in range(len(list)):
        start_x = (i * BAR_WIDTH) + (OFFSET * i) + ((previous_list_length * BAR_WIDTH) + (OFFSET * previous_list_length))
        start_y = HEIGHT - list[i]
        end_x = start_x + BAR_WIDTH
        end_y = HEIGHT

        canvas.coords(
            rect_list[i],
            start_x,
            start_y,
            end_x,
            end_y
        )
        

def selection_sort(canvas, random_list, random_rect_list, sorted_list, sorted_rect_list):
    if not random_list:
        return
    
    smallest = random_list[0]
    smallest_index = 0
    canvas.itemconfig(random_rect_list[smallest_index], fill=GREEN)

    for i in range(1, len(random_list)):
        current = random_list[i]
        canvas.itemconfig(random_rect_list[i], fill=RED)
        canvas.update()

        if smallest > current:
            canvas.itemconfig(random_rect_list[i], fill=GREEN)
            canvas.itemconfig(random_rect_list[smallest_index], fill=BLUE)
            smallest = current
            smallest_index = i
        else:
            canvas.itemconfig(random_rect_list[i], fill=BLUE)
        time.sleep(SPEED)

    sorted_list.append(random_list.pop(smallest_index))
    sorted_rect_list.append(random_rect_list.pop(smallest_index))

    draw_updated_list(canvas, sorted_list, sorted_rect_list)
    draw_updated_list(canvas, random_list, random_rect_list, len(sorted_list))
    canvas.update()
    selection_sort(canvas, random_list, random_rect_list, sorted_list, sorted_rect_list)
    



if __name__ == '__main__':
    main()