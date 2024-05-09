from tkinter import Tk, Toplevel, Button, Listbox 


class okno_whod(Tk):

 def __init__(self):
  Tk.__init__(self)
  self.title("Окно входа")
  self.geometry('700x300') 
  self.resizable(False,False)

#кнопка посетитель
  self.button = Button(self,text="посетитель", command=lambda: User()).grid(row=2,column=1,padx=5, pady=5)
  
#кнопка администратор
  self.button = Button(self,text="администратор", command=lambda: Admin()).grid(row=2,column=2,padx=5, pady=5)
  
# заказать
  self.button = Button(self,text="Заказать", command=lambda: order()).grid(row=2,column=3,padx=5, pady=5)
  

class Admin(Toplevel):
 def __init__(self,):
  Toplevel.__init__(self)
  self.title("Admin")
  self.geometry("900x450")
  self.resizable(False, False)
  





  # Кнопка добавить 
  self.btn_add = Button(self, text='add Users', command=lambda:Admin ()).grid(row=2, column=1, padx=5, pady=5)
  
  # Кнопка для удаление пользователя
  self.btn_add = Button(self, text='Delit User', command=lambda: Admin()).grid(row=2,column=2,padx=5, pady=5)
  

  # Кнопка для редактирования посетителя
  self.btn_add = Button(self, text='to change Users', command=lambda: Admin()).grid(row=2,column=3,padx=5, pady=5)
  
 
  self.lbox = Listbox(self, width=50,height=80).grid(row=3,column=4,padx=10,pady=10)
  

 
if __name__ == '__main__':
  app = okno_whod()
  app.mainloop()
 
 
