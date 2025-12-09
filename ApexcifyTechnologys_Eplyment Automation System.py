

#                              Emails Automation 


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox


#------------------------------------------------------------------
# Part 1 -- Email Automation main logic code
#------------------------------------------------------------------

# predefined email list

e_list = [
    'student1@university.com','student2@university.com',
    'student3@university.com','student3@university.com',
    'student3@university.com','student3@university.com',
    'student3@university.com','student3@university.com',
    'student3@university.com','student3@university.com',
    'student3@university.com','student3@university.com',
    'student3@university.com','student3@university.com',
    'student3@university.com','student3@university.com',
    'student3@university.com','student3@university.com',
    'student3@university.com','student3@university.com'
]
def send_emails(sender_e,sender_password,subject,body):
    try:
        for receiver_e in e_list:
            msg  = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender_e
            msg['To'] = receiver_e

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender_e,sender_password)
            server.sendmail(sender_e,receiver_e,msg.as_string())
            server.quit()

        return True
    except Exception as e:
      print('Error:',e)
      return False

#---------------------------------------------------
#  Part 2 -- GUI Code for interface 
#---------------------------------------------------


def send_email_gui():
    sender = enter_email.get()
    password = enter_password.get()
    subject = enter_sub.get()
    body = text_msg.get('1.0',tk.END)

    if  send_emails(sender,password,subject,body):
        messagebox.showinfo('Success', 'Emails sent successfully!')
    else:
        messagebox.showerror('Error','Failed tp send emails.')

# main window
window = tk.Tk()     
window.title('Email Automation System')
window.geometry('500x450')

tk.Label(window, text = 'Sender Email:').pack()
enter_email = tk.Entry(window,width=40)
enter_email.pack()

tk.Label(window,text='Password').pack()
enter_password = tk.Entry(window, width=40, show='*')
enter_password.pack()

tk.Label(window,text = 'Email Subject:').pack()
enter_sub = tk.Entry(window,width=40)
enter_sub.pack()

tk.Label(window,text='Message:').pack()
text_msg = tk.Text(window,width=50,height=10)
text_msg.pack()

tk.Button(window,text='Send Emails',command=send_email_gui).pack(pady = 10)
window.mainloop()
            