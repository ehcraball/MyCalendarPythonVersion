# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.4 on Mon Mar 13 10:01:52 2023
#

import wx
# begin wxGlade: dependencies
import wx.adv
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Ajout(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Ajout.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("Ajout de Topic")

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(6, 2, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        lblNom = wx.StaticText(self, wx.ID_ANY, "Nom :")
        grid_sizer_1.Add(lblNom, 0, wx.ALIGN_CENTER, 0)

        self.txtNom = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_1.Add(self.txtNom, 0, wx.ALIGN_CENTER | wx.RIGHT, 25)

        lblDesc = wx.StaticText(self, wx.ID_ANY, "Description :")
        grid_sizer_1.Add(lblDesc, 0, wx.ALIGN_CENTER, 0)

        self.txtDesc = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_1.Add(self.txtDesc, 0, wx.ALIGN_CENTER | wx.RIGHT, 25)

        lblDebut = wx.StaticText(self, wx.ID_ANY, u"Début :")
        grid_sizer_1.Add(lblDebut, 0, wx.ALIGN_CENTER, 0)

        self.datepickerDebut = wx.adv.DatePickerCtrl(self, wx.ID_ANY)
        grid_sizer_1.Add(self.datepickerDebut, 0, wx.ALIGN_CENTER | wx.RIGHT, 25)

        lblFin = wx.StaticText(self, wx.ID_ANY, "Fin :")
        grid_sizer_1.Add(lblFin, 0, wx.ALIGN_CENTER, 0)

        self.datepickerFin = wx.adv.DatePickerCtrl(self, wx.ID_ANY)
        grid_sizer_1.Add(self.datepickerFin, 0, wx.ALIGN_CENTER | wx.RIGHT, 25)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.OnAjoutConfirmed, self.button_OK)
        # end wxGlade

    def OnAjoutConfirmed(self, event):  # wxGlade: Ajout.<event_handler>
        print("Event handler 'OnAjoutConfirmed' not implemented!")
        event.Skip()
        
# end of class Ajout
