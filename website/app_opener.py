import pygetwindow as gw
import pyautogui
import win32gui
import win32con


class AppOpener():
  def __init__(self) -> None:
    pass

  def focus_by_title(self, window_title):
    titles = gw.getAllTitles()
    window = None

    #loops through all titles and searches if one starts with "Minecraft"
    for title in titles:
      if str(title).startswith(str(window_title)):
        window = gw.getWindowsWithTitle(title=title)[0]

    if window == None:
      print("Window not found!")
      return
    
    #fensterhandle bekommen
    hwnd = window._hWnd
    #check if window is minimized
    if win32gui.IsIconic(hwnd):
      #fokus again
      win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    window.activate()

    pyautogui.sleep(0.5)

    print("fokussiert")



