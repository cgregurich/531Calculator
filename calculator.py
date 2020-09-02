from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from constants import *
		

class Calculator(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		ttk.Button(self, text="Calculate", command=self.calc_all).grid(row=5, column=0)

		# Create frames
		self.start = Frame(self)
		self.w1 = Frame(self)
		self.w2 = Frame(self)
		self.w3 = Frame(self)

		# Set default BBB mode option
		self.bbb = StringVar(value="Pyramid")

		# Put frames on screen
		self.start.grid(row=1, column=0, sticky=N)
		self.w1.grid(row=2, column=0, sticky=W, pady=(10,10), padx=(15, 25))
		self.w2.grid(row=3, column=0, sticky=W, pady=(10,10), padx=(15, 25))
		self.w3.grid(row=4, column=0, sticky=W, pady=(10,10), padx=(15, 25))

		# Button that displays program's percentages
		ttk.Button(self.start, text="Percentages", command=lambda: controller.show_frame("DisplayPercentages")).grid(row=0, column=2)

		self.max = 0

		self.w1_labels = []
		self.w2_labels = []
		self.w3_labels = []

		self.w1_bbb_labels = []
		self.w2_bbb_labels = []
		self.w3_bbb_labels = []


		self.create_labels()

		self.populate_start()
		





	def create_labels(self):
		# Create labels for displaying sets and reps
		for w in range(1, 4):
			if w == 1:
				frame = self.w1
				labels = self.w1_labels
				bbb_labels = self.w1_bbb_labels
			elif w == 2:
				frame = self.w2
				labels = self.w2_labels
				bbb_labels = self.w2_bbb_labels
			elif w == 3:
				frame = self.w3
				labels = self.w3_labels
				bbb_labels = self.w3_bbb_labels

			# Create Main lift labels
			for x in range(0, 3):
				lbl = Label(frame, text="", font=SETS_FONT)
				labels.append(lbl)
				lbl.grid(row=1, column=x+1)

			# Create BBB lift labels
			for x in range(0, 5):
				lbl = Label(frame, text="", font=SETS_FONT)
				bbb_labels.append(lbl)
				lbl.grid(row=2, column=x+1)

		for w in range(1, 4):
			self.populate_week(w)
			self.calc_and_fill_main(w)
			self.calc_and_fill_bbb(w)


	def calc_all(self):
		self.max = self.entry_max.get()
		if not self.max:
			messagebox.showerror("Error", "Enter a max")
			return False
		if self.bbb.get() == "Select":
			messagebox.showerror("Error", "Select a BBB scheme")
			return False
		self.max = int(self.max)
		for x in range(1, 4):
			self.calc_and_fill_main(x)
			self.calc_and_fill_bbb(x)

		
	# PERCENTAGES
	# 65, 75, 85
	# 70, 80, 90
	# 75, 85, 95
	def calc_main(self, week):
		lifts = []
		if week == 1:
			per = (.65, .75, .85)
		elif week == 2:
			per = (.7, .8, .9)
		elif week == 3:
			per = (.75, .85, .95)
		for p in per:
			lifts.append(5 * round((self.max * p) / 5))
		return lifts



	def calc_and_fill_main(self, week):
		lifts = self.calc_main(week)
		if week == 1:
			labels = self.w1_labels
			reps = ('5', '5', '5+')
		elif week == 2:
			labels = self.w2_labels
			reps = ('3', '3', '3+')
		elif week == 3:
			labels = self.w3_labels
			reps = ('5', '3', '1+')

		for i in range(0, 3):
			labels[i].config(text=f"{lifts[i]}x{reps[i]}")
			

	def calc_bbb(self):
		per = []
		if self.bbb.get() == "Ascending":
			per = (.3, .4, .5, .6, .7)
		elif self.bbb.get() == "Descending":
			per = (.7, .6, .5, .4, .3)
		elif self.bbb.get() == "Pyramid":
			per = (.5, .6, .7, .6, .5)
		lifts = []
		for p in per:
			lifts.append(5 * round((self.max * p) / 5))
		return lifts

	def calc_and_fill_bbb(self, week):
		lifts = self.calc_bbb()
		if not lifts:
			lifts = (0, 0, 0, 0, 0)
		reps = 10
		if week == 1:
			labels = self.w1_bbb_labels
		elif week == 2:
			labels = self.w2_bbb_labels
		elif week == 3:
			labels = self.w3_bbb_labels
		for i in range(0, 5):
			labels[i].config(text=f"{lifts[i]}x{reps}")




	def populate_start(self):
		bbb_options = ["Ascending", "Descending", "Pyramid"]

		Label(self.start, text="Enter max", font=HEADER_FONT).grid(row=0, column=0, padx=(10, 0), sticky=W)
		self.entry_max = ttk.Entry(self.start, width=8)
		self.entry_max.grid(row=0, column=1)
		Label(self.start, text="BBB %", font=HEADER_FONT).grid(row=1, column=0)
		ttk.OptionMenu(self.start, self.bbb, "Pyramid", *bbb_options).grid(row=1, column=1)

	def populate_week(self, week):
		if week == 1:
			frame = self.w1
		elif week == 2:
			frame = self.w2
		elif week == 3:
			frame = self.w3

		Label(frame, text=f"Week {week}", font=BOLD_FONT).grid(row=0, column=0, sticky=W)
		Label(frame, text="Main:", font=HEADER_FONT).grid(row=1, column=0, sticky=W)
		Label(frame, text="BBB:", font=HEADER_FONT).grid(row=2, column=0, sticky=W)


		







