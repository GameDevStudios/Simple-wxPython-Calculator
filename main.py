import wx

class MainWindow( wx.Frame ): 
	def __init__( self, parent, title, id ): 
		defaultFont = wx.Font( 45, wx.DECORATIVE, wx.NORMAL, wx.NORMAL )

		wx.Frame.__init__( self, parent, id, title=title, size=(300, 300), style=wx.MINIMIZE_BOX | wx.CLOSE_BOX )

		self.panel = wx.Panel( self ) 

		self.sumOfCals = 0
		self.sumOfCalsText = wx.StaticText( self.panel, -1, str(self.sumOfCals), (10, 30), style=wx.ALIGN_RIGHT )

		self.mode = "add"

		self.sumOfCalsText.SetFont( defaultFont )

		self.oneButton = wx.Button( self.panel, label="1", pos=( 10, 100 ), size=( 50, 50 ) ) 
		self.twoButton = wx.Button( self.panel, label="2", pos=( 10+60, 100 ), size=( 50, 50 ) )
		self.threeButton = wx.Button( self.panel, label="3", pos=( 10+60+60, 100 ), size=( 50, 50 ) ) 
		self.fourButton = wx.Button( self.panel, label="4", pos=( 10, 100+30 ), size=( 50, 50 ) ) 
		self.fiveButton = wx.Button( self.panel, label="5", pos=( 10+60, 100+30 ), size=( 50, 50 ) ) 
		self.sixButton = wx.Button( self.panel, label="6", pos=( 10+60+60, 100+30 ), size=( 50, 50 ) )
		self.sevenButton = wx.Button( self.panel, label="7", pos=( 10, 100+60 ), size=( 50, 50 ) ) 
		self.eightButton = wx.Button( self.panel, label="8", pos=( 10+60, 100+60 ), size=( 50, 50 ) ) 
		self.nineButton = wx.Button( self.panel, label="9", pos=( 10+60+60, 100+60 ), size=( 50, 50 ) ) 

		self.clearButton = wx.Button( self.panel, label="CLEAR", pos=( 10, 100+60+60 ), size=( 180, 50 ) )

		self.addModeButton = wx.Button( self.panel, label="+", pos=( 10+60+60+60+20, 100 ), size=( 30, 50 ) )
		self.subModeButton = wx.Button( self.panel, label="-", pos=( 10+60+60+60+60, 100 ), size=( 30, 50 ) )
		self.mulModeButton = wx.Button( self.panel, label="*", pos=( 10+60+60+60+20, 100+30 ), size=( 30, 50 ) )
		self.divModeButton = wx.Button( self.panel, label="/", pos=( 10+60+60+60+60, 100+30 ), size=( 30, 50 ) )
		self.expModeButton = wx.Button( self.panel, label="^", pos=( 10+60+60+60+20, 100+60 ), size=( 30, 50 ) )

		self.Bind( wx.EVT_BUTTON, self.OnOneButtonClick, self.oneButton )
		self.Bind( wx.EVT_BUTTON, self.OnTwoButtonClick, self.twoButton )
		self.Bind( wx.EVT_BUTTON, self.OnThreeButtonClick, self.threeButton )
		self.Bind( wx.EVT_BUTTON, self.OnFourButtonClick, self.fourButton )
		self.Bind( wx.EVT_BUTTON, self.OnFiveButtonClick, self.fiveButton )
		self.Bind( wx.EVT_BUTTON, self.OnSixButtonClick, self.sixButton )
		self.Bind( wx.EVT_BUTTON, self.OnSevenButtonClick, self.sevenButton )
		self.Bind( wx.EVT_BUTTON, self.OnEightButtonClick, self.eightButton )
		self.Bind( wx.EVT_BUTTON, self.OnNineButtonClick, self.nineButton )

		self.Bind( wx.EVT_BUTTON, self.OnClearButtonClick, self.clearButton )

		self.Bind( wx.EVT_BUTTON, self.OnAddButtonClick, self.addModeButton )
		self.Bind( wx.EVT_BUTTON, self.OnSubButtonClick, self.subModeButton )
		self.Bind( wx.EVT_BUTTON, self.OnMulButtonClick, self.mulModeButton )
		self.Bind( wx.EVT_BUTTON, self.OnDivButtonClick, self.divModeButton )
		self.Bind( wx.EVT_BUTTON, self.OnExpButtonClick, self.expModeButton )

		self.Center() 
		self.Show(True) 

	def OnOneButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 1
		elif self.mode == "sub":
			self.sumOfCals -= 1
		elif self.mode == "mul":
			self.sumOfCals *= 1
		elif self.mode == "div":
			self.sumOfCals /= 1
		elif self.mode == "exp":
			self.sumOfCals ** 1
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnTwoButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 2
		elif self.mode == "sub":
			self.sumOfCals -= 2
		elif self.mode == "mul":
			self.sumOfCals *= 2
		elif self.mode == "div":
			self.sumOfCals /= 2
		elif self.mode == "exp":
			self.sumOfCals ** 2
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnThreeButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 3
		elif self.mode == "sub":
			self.sumOfCals -= 3
		elif self.mode == "mul":
			self.sumOfCals *= 3
		elif self.mode == "div":
			self.sumOfCals /= 3
		elif self.mode == "exp":
			self.sumOfCals ** 3
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnFourButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 4
		elif self.mode == "sub":
			self.sumOfCals -= 4
		elif self.mode == "mul":
			self.sumOfCals *= 4
		elif self.mode == "div":
			self.sumOfCals /= 4
		elif self.mode == "exp":
			self.sumOfCals ** 4
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnFiveButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 5
		elif self.mode == "sub":
			self.sumOfCals -= 5
		elif self.mode == "mul":
			self.sumOfCals *= 5
		elif self.mode == "div":
			self.sumOfCals /= 5
		elif self.mode == "exp":
			self.sumOfCals ** 5
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnSixButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 6
		elif self.mode == "sub":
			self.sumOfCals -= 6
		elif self.mode == "mul":
			self.sumOfCals *= 6
		elif self.mode == "div":
			self.sumOfCals /= 6
		elif self.mode == "exp":
			self.sumOfCals ** 6
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnSevenButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 7
		elif self.mode == "sub":
			self.sumOfCals -= 7
		elif self.mode == "mul":
			self.sumOfCals *= 7
		elif self.mode == "div":
			self.sumOfCals /= 7
		elif self.mode == "exp":
			self.sumOfCals ** 7
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnEightButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 8
		elif self.mode == "sub":
			self.sumOfCals -= 8
		elif self.mode == "mul":
			self.sumOfCals *= 8
		elif self.mode == "div":
			self.sumOfCals /= 8
		elif self.mode == "exp":
			self.sumOfCals ** 8
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnNineButtonClick( self, event ):
		if self.mode == "add":
			self.sumOfCals += 9
		elif self.mode == "sub":
			self.sumOfCals -= 9
		elif self.mode == "mul":
			self.sumOfCals *= 9
		elif self.mode == "div":
			self.sumOfCals /= 9
		elif self.mode == "exp":
			self.sumOfCals ** 9
		else:
			pass

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnClearButtonClick( self, event ):
		self.sumOfCals = 0

		self.sumOfCalsText.SetLabel( str( self.sumOfCals ) )

	def OnAddButtonClick( self, event ):
		self.mode = "add"

	def OnSubButtonClick( self, event ):
		self.mode = "sub"

	def OnMulButtonClick( self, event ):
		self.mode = "mul"

	def OnDivButtonClick( self, event ):
		self.mode = "div"

	def OnExpButtonClick( self, event ):
		self.mode = "exp"

app = wx.App(False)

mainWindow = MainWindow( None, 'My wxPython Calculator', wx.ID_ANY )

app.MainLoop()
