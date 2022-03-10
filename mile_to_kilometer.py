from tkinter import *
def mile_to_km():
    miles = float(m_input.get())
    km = miles * 1.6099
    km_result_label.config(text=f"{km}")
window = Tk()

window.title("Miles to kilometer")
window.config(padx=20, pady=20)

m_input = Entry(width=7)
m_input.grid(column= 1, row= 0)
m_label = Label(text="Miles")
m_label.grid(column= 2, row= 0)
equal_label = Label(text="is equal to")
equal_label.grid(column= 0 , row= 1)
km_result_label = Label(text= "0")
km_result_label.grid(column= 1, row= 1)
km_label = Label(text="Km")
km_label.grid(column= 2, row= 1)
cal_button = Button(text="Calculate", command=mile_to_km)
cal_button.grid(column= 1, row= 2)
window.mainloop()