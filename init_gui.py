from Tkinter import *
import ttk
import sys
from ruamel.yaml import YAML


def combo_action(event):
    global e_password
    if card_name.get() == 'OPEN':
        l_password.config(text='')
        e_password.destroy()
    else:
        l_password.config(text='password : ')
        e_password = Entry(window, bg='snow')
        e_password.grid(row=4, column=1, padx=10, pady=10)


def get_details():
    file_name = 'conf_gui.yaml'
    with open(file_name) as fp:
        file_load = YAML().load(fp)
    file_load['Group 1']['No_of_clients'] = e_no_of_clients.get()
    file_load['Group 1']['Connection'] = 'SSID-1'
    file_load['SSID-1']['SSID'] = e_ssid.get()
    if e_password.get().lower() == 'none':
        file_load['SSID-1']['key_mgmt'] = e_password.get()
    else:
        file_load['SSID-1']['password'] = e_password.get()
    with open(file_name, 'w')as fp:
        YAML().dump(file_load, fp)
    window.destroy()


window = Tk()
window.config(bg='dim gray')
window.wm_geometry("500x300+300+100")
window.title("Virtual WiFi Clients")

l_no_of_clients = Label(window, text='              ', fg='azure', bg='dim gray')
l_no_of_clients.grid(row=0, sticky=E)
l_no_of_clients = Label(window, text='No of Clients : ', fg='azure', bg='dim gray')
l_no_of_clients.grid(row=1, sticky=E, padx=10, pady=10)
l_ssid = Label(window, text='SSID : ', fg='azure', bg='dim gray')
l_ssid.grid(row=2, sticky=E, padx=10, pady=10)
l_encryption = Label(window, text='WiFi Encryption : ', fg='azure', bg='dim gray')
l_encryption.grid(row=3, sticky=E, padx=10, pady=10)
l_password = Label(window, text='Password : ', fg='azure', bg='dim gray')
l_password.grid(row=4, sticky=E, padx=10, pady=10)

card_name = StringVar()
combo_encrypt = ttk.Combobox(window, width=8, textvariable=card_name,
                             state='readonly', values=['WPA-PSK', 'OPEN'])
combo_encrypt.grid(row=3, column=1, padx=10, pady=10)
combo_encrypt.bind("<<ComboboxSelected>>", combo_action)

e_no_of_clients = Entry(window, bg='snow')
e_no_of_clients.grid(row=1, column=1, padx=10, pady=10)
e_ssid = Entry(window, bg='snow')
e_ssid.grid(row=2, column=1, padx=10, pady=10)
e_password = Entry(window, bg='snow')
e_password.grid(row=4, column=1, padx=10, pady=10)


btn = Button(window, text='Submit', bg='SkyBlue', command=get_details)
btn.grid(row=5, column=1, padx=10, pady=10)

window.mainloop()
