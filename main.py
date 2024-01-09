import tkinter as tk
import tkinter.ttk as ttk
from game import Board, Player


class GameGUI:
    def __init__(self, root):
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=3)

        self.headerStyle = ttk.Style()
        self.headerStyle.configure('TLabel', background='black', font=('Helevetica', 20), foreground='white', anchor='center')
        self.header = tk.Frame(root)
        self.headerText = ttk.Label(self.header, text='Tic Tac Toe', style='TLabel')

        self.buttonStyle = ttk.Style()
        self.buttonStyle.configure('TButton', font=('Helevetica', 75))
        self.buttonFrame = tk.Frame(root)
        self.button0 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(0))
        self.button1 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(1))
        self.button2 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(2))
        self.button3 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(3))
        self.button4 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(4))
        self.button5 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(5))
        self.button6 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(6))
        self.button7 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(7))
        self.button8 = ttk.Button(self.buttonFrame, text='', style='TButton', command=lambda: self.tileChange(8))

        self.head()
        self.gameScreen()


    def head(self):
        self.header.grid(row=0, column=0, sticky='nsew')
        self.header.grid_columnconfigure(0, weight=1)
        self.header.grid_rowconfigure(0, weight=1)
        self.headerText.grid(row=0, column=0, sticky='nsew')


    def headVictoryChange(self, player=None):
        if player != None:
            self.headerText['text'] = f"{player} wins!"
        else:
            self.headerText['text'] = "Congrats on your tie!"



    def gameScreen(self):
        self.buttonFrame.grid_forget()
        self.buttonFrame.grid(row=1, column=0, sticky='nsew')
        for column in range(3):
            self.buttonFrame.grid_columnconfigure(column, weight=1)
        for row in range(3):
            self.buttonFrame.grid_rowconfigure(row, weight=1)
        self.button0.grid(row=0, column=0, sticky='nsew')
        self.button1.grid(row=0, column=1, sticky='nsew')
        self.button2.grid(row=0, column=2, sticky='nsew')
        self.button3.grid(row=1, column=0, sticky='nsew')
        self.button4.grid(row=1, column=1, sticky='nsew')
        self.button5.grid(row=1, column=2, sticky='nsew')
        self.button6.grid(row=2, column=0, sticky='nsew')
        self.button7.grid(row=2, column=1, sticky='nsew')
        self.button8.grid(row=2, column=2, sticky='nsew')


    def tileChange(self, userInput):
        tileState = board.tileCheck(userInput)
        currentPlayer = player.playerCheck()
        if tileState == True:
            if userInput == 0:
                self.button0['text'] = currentPlayer
            elif userInput == 1:
                self.button1['text'] = currentPlayer
            elif userInput == 2:
                self.button2['text'] = currentPlayer
            elif userInput == 3:
                self.button3['text'] = currentPlayer
            elif userInput == 4:
                self.button4['text'] = currentPlayer
            elif userInput == 5:
                self.button5['text'] = currentPlayer
            elif userInput == 6:
                self.button6['text'] = currentPlayer
            elif userInput == 7:
                self.button7['text'] = currentPlayer
            elif userInput == 8:
                self.button8['text'] = currentPlayer
            else:
                pass
            board.tileListUpdate(userInput, currentPlayer)
            player.playerTurnChange(currentPlayer)
        boardCondition = board.boardCheck()
        if boardCondition != 'continue':
            self.boardClear()
            if boardCondition == 'p1 wins':
                if currentPlayer == 'X':
                    player.playerTurnChange(player.players[1])
                    self.headVictoryChange(player.players[0])
            elif boardCondition == 'p2 wins':
                self.headVictoryChange(player.players[1])
            elif boardCondition == 'tie':
                self.headVictoryChange()


    def boardClear(self):
        self.button0['text'], self.button1['text'], self.button2['text'], self.button3['text'], self.button4['text'], self.button5['text'], self.button6['text'], self.button7['text'], self.button8['text'] = ['' for _ in range(9)]
        board.tileListUpdate(None, None, True)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.title('Tic Tac Toe')
    root.geometry('600x900+0+0')
    GameGUI = GameGUI(root)
    board = Board()
    player = Player('X', 'O')
    root.mainloop()