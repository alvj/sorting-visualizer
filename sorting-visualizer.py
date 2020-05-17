import tkinter
import random

HEIGHT = 600
BAR_WIDTH = 20
LIST_LENGTH = 40
OFFSET = 5

def main():
    random_list = create_random_list(LIST_LENGTH)
    canvas = create_canvas((BAR_WIDTH + OFFSET) * LIST_LENGTH, HEIGHT)
    
    draw_list(canvas, random_list)

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


def create_random_list(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(0, HEIGHT))
    return random_list


def draw_list(canvas, list):
    for i in range(len(list)):
        start_x = (i * BAR_WIDTH) + (OFFSET * i)
        start_y = HEIGHT - list[i]
        end_x = start_x + BAR_WIDTH
        end_y = HEIGHT
        canvas.create_rectangle(start_x, start_y, end_x, end_y, fill="#c3dff7")


if __name__ == '__main__':
    main()