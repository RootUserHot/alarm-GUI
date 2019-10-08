from classes import *

def windowDeleted():
    root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Alarm")
    root.geometry('470x50')
    root.protocol('WM_DELETE_WINDOW', windowDeleted)
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()
