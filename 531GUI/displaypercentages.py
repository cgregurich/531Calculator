from tkinter import *
from constants import *

# 65, 75, 85
# 70, 80, 90
# 75, 85, 95


class DisplayPercentages(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		

		ttk.Button(self, text="Back", command=lambda: controller.show_frame("Calculator")).grid(row=0, column=0)

		self.frame_percentages = Frame(self)

		self.frame_percentages.grid(row=1, column=0, sticky="nsew")

		self.draw()


	def draw(self):
		# Create back button

		per = [[.65, .75, .85], [.7, .8, .9], [.75, .85, .95]]

		for r in range(3):
			for c in range(3):
				percentage = int(per[r][c] * 100)
				Label(self.frame_percentages, text=f"{percentage}%", font=SETS_FONT).grid(row=r, column=c)


		

