# This script will open Outlook even if closed and draft an email.
# Script can be set to trigger each night using a task scheduler

import win32com.client as win32

def EmailMe(address, subject, data):
    # https://stackoverflow.com/questions/20956424/how-do-i-generate-and-open-an-outlook-email-with-python-but-do-not-send
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = address
    mail.Subject = subject
    mail.HtmlBody = data
    mail.Display(True)


address = "user@email.com"
subject = "Plan the six most important tasks to accomplish tomorrow"
data = """
        Priority,    Description
        1,  
        2,     
        3, 
        4, 
        5, 
        6,
"""

# https://pythonprogramming.altervista.org/python-to-make-html-tables-code/
data = data.splitlines()
data = [d.strip() for d in data]
data = [f"<tr><td>{d}</tr>" for d in data if d.strip() != ""]
data = "<table border=1>" + "".join(data) + "</table>"
# display(HTML(data))
data = data.replace("    ", "")
data = data.replace(",", "</td><td>")

EmailMe(address, subject, data)