import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image,ImageTk
from main_window import main_window_start
from statistics_window import stat_window
def stretch_image(event, canvas):
    global resized_image_tk
    width1 = event.width
    height1 = event.height
    resized_image = image_original.resize((width1,height1))
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0,0,image=resized_image_tk,anchor = "nw")

def start_new_window():
    # call new main window from another file main_window
    main_window_start()

def start_statistics_window():
    # call statistics window to show history
    stat_window()

def start_game_window():
    pass

def exit(window):
    window.quit()

def main():
    window = tk.Tk()
    print("attribute of window: ",window.__dict__)
    window.title("TYPEWIZ")
    window.minsize(width=700,height=400)

    #For background image processing
    global image_original
    image_original = Image.open("wallpaperflare.png")
    photo_image_tk = ImageTk.PhotoImage(image=image_original)

    canvas = tk.Canvas(master=window,bd=0,highlightthickness=0,highlightbackground="black",relief="ridge")
    canvas.place(relwidth=1,relheight=1)
    #binding the the stretching event to stretch_image function
    canvas.bind("<Configure>",func=lambda event:stretch_image(event, canvas))



    #defining button
    start_btn = ctk.CTkButton(master=window,text="TYPING TEST",
                    command=start_new_window,fg_color="#180227",
                    bg_color="transparent",
                    corner_radius=1,font=("Goblin One", 15)
                    )
    game_btn = ctk.CTkButton(master=window,text="GAME",
                    command=start_game_window,fg_color="#180227",
                    bg_color="transparent",
                    corner_radius=1,font=("Goblin One", 15)
                    )
    statistics_btn = ctk.CTkButton(master=window,text="STATISTICS",
                    command=start_statistics_window,fg_color="#180227",
                    bg_color="transparent",
                    corner_radius=1,font=("Goblin One", 15)
                    )
    exit_btn = ctk.CTkButton(master=window,text="EXIT",
                    command=lambda:exit(window=window),fg_color=("#180227"),
                    bg_color="transparent",
                    corner_radius=1,font =("Goblin One",15)
                    )
    #placing buttons
    start_btn.place(relx=0.1,rely=0.4,relwidth=0.2,relheight=0.1)
    game_btn.place(relx=0.1,rely=0.55,relwidth=0.2,relheight=0.1)
    statistics_btn.place(relx=0.1,rely=0.7,relwidth=0.2,relheight=0.1)
    exit_btn.place(relx=0.1,rely=0.85,relwidth=0.2,relheight=0.1)




    window.mainloop()

if __name__=="__main__":
    main()