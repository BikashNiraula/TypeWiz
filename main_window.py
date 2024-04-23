import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image,ImageTk
from result_window import resultant_window
import time
import random 
#circular import
# from initial_window import main

demo_text = """Language is meant to be a playful, ever-shifting creation but we have been taught, and most of us continue to believe, that language must obediently follow precisely prescribed rules that govern clear sentence structures, specific word orders, correct spellings, and proper pronunciations."""


i=0
char_count=0
green_char_count = 0
red_char_count = 0
time_var_list=[] 

def restrict_enter_key(event):
    return 'break'
def update_text(event, textbox, text):
    global demo_text
    global i
    global char_count
    global green_char_count
    global red_char_count
    global time_var_list #Time every 1 character
    
    
    print(time_var_list)

    print(time_var)
    typed_char = event.char
    if typed_char == '' or typed_char== None:
        print("check for nullity")
        return

    # set the timer for the time_label
    time_var.set(str(round(time.time()-start_time,2)))
    demo_char = demo_text[i]


    cursor_pos = textbox.index(tk.INSERT)

    # Handle backspace
    if typed_char == '\x08':
        # Move the cursor back one position
        cursor_pos = textbox.index(tk.INSERT + "-1c")

        start = cursor_pos   # Start of the current character
        print(start)
        end = cursor_pos + "+1c"  # End of the current character
        print(text.tag_names(cursor_pos))
        if("highlight_green" in text.tag_names(cursor_pos)):
            green_char_count-=1
            print("green count removed")
        elif("highlight_red" in text.tag_names(cursor_pos)):
            red_char_count-=1
            print('red count removed')
        print("Backspace")
        text.tag_remove(text.tag_names(cursor_pos),start,end)
        print("typed:",typed_char,"==","demo:",demo_char," value of i",i)
        # To compensate for the bug when the backspace overcompensates
        char_count-=1
        i-=1

        # remove from the time_var_list
        if(len(time_var_list)==0):
            time_var_list=[]
        else:
            time_var_list.pop()
        print(time_var_list)
        if(i<0):
            i=0
        return
    
    #demo_char = demo_text[i]
    print("typed:",typed_char,"==","demo:",demo_char," value of i",i)

    if typed_char == demo_char:
        start = cursor_pos   # Start of the current character
        print(start)
        end = cursor_pos + "+1c"  # End of the current character
        print("Inside this if state ment")
        text.tag_add("highlight_green", start, end)
        text.tag_config("highlight_green", foreground="green")
        #green = True
        time_var_list.append(float(time_var.get()))
        i+=1
        char_count+=1
        green_char_count+=1
        return
    else:
        start = cursor_pos   # Start of the current character
        end = cursor_pos + "+1c"  # End of the current character
        print("the position is ",start,end)
        text.tag_add("highlight_red", start, end)
        text.tag_config("highlight_red", foreground="red")
        time_var_list.append(float(time_var.get()))
        i+=1
        char_count+=1
        red_char_count+=1
        return
        
    

def start_timer(textbox,countdown_label,countdown_seconds=3):
    global start_time
    countdown_label.configure(text=str(countdown_seconds))
    if countdown_seconds > 0:
        countdown_label.after(1000, start_timer,textbox,countdown_label,countdown_seconds-1)
        
    else:
        countdown_label.place_forget()
        start_time = time.time()
        textbox.configure(state = "normal")
        textbox.focus()
    
def generate_text(text, textbox,countdown_label):
    global demo_text
    text_list = ["Nepal, the land of majestic mountains, colorful prayer flags, and momos that will make your taste buds do a happy dance! This country has it all - from the serene beauty of the Himalayas to the bustling streets of Kathmandu where dodging motorcycles is practically an Olympic sport. And let's not forget about the mischievous monkeys in Swayambhunath Temple who will steal your snacks if you're not careful. Nepal is a place where you can find inner peace while simultaneously testing your negotiation skills at every turn - whether haggling for souvenirs or convincing yourself that eating one more plate of dal bhat won't hurt. So pack your bags, grab your sense of adventure (and maybe some extra snacks), and get ready for a wild ride in Nepal!",
                 "The United States' double standards and hypocrisy are evident in various aspects. Whether it is their foreign policy, human rights record, or economic practices, the US often portrays itself as a champion of democracy and justice while engaging in actions that contradict these principles. This hypocrisy undermines their credibility and raises questions about their true intentions and motivations",
                 "Radicalism in religion poses significant challenges to social cohesion, as it can lead to divisions, conflicts, and even acts of terrorism. It is crucial for societies to address these concerns by promoting dialogue, understanding, and education to counter the influence of radical ideologies and foster a more inclusive and peaceful religious environment.",
                 "Samsung, a renowned multinational conglomerate, is widely recognized for its innovative and cutting-edge technology solutions. With a strong focus on research and development, Samsung has consistently pushed the boundaries of what is possible in the tech industry. Samsung's commitment to quality and user-friendly designs has made it a trusted brand that continues to shape the future of technology.",
                 "The paragraph containing complex vocabulary can be rephrased in a manner that simplifies the language used. This can involve breaking down intricate terms into more easily understandable words, ensuring that the message remains clear and accessible to a wider audience. By avoiding convoluted language and opting for simpler alternatives, the paragraph can be made more comprehensible without losing its original meaning or intent.",
                 "Politics in Nepal has always been an interesting subject to observe, with its unique blend of drama and unpredictability. The political landscape of this nation is akin to a rollercoaster ride, where alliances are formed and broken at the drop of a hat. It seems that politicians here have mastered the art of making promises they never intend to keep, leaving the citizens in a perpetual state of disillusionment.",
                 "Ah, the never-ending game of political musical chairs in Nepal, where politicians seem to be constantly rotating in and out of power without any real progress being made. It's almost comical how easily these politicians swap seats, as if it's all just a game to them while the citizens suffer the consequences of their actions. Oh, what a delightful spectacle to witness, the political circus of Nepal.",
                 "A typing assessment evaluates an individual's typing speed and accuracy by measuring how quickly and accurately they can type a given passage of text. This evaluation is often used by employers to assess a candidate's proficiency in typing, which is an essential skill in many jobs that require extensive computer use. Typing tests can vary in length and difficulty, but they all aim to provide an objective measure of a person's typing abilities.",
                 "Oh, how wonderful it is to have AI constantly monitoring our every move, making decisions for us, and predicting our every desire. It's not like we're slowly giving up our autonomy and privacy to machines that may or may not have our best interests at heart. Who needs free will when we have AI to tell us what to do and think? It's truly a utopia we're living in, where our robot overlords reign supreme and we're just along for the ride. ",
                 "Language is meant to be a playful, ever-shifting creation but we have been taught, and most of us continue to believe, that language must obediently follow precisely prescribed rules that govern clear sentence structures, specific word orders, correct spellings, and proper pronunciations."]
    # generate demo text randomly
    curr_text = demo_text
    text_list.remove(curr_text)
    demo_text = text_list[random.randint(0,8)]
    text_list.append(curr_text)
    print(demo_text)
    # update the countdown_label
    countdown_label.place(relx=0.5,rely=0.4,anchor="center")
    countdown_label.configure(text="")
    text.configure(state="normal")
    textbox.configure(state="normal")
    textbox.delete(1.0,tk.END)
    text.delete(1.0,tk.END)
    text.insert(ctk.INSERT,demo_text)
    #reset global variables
    global i
    global char_count
    global red_char_count
    global green_char_count
    global time_var
    time_var.set("")
    i=0
    char_count=0
    red_char_count=0
    green_char_count=0
    #forcefully update the window
    text.configure(state = "disabled")
    textbox.configure(state = "disabled")
    text.update()
    textbox.update()

# def go_back(main_window):
#     main_window.quit()
#     main()



def main_window_start():
    global i
    i=0
    global char_count
    char_count = 0
    global green_char_count
    global red_char_count
    global demo_text
    green_char_count = 0
    red_char_count = 0
    #str_val = tk.StringVar()
    global time_var
    time_var = tk.StringVar(value="000")
    main_window = tk.Toplevel(background="#180227")
    main_window.title("TYPEWIZ")
    main_window.minsize(width = 700,height = 400)

    time_label = ctk.CTkLabel(master=main_window,textvariable=time_var)
    time_label.pack(anchor="center")


    text = ctk.CTkTextbox(master=main_window)
    text.insert(ctk.INSERT,demo_text)
    text.configure(state = "disabled")
    text.place(relx = 0.5,rely=0.2,relwidth=0.7,relheight = 0.25,anchor = "center")

    #generate_icon = tk.PhotoImage(file='generate_text.png')
    
    generate_text_btn = tk.Button(master=main_window,
                                  command=lambda:generate_text(text=text,textbox = textbox,countdown_label=countdown_label),
                                  fg="white",
                                  bg="blue",
                                  text="Generate",
                                  activebackground="#180227",
                                  activeforeground="white")
    generate_text_btn.place(relx=0.9,rely=0.2,anchor = "center")

    countdown_label = ctk.CTkLabel(master=main_window,text="",font=("Helvetica", 30))
    countdown_label.place(relx=0.5,rely=0.4,anchor="center")

    textbox = ctk.CTkTextbox(master=main_window)
    textbox.configure(state="disabled")
    textbox.place(relx = 0.5,rely=0.6,relwidth=0.7,relheight = 0.25,anchor = "center")

    start_timer_btn = ctk.CTkButton(master=main_window,text="START",command=lambda:start_timer(textbox,countdown_label,countdown_seconds=3))
    start_timer_btn.place(relx=0.5,rely=0.8,anchor ="center")

    btn_result = ctk.CTkButton(master=main_window,text="RESULT",command=lambda:resultant_window(char_count,red_char_count,green_char_count,time_var,time_var_list))
    btn_result.place(relx=0.5,rely=0.9,anchor = "center")


    # back_btn = tk.Button(master=main_window,
    #                               command=lambda:go_back(main_window),
    #                               fg="white",
    #                               bg="blue",
    #                               text="Back",
    #                               activebackground="#180227",
    #                               activeforeground="white")
    # back_btn.place(relx=0,rely=0,anchor = "nw")

    textbox.bind("<Key>",lambda event:update_text(event,textbox,text))
    textbox.bind("<Return>",restrict_enter_key)


    return