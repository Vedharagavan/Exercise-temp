from Tkinter import *
import ttk
import sys
from ruamel.yaml import YAML


class Label_entry_box:
    def __init__(self, l_text, row_no):
        self.label = Label(window, text=l_text, fg='azure', bg='dim gray')
        self.label.grid(row=row_no, sticky=E, padx=10, pady=10)
        self.ebox = Entry(window, bg='snow')
        self.ebox.grid(row=row_no, column=1, padx=10, pady=10)


class Tk_var:
    def __init__(self):
        self.label = Label(window, text=' ', fg='azure', bg='dim grey')
        self.ebox = Entry(window, bg='snow')

    def labl(self, l_text, row_no):
        self.label = Label(window, text=l_text, fg='azure', bg='dim grey')
        self.label.grid(row=row_no, sticky=E, padx=10, pady=10)

    def ebox(self, row_no):
        self.ebox = Entry(window, bg='snow')
        self.ebox.grid(row=row_no, column=1, padx=10, pady=10)


def cmd_encrypt(event):
    global password
    if encrypt_type.get() == 'OPEN':
        password.label.config(text='')
        password.ebox.destroy()
    else:
        password = Label_entry_box('Password  :  ', 4)


def cmd_ip_method(event):
    global ip_prefix, netmask, def_gw
    if ip_method.get() == 'STATIC-IP':
        ip_prefix = Label_entry_box('IP Prefix', 6)
        netmask = Label_entry_box('Netmask', 7)
        def_gw = Label_entry_box('Default Gateway', 8)
        btn.grid(row=9, column=1, padx=10, pady=10)
    else:
        ip_prefix.label.destroy()
        ip_prefix.ebox.destroy()
        netmask.label.destroy()
        netmask.ebox.destroy()
        def_gw.label.destroy()
        def_gw.ebox.destroy()
        btn.grid(row=6, column=1, padx=10, pady=10)


def get_details():
    file_name = 'conf_gui.yaml'
    with open(file_name) as fp:
        file_load = YAML().load(fp)
    file_load['Group 1']['No_of_clients'] = int(no_of_clients.ebox.get())
    file_load['Group 1']['Connection'] = 'SSID-1'
    file_load['SSID-1']['SSID'] = ssid.ebox.get()
    if encrypt_type.get().lower() == 'open':
        file_load['SSID-1']['key_mgmt'] = 'none'
    else:
        file_load['SSID-1']['key_mgmt'] = 'WPA-PSK'
        file_load['SSID-1']['password'] = password.ebox.get()
    if ip_method.get().lower() == 'dhcp':
        file_load['Group 1']['Static_ip'] = 'no'
        file_load['Group 1']['dhcp_ip'] = 'yes'
    else:
        file_load['Group 1']['Static_ip'] = 'yes'
        file_load['Group 1']['ip_prefix'] = ip_prefix.ebox.get()
        file_load['Group 1']['netmask'] = netmask.ebox.get()
        file_load['Group 1']['default_gateway'] = def_gw.ebox.get()
        file_load['Group 1']['dhcp_ip'] = 'no'
    with open(file_name, 'w')as fp:
        YAML().dump(file_load, fp)
    window.destroy()


window = Tk()
window.config(bg='dim gray')
window.wm_geometry("500x450+300+150")
window.title("Virtual WiFi Clients")

Tk_var().labl('              ', 0)
no_of_clients = Label_entry_box('No of Clients  :  ', 1)
ssid = Label_entry_box('SSID  :  ', 2)
Tk_var().labl('WiFi Encryption  :  ', 3)
password = Label_entry_box('Password  :  ', 4)
Tk_var().labl('IP Method  :  ', 5)

encrypt_type = StringVar()
combo_encrypt = ttk.Combobox(window, width=8, textvariable=encrypt_type,
                             state='readonly', values=['WPA-PSK', 'OPEN'])
combo_encrypt.grid(row=3, column=1, padx=10, pady=10)
combo_encrypt.current(0)
combo_encrypt.bind("<<ComboboxSelected>>", cmd_encrypt)

ip_method = StringVar()
combo_ip_method = ttk.Combobox(window, width=8, textvariable=ip_method,
                               state='readonly', values=['DHCP', 'STATIC-IP'])
combo_ip_method.grid(row=5, column=1, padx=10, pady=10)
combo_ip_method.current(0)
combo_ip_method.bind("<<ComboboxSelected>>", cmd_ip_method)

btn = Button(window, text='Submit', bg='SkyBlue', command=get_details)
btn.grid(row=6, column=1, padx=10, pady=10)

window.mainloop()
