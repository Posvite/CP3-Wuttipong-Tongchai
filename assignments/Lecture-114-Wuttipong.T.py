from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyCodes


def trace_entry(var,idt,mode):
    test_string_trace = 0.0
    try:
        test_string_trace = isinstance(int(entry_trace.get()), int)
    except:
        label_convert.set("ใส่ข้อมูลผิด")
        entry_trace.set('')
    if test_string_trace == True:
        label_convert.set(c.convert(combo_currency1.get(),combo_currency2.get(),int(entry_trace.get())))
        label_convert_info = c_symbol.get_currency_name(combo_currency1.get()) + ' ' + c_symbol.get_symbol(combo_currency1.get()) + " >" + c_symbol.get_currency_name(combo_currency2.get()) + ' ' + c_symbol.get_symbol(combo_currency2.get())
        label_currency_info.set(label_convert_info)

#GUI
c = CurrencyRates()
c_symbol = CurrencyCodes()
main_window = tk.Tk()
main_window.configure(bg='#f2f2f2')
main_window.title("Convert money")
main_window.geometry("700x100")

#get list
list_curency = []
for i in c.get_rates("USD"):
    list_curency += [i]


#Label

label_currency1 = ttk.Label(main_window,
                            text='ค่าเงินหลัก ')
label_currency1.grid(row=0, column=0, padx=30)

label_currency2 = ttk.Label(main_window,
                            text='ค่าเงินที่ต้องการแลกเปลี่ยน')
label_currency2.grid(row=1, column=0, padx=30)
label_convert = tk.StringVar()
label_convert.set("อัตราการแลกเปลี่ยนค่าเงิน")
label_currency3 = ttk.Label(main_window,
                            text="อัตราการแลกเปลี่ยนค่าเงิน",
                            textvariable=label_convert)
label_currency3.grid(row=1, column=1, padx=30)
label_currency4 = ttk.Label(main_window,
                            text="ข้อมูลการแลกเปลี่ยนค่าเงิน")
label_currency4.grid(row=3,column=0)
label_currency_info = tk.StringVar()
label_currency_info.set("ข้อมูลการแปลงค่าเงิน")
label_currency5 = ttk.Label(main_window,
                            textvariable=label_currency_info)
label_currency5.grid(row=3,column=1,padx=30)

#Entry
entry_trace = tk.StringVar()
entry_trace.trace_add('write', trace_entry)
entry_currency1 = ttk.Entry(main_window,
                            width=20,
                            textvariable = entry_trace)
entry_currency1.grid(row=0, column=1)

#combo
combo_currency1 = ttk.Combobox(main_window,
                              values=list_curency,
                              state="readonly")
combo_currency1.grid( row=0, column=2)
combo_currency1.current(10)

combo_currency2 = ttk.Combobox(main_window,
                              values=list_curency,
                              state="readonly")
combo_currency2.grid(row=1, column=2)
combo_currency2.current(29)



main_window.mainloop()