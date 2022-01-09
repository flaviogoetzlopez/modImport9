import webbrowser
"""
links = ["https://www.python.org/", "www.python.org", "https://www.youtube.com/", "www.youtube.com"]

# Normal
# Autoraise, tries to raise window by default, if set to false may not work because of window management systems
# new deals with other tab, window etc.


# webbrowser.open(links[0], new=0, autoraise=True)
# webbrowser.open(links[0], new=1, autoraise=True)
# webbrowser.open(links[1], new=2, autoraise=False)
# webbrowser.open_new(links[2])
# webbrowser.open_new_tab(links[3])


#Weird, same methods but with a browser 'controller', use get method, to use
#you can also reister new 'browsers' xd
win_def = webbrowser.get(using="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s")
win_def.open(links[0])



# print(type(webbrowser.get())) # Windows default
"""





# These Work:
chrome = webbrowser.get(using='C:/Program Files/Google/Chrome/Application/chrome.exe %s')
chrome.open_new("https://www.python.org/")

default = webbrowser.get()
default.open_new("https://www.python.org/")

webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open_new_tab("https://www.python.org/")

opera = webbrowser.get(using='C:/Users/flavi/AppData/Local/Programs/Opera GX/launcher.exe %s')
opera.open_new("https://www.python.org/")

default = webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s")
default.open_new("https://www.python.org/")



# notwork = webbrowser.get("C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe %s")
# notwork.open_new("https://www.python.org/") # because double slash

# mierda = webbrowser.get(using='google-chrome')
# mierda.open("https://www.python.org/") # system path

# chrome_anti_backslash = webbrowser.get(using='C:\Program Files\Google\Chrome\Application\chrome.exe %s')
# chrome_anti_backslash.open_new("https://www.python.org/") # not backslash, foreward slash

# chrome_tripol = webbrowser.get(using='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s')
# chrome_tripol("https://www.python.org/") # because double slash