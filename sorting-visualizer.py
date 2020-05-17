import tkinter
import random
import time

HEIGHT = 600
BAR_WIDTH = 20
LIST_LENGTH = 40
OFFSET = 5

# COLORS
BLUE = "#c3dff7"
RED = "#ff9c9c"
GREEN = "#92fc94"

def main():
    canvas = create_canvas((BAR_WIDTH + OFFSET) * LIST_LENGTH, HEIGHT)
    rect_list = draw_list(canvas)
    selection_sort(canvas, rect_list)
    canvas.mainloop()


def create_canvas(width, height):
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title("Sorting Visualizer")
    canvas = tkinter.Canvas(top, width=width, height=height)
    canvas.pack()
    # Add this so the first bar is not clipped
    canvas.xview_scroll(8, 'units')
    return canvas


def draw_list(canvas):
    rect_list = []
    for i in range(LIST_LENGTH):
        start_x = (i * BAR_WIDTH) + (OFFSET * i)
        start_y = HEIGHT - random.randint(1, HEIGHT)
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
        
def selection_sort(canvas, list):
    smallest = HEIGHT - canvas.bbox(list[0])[1]
    smallest_index = 0
    for i in range(len(list)):
        current = HEIGHT - canvas.bbox(list[i])[1]
        canvas.itemconfig(list[i], fill=RED)
        canvas.update()
        if smallest > current:
            canvas.itemconfig(list[i], fill=GREEN)
            canvas.itemconfig(list[smallest_index], fill=BLUE)
            smallest = current
            smallest_index = i
        else:
            if smallest_index == i:
                canvas.itemconfig(list[i], fill=GREEN)
            else:
                canvas.itemconfig(list[i], fill=BLUE)
        time.sleep(0.3)



if __name__ == '__main__':
    main()