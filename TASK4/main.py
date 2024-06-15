'''
Rock-Paper-Scissors Game
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
Game Logic: Determine the winner based on the user's choice and the computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and feedback.
'''
import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk
import random

class GameApp:
    def __init__(self, root):
        self.user_score = 0
        self.comp_score = 0
        
        # Create a custom button style
        self.style = ttk.Style()
        self.style.configure("MD.TButton", foreground="blue", background="#2196F3", font=("Roboto", 20), padx=10, pady=5)
        
        try:
            self.stone_img_path = "TASK4/image1.jpg"
            self.paper_img_path = "TASK4/image2.jpg"
            self.scissor_img_path = "TASK4/image3.jpg"
            
            self.stone_img = Image.open(self.stone_img_path)
            self.stone_img = ImageTk.PhotoImage(self.stone_img)

            self.paper_img = Image.open(self.paper_img_path)
            self.paper_img = ImageTk.PhotoImage(self.paper_img)

            self.scissor_img = Image.open(self.scissor_img_path)
            self.scissor_img = ImageTk.PhotoImage(self.scissor_img)

            # Load and resize image
            self.image_path = "TASK4/Q_mark.png"
            self.image = Image.open(self.image_path)
            # Resize image to desired dimensions (e.g., 200x200 pixels)
            self.image = self.image.resize((200, 200), Image.Resampling.LANCZOS)
            self.Q_mark_img = ImageTk.PhotoImage(self.image)
        except Exception as e:
            print(f"Error loading image: {e}")
            return
        
        # row 1
        heading_font = font.Font(root, weight="bold", underline=True, size=50)
        heading = ttk.Label(root, text="STONE PAPER SCISSORS", font=heading_font, anchor="center")
        heading.grid(column=0, row=0, columnspan=3, sticky="nsew", pady=(20, 10))
        
        # row 2
        label_font = font.Font(root, size=30)
        ttk.Label(root, text="Computer", font=label_font, anchor="center").grid(column=0, row=1, sticky="nsew", pady=(0, 20))
        ttk.Label(root, text="", anchor="center").grid(column=1, row=1, sticky="nsew")
        ttk.Label(root, text="User", font=label_font, anchor="center").grid(column=2, row=1, sticky="nsew", pady=(0, 20))
        
        # row 3
        if self.Q_mark_img:
            self.Computer_choice = ttk.Label(root, image=self.Q_mark_img,anchor="center")
            self.User_choice = ttk.Label(root, image=self.Q_mark_img,anchor="center")
            self.Computer_choice.grid(column=0, row=2, sticky="nsew")
            self.User_choice.grid(column=2, row=2, sticky="nsew")
            self.Computer_choice.image = self.Q_mark_img  # Keep a reference to avoid garbage collection
            self.User_choice.image = self.Q_mark_img  # Keep a reference to avoid garbage collection
            
            self.winnig_status = tk.Label(root, text="Winning Status", font=label_font, anchor="center")
            self.winnig_status.grid(column=1, row=2, sticky="nsew", pady=(0, 20))
            
            
            
        else:
            ttk.Label(root, text="Image not loaded", anchor="center").grid(column=0, row=2, sticky="nsew")
        
        # row 4
        self.comp_score_lbl = ttk.Label(root, text=f"Score: {self.comp_score}", font=font.Font(root, size=15), anchor="center")
        self.comp_score_lbl.grid(column=0, row=3, sticky="nsew", pady=(0, 20))
        ttk.Label(root, text="", anchor="center").grid(column=1, row=3, sticky="nsew")
        self.user_score_lbl =ttk.Label(root, text=f"Score: {self.user_score}", font=font.Font(root, size=15), anchor="center")
        self.user_score_lbl.grid(column=2, row=3, sticky="nsew", pady=(0, 20))

        # row 5
        self.start_next = ttk.Button(root, text="Start",command=self.start_game,style="MD.TButton")
        self.start_next.grid(column=1, row=4, pady=(20, 0))
        
        #row 6
        ttk.Button(root,text="New Game",command=self.new_game,style="MD.TButton").grid(column=1,row=5,pady=(20, 10))

        # Make the grid cells expand
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(3):
            root.grid_columnconfigure(i, weight=1)
            
    def game_choice(self,frame):
        
        ttk.Label(frame,text="Select Your Choice...",background="skyblue",font=font.Font(root, weight="bold", underline=True, size=30)).pack(side="top")
        self.img1 = tk.Button(frame,image=self.stone_img,text="stone",command=self.choose_stone).pack(side=tk.LEFT)
        self.img2 = tk.Button(frame,image=self.paper_img,command= self.choose_paper).pack(side=tk.LEFT)
        self.img3 = tk.Button(frame,image=self.scissor_img,command=self.choose_scissor).pack(side=tk.LEFT)
        
    def ComputerChoice(self,user_ch):
        choice = random.choice([self.stone_img,self.paper_img,self.scissor_img])
        self.Computer_choice.config(image=choice)
        match choice:
            case self.stone_img:
                comp_ch = "stone"
                
            case self.paper_img:
                comp_ch = "paper"
                
            case self.scissor_img:
                comp_ch = "scissor"
                
        self.game_result(user_ch,comp_ch)
        
        
    def choose_stone(self):
        self.User_choice.config(image=self.stone_img)
        self.frame.destroy()
        self.ComputerChoice("stone")
    
    def choose_paper(self):
        self.User_choice.config(image=self.paper_img)
        self.frame.destroy()
        self.ComputerChoice("paper")
        

    def choose_scissor(self):
        self.User_choice.config(image=self.scissor_img)
        self.frame.destroy()
        self.ComputerChoice("scissor")
        
    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._x = None
        self._y = None

    def do_move(self, event):
        x = self.frame.winfo_pointerx() - self._x
        y = self.frame.winfo_pointery() - self._y
        self.frame.geometry(f"+{x}+{y}")

                 
    def start_game(self):
        print("start")
        
        self.frame = tk.Toplevel()
        self.frame.overrideredirect(True)
        
        self.frame.config(bg="skyblue")
        title = "Choice Selecting Window..."
        
        # Create a custom title bar frame
        self.title_bar = tk.Frame(self.frame, bg="#2196F3", relief="raised", bd=2)
        self.title_bar.pack(side="top", fill="x")

        # Add a title label to the title bar
        self.title_label = tk.Label(self.title_bar, text=title, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.title_label.pack(side="left", padx=10)
        
        # Bind events for moving the window
        self.frame.bind("<ButtonPress-1>", self.start_move)
        self.frame.bind("<ButtonRelease-1>", self.stop_move)
        self.frame.bind("<B1-Motion>", self.do_move)
        
        popup_width = 500
        popup_height = 300
        
         # Calculate the center position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (popup_width // 2)
        y = (screen_height // 2) - (popup_height // 2)

        # # Set the geometry of the popup window
        self.frame.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        self.frame.resizable(False,False)
        
        self.frame.grab_set()
        
        # frame.geometry("510x200")
        self.game_choice(frame=self.frame)
    
    
    def new_game(self):
        print("new")
        self.comp_score = 0
        self.user_score = 0
        self.winnig_status.config(text=f"Winning Status\n")
        
        self.start_next.config(text="Start")
        self.comp_score_lbl.config(text=f"Score: {self.comp_score}")
        self.user_score_lbl.config(text=f"Score: {self.user_score}")
        
        self.User_choice.config(image=self.Q_mark_img)
        self.Computer_choice.config(image=self.Q_mark_img)
        
    def AnnounceWinner(self,winner,user_score,comp_score)    :
        announcement_win = tk.Toplevel()

        announcement_win.attributes("-toolwindow", True)
        announcement_win.title("Winner Announcement...")
        
        popup_width = 500
        popup_height = 300

        # Calculate the center position
        screen_width = announcement_win.winfo_screenwidth()
        screen_height = announcement_win.winfo_screenheight()
        x = (screen_width // 2) - (popup_width // 2)
        y = (screen_height // 2) - (popup_height // 2)

        # Set the geometry of the popup window
        announcement_win.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        label_font = font.Font(root, size=20)
        main_font = font.Font(root, size=20,weight="bold")
        
        if winner == "Commputer":
            label = tk.Label(announcement_win, text="You Loose!!\nBrtter Luck Next Time.",font=main_font)
            label.pack(padx=20, pady=20)
            
            label = tk.Label(announcement_win, text=f"Your Score: {user_score}",font=label_font)
            label.pack(padx=20, pady=20)
            
            label = tk.Label(announcement_win, text=f"Computers Score: {comp_score}",font=label_font)
            label.pack(padx=20, pady=20)
        
        else:
            label = tk.Label(announcement_win, text="CONGRATULATIONS...\nYou are the Winner!!",font=main_font)
            label.pack(padx=20, pady=20)
            
            label = tk.Label(announcement_win, text=f"Your Score: {user_score}",font=label_font)
            label.pack(padx=20, pady=20)
            
            label = tk.Label(announcement_win, text=f"Computers Score: {comp_score}",font=label_font)
            label.pack(padx=20, pady=20)
            
        self.new_game()
        
    def game_result(self,user,comp):
        print(f"{comp}\t{user}")
        # store beats scissor
        # scissor beats paper
        # paper beats stone
        winning_status = "Winning Status\n"
        
        if self.comp_score >=5 or self.user_score >=5:
            if self.comp_score >=5:
                print("Comp is a winner")
                self.AnnounceWinner("Commputer",self.user_score,self.comp_score)
            
            elif self.user_score >=5:
                print("User is a winner...")
                self.AnnounceWinner("User",self.user_score,self.comp_score)
        else:
            if ((user == "stone" and comp == "scissor") or (user == "scissor" and comp == "paper") or (user == "paper" and comp == "stone")):
                print("user Win...")
                self.winnig_status.config(text=f"{winning_status}User Won")
                self.user_score += 1
                self.user_score_lbl.config(text=f"Score: {self.user_score}")
                
            elif user == comp:
                print("Tie...")
                self.winnig_status.config(text=f"{winning_status}It's Tie...")
                
            else:
                print("Computer Win")
                self.winnig_status.config(text=f"{winning_status}Computer Won")
                self.comp_score += 1
                self.comp_score_lbl.config(text=f"Score: {self.comp_score}")
                
            self.start_next.config(text="Next Round")
                    

root = tk.Tk()
root.geometry("1000x600")
root.config()
root.minsize(1000,600)
popup_width = 1000
popup_height = 600

# Calculate the center position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (popup_width // 2)
y = (screen_height // 2) - (popup_height // 2)

# # Set the geometry of the popup window
root.geometry(f"{popup_width}x{popup_height}+{x}+{y}")


GameApp(root=root)


root.mainloop()
