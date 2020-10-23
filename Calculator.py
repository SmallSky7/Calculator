import wx
from Function import *

class Calculator(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title='Calculator', size=(430, 650))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#FFFFFF')

        self.result = []
        self.result_bat = []

        #文本框控件
        self.text = wx.TextCtrl(panel, size=(600, 100), style=wx.TE_RIGHT|wx.TE_READONLY)
        self.font1 = wx.Font(50, wx.MODERN, wx.NORMAL, wx.NORMAL, False, 'Consolas')
        self.text.SetFont(self.font1)

        #按钮控件
        self.add_button = wx.Button(panel, label="+", pos=(300, 100), size=(100, 100))
        self.back_button = wx.Button(panel, label="back", pos=(200, 100), size=(100, 100))
        self.delete_button = wx.Button(panel, label="c", pos=(100, 100), size=(100, 100))
        self.percent_button = wx.Button(panel, label="%", pos=(0, 100), size=(100, 100))
        self.nine_button = wx.Button(panel, label="9", pos=(200, 200), size=(100, 100))
        self.eight_button = wx.Button(panel, label="8", pos=(100, 200), size=(100, 100))
        self.seven_button = wx.Button(panel, label="7", pos=(0, 200), size=(100, 100))
        self.reduce_button = wx.Button(panel, label="-", pos=(300, 200), size=(100, 100))
        self.six_button = wx.Button(panel, label="6", pos=(200, 300), size=(100, 100))
        self.five_button = wx.Button(panel, label="5", pos=(100, 300), size=(100, 100))
        self.four_button = wx.Button(panel, label="4", pos=(0, 300), size=(100, 100))
        self.mulity_button = wx.Button(panel, label="*", pos=(300, 300), size=(100, 100))
        self.three_button = wx.Button(panel, label="3", pos=(200, 400), size=(100, 100))
        self.two_button = wx.Button(panel, label="2", pos=(100, 400), size=(100, 100))
        self.one_button = wx.Button(panel, label="1", pos=(0, 400), size=(100, 100))
        self.division_button = wx.Button(panel, label="/", pos=(300, 400), size=(100, 100))
        self.point_button = wx.Button(panel, label=".", pos=(200, 500), size=(100, 100))
        self.zero_button = wx.Button(panel, label="0", pos=(100, 500), size=(100, 100))
        self.reverse_button = wx.Button(panel, label="+/-", pos=(0, 500), size=(100, 100))
        self.equal_button = wx.Button(panel, label="=", pos=(300, 500), size=(100, 100))

        self.switcher_name={
            1:self.one_button,
            2:self.two_button,
            3:self.three_button,
            4:self.four_button,
            5:self.five_button,
            6:self.six_button,
            7:self.seven_button,
            8:self.eight_button,
            9:self.nine_button,
            10:self.zero_button,
            11:self.point_button,
            12:self.add_button,
            13:self.reduce_button,
            14:self.mulity_button,
            15:self.division_button,
            16:self.reverse_button,
            17:self.back_button,
            18:self.delete_button,
            19:self.percent_button,
            20:self.equal_button          
        }

        #设置字体
        for i in range(1,21):
            self.font2 = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, 'Consolas')
            self.switcher_name[i].SetFont(self.font2)
        
        #设置控件背景颜色
        self.text.SetBackgroundColour('#FFFFFF')
        for i in range(1, 11):
            self.switcher_name[i].SetBackgroundColour('#FFFFFF')
        self.switcher_name[20].SetBackgroundColour('#9370DB')
        for i in range(11, 20):
            self.switcher_name[i].SetBackgroundColour('EEEEE0')

        #基本按钮(只需要显示，没有复杂函数的)绑定事件
        for i in range(1, 16):
            self.Bind(wx.EVT_BUTTON, self.onButtonClick, self.switcher_name[i])
        
        #特殊按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.onTextPrint, self.equal_button)
        self.Bind(wx.EVT_BUTTON, self.onTextPrint, self.reverse_button)

        #创建boxsizer，支持页面自适应
        box1 = wx.BoxSizer()
        box1.Add(self.percent_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box1.Add(self.delete_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box1.Add(self.back_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box1.Add(self.add_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)

        box2 = wx.BoxSizer()
        box2.Add(self.seven_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box2.Add(self.eight_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box2.Add(self.nine_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box2.Add(self.reduce_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)

        box3 = wx.BoxSizer()
        box3.Add(self.four_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box3.Add(self.five_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box3.Add(self.six_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box3.Add(self.mulity_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)

        box4 = wx.BoxSizer()
        box4.Add(self.three_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box4.Add(self.two_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box4.Add(self.one_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box4.Add(self.division_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)

        box5 = wx.BoxSizer()
        box5.Add(self.point_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box5.Add(self.zero_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box5.Add(self.reverse_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)
        box5.Add(self.equal_button, proportion = 1, flag=wx.EXPAND|wx.ALL, border=1)

        box6 = wx.BoxSizer(wx.VERTICAL)
        box6.Add(self.text, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
        box6.Add(box1, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
        box6.Add(box2, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
        box6.Add(box3, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
        box6.Add(box4, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
        box6.Add(box5, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
        panel.SetSizer(box6)

    def onButtonClick(self, event):
        ID = event.GetEventObject().GetLabel()
        Button_ID = event.GetEventObject().Get
        self.result.append(ID)
        self.text.AppendText(str(self.result[-1]))
        
        if self.result[-1] == '1' or self.result[-1] == '2' or self.result[-1] == '3' or self.result[-1] == '4' or self.result[-1] == '5' or self.result[-1] == '6' or self.result[-1] == '7' or self.result[-1] == '8' or self.result[-1] == '9' or self.result[-1] == '0':
            if len(self.result) >= 2:
                if self.result[-2] == '1' or self.result[-2] == '2' or self.result[-2] == '3' or self.result[-2] == '4' or self.result[-2] == '5' or self.result[-2] == '6' or self.result[-2] == '7' or self.result[-2] == '8' or self.result[-2] == '9':
                    new_element = self.result[-2] + self.result[-1]
                    print(new_element)
                    del(self.result[-2])
                    del(self.result[-1])
                    self.result.append(new_element)
                if self.result[-2] == '0':
                    del(self.result[-2])

        print(self.result)
        return self.result
    

    def onTextPrint(self, event):
        ID = event.GetEventObject().GetLabel()

        if ID == '+/-':
            self.result.append('+/-')
        final_result = Calculator_rules(self.result)
        self.text.SetValue(str(final_result[0]))


if __name__ == '__main__':
    app = wx.App()
    calculator = Calculator()
    calculator.Show()
    app.MainLoop()
