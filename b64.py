import base64
import wx

class MainFrame(wx.Frame):
           
    def onb64decode(self, event):
        encoded_text = self.upper_box.GetValue()
        try:
            decoded_text = base64.b64decode(encoded_text).decode('utf-8')
            self.lower_box.SetValue(decoded_text)
        except Exception as e:
            self.lower_box.SetValue(f"Error on decoding: {e}")

    def onb64encode(self, event):
        decoded_text = self.upper_box.GetValue()
        try:
            encoded_text = base64.b64encode(decoded_text.encode('utf-8')).decode('utf-8')
            self.lower_box.SetValue(encoded_text)

        except Exception as e:
            self.lower_box.SetValue(f"Error on encoding: {e}")

    def oncopy(self, event):
        if wx.TheClipboard.Open():
            data = wx.TextDataObject(self.lower_box.GetValue())
            wx.TheClipboard.SetData(data)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Unable to open the clipboard.", "Error")


    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        window_sizer = wx.BoxSizer(wx.VERTICAL)
                                
        self.upper_box = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        window_sizer.Add(self.upper_box, 1, wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND, 10)

        upper_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.b64decode = wx.Button(self, wx.ID_ANY, 'base64 decode', (10, 10))
        self.b64encode = wx.Button(self, wx.ID_ANY, 'base64 encode', (10, 10))
        upper_button_sizer.Add(self.b64decode)
        upper_button_sizer.Add(self.b64encode)
        window_sizer.Add(upper_button_sizer, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 12)

        self.lower_box = wx.TextCtrl(self, style=wx.TE_READONLY|wx.TE_MULTILINE)
        window_sizer.Add(self.lower_box, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 10)

        lower_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.copy = wx.Button(self, wx.ID_ANY, 'copy to clipboard', (10, 10))
        lower_button_sizer.Add(self.copy)
        window_sizer.Add(lower_button_sizer, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 12)

        self.b64decode.Bind(wx.EVT_BUTTON, self.onb64decode)
        self.b64encode.Bind(wx.EVT_BUTTON, self.onb64encode)
        self.copy.Bind(wx.EVT_BUTTON, self.oncopy)

        self.SetSizer(window_sizer)        

def main():
    app = wx.App()
    frame = MainFrame(None, wx.ID_ANY, "B64", size=(1200, 700))
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()

