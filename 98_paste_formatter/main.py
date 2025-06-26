from tkinter import *
from tkinter import messagebox, font, colorchooser

import win32clipboard as clip
import win32con
import keyboard
import threading
import time

from format_gui import *

#--------------------- CLIPBOARD & FORMAT ---------------------#
def set_clipboard_rtf(rtf_text):
    # Put RTF content into clipboard (Win API)
    clip.OpenClipboard()
    clip.EmptyClipboard()
    rtf_format = clip.RegisterClipboardFormat("Rich Text Format")
    clip.SetClipboardData(rtf_format, rtf_text.encode('utf-8'))
    clip.CloseClipboard()

def make_rtf(text, fmt):
    """Tạo chuỗi RTF từ text với định dạng trong fmt (dict)"""
    rtf = r"{\rtf1\ansi\deff0"
    if fmt["font"]:
        rtf += fr"{{\fonttbl\f0\fnil\fcharset0 {fmt['font']};}}"
        rtf += r"\f0"

    if fmt["size"]:
        rtf += fr"\fs{fmt['size'] * 2}"  # RTF dùng đơn vị nửa-point

    if fmt["color"]:
        # thêm bảng màu: màu đầu tiên luôn là đen, màu người dùng chọn là màu thứ hai
        r, g, b = fmt["color"]
        rtf += fr"{{\colortbl ;\red{r}\green{g}\blue{b};}}"
        rtf += r"\cf1"

    if fmt["bold"]:
        text = r"\b " + text + r"\b0"
    if fmt["italic"]:
        text = r"\i " + text + r"\i0"
    if fmt["underline"]:
        text = r"\ul " + text + r"\ul0"

    rtf += text + "}"
    return rtf

#--------------------- MONITOR CTRL + V ---------------------#

def on_ctrl_v(gui: FormatGUI):
    try:
        clip.OpenClipboard()
        if clip.IsClipboardFormatAvailable(win32con.CF_UNICODETEXT):
            raw_text = clip.GetClipboardData(win32con.CF_UNICODETEXT)
            clip.EmptyClipboard()
            clip.CloseClipboard()
        else:
            clip.CloseClipboard()
            return
    
    except:
        return

    fmt = gui.get_applied_format()
    rtf = make_rtf(raw_text, fmt)
    set_clipboard_rtf(rtf)

    # Send virtual Ctrl + V
    time.sleep(0.05)
    keyboard.press_and_release("ctrl+v")

#--------------------- MAIN ---------------------#

root = tk.Tk()
gui = FormatGUI(root)

keyboard.add_hotkey("ctrl+v", lambda: on_ctrl_v(gui))

root.mainloop()

