class SettingsPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		ttk.Button(self, text="Back", command=lambda: controller.show_frame(HomePage)).pack()