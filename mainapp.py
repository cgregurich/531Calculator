from tkinter import *

from calculator import Calculator
from displaypercentages import DisplayPercentages


class MainApp(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)


		
		self.title("531 Calculator")

		self.config(width=375,height=375)

		self.pack_propagate(0)


		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for gui_class in Calculator, DisplayPercentages:
			frame = gui_class(container, self)

			self.frames[gui_class.__name__] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("Calculator")


	def show_frame(self, gui_class):
		frame = self.frames[gui_class]
		frame.tkraise()




def main():
	app = MainApp()
	app.mainloop()

if __name__ == '__main__':
	main()