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
        break

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

  def close_by_title(self, window_title):
    titles = gw.getAllTitles()
    window = None

    # Loop through all titles and search for a match
    for title in titles:
      if str(title).startswith(str(window_title)):
        window = gw.getWindowsWithTitle(title=title)[0]
        break  # Exit loop after finding the first match

    if window is None:
      print("Window not found!")
      return

    # Close the window using Win32 API
    hwnd = window._hWnd
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
    print(f"Window '{window.title}' closed")

    



