
from tkinter import *
import model


    

cell_size = 11
is_running = False


def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice
    
    root = Tk()
    root.title('Game of Life')

    grid_view = Canvas(root, width=model.width*cell_size,
                       height=model.height*cell_size,
                       borderwidth=0,
                       highlightthickness=0,
                       bg='white')

    start_button = Button (root, text ="Start", width=12)
    start_button.bind('<Button-1>', start_handler)
    clear_button = Button (root, text ="Clear", width=12)
    clear_button.bind('<Button-1>', clear_handler)
    grid_view.bind('<Button-1>', grid_handler)

    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu (root, choice, "Choose a Patterm",
                         "glider",
                         "glider gun",
                         "random",
                          command=option_handler)
    
    option.config(width=20)

    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)


def start_handler(event):
    global is_running, start_button

    if is_running:
        is_running = False
        start_button.configure(text='Start')
    else:
        is_running = True
        start_button.configure(text='Stop')
        update()

def clear_handler(event):
    global is_running, clear_button, grid_view
    is_running=False
    for i in range(0, model.height):
        for j in range(0, model.width):
            model.grid_model[i][j] = 0

    start_button.configure(text = 'Start')
    update()

def grid_handler(event):
    global grid_view, cell_size
    x = int(event.x/cell_size)
    y = int(event.y/cell_size)
    if (model.grid_model[x][y] == 1):
        model.grid_model[x][y] = 0
        draw_cell(x, y, 'white')
    else:
        model.grid_model[x][y] = 1
        draw_cell(x, y, 'red')

def option_handler(event):
    global is_running, start_button, choice

    is_running = False
    start_button.configure(text='Start')

    selection = choice.get()
    if selection == 'glider':
        model.load_pattern(model.glider_pattern, 10, 10)
    else:
        if selection == 'glider gun':
            model.load_pattern(model.glider_gun_pattern, 10, 10)
        else:
            if selection == 'random':
                model.randomize(model.grid_model, model.width, model.height)
    update()
    

        
def update():
    global grid_view
    grid_view.delete(ALL)
    model.next_gen()
    for i in range(0, model.height):
        for j in range(0, model.width):
            if model.grid_model[i][j] == 1:
                draw_cell(i, j, 'red')   
    if (is_running):
        root.after(10, update)

                
def draw_cell(row, col, color):
    global grid_view, cell_size
    if color == 'black':
        outline = 'grey'
    else:
        outline = 'black'
    grid_view.create_rectangle(row*cell_size,
                                col*cell_size,
                                row*cell_size+cell_size,
                                col*cell_size+cell_size,
                                fill=color, outline=outline)

if __name__ == '__main__':
    setup()
    update()
    mainloop()

