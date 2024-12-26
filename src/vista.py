__author__ = 'Diego J D Arias - diegojdarias@gmail.com'

from tkinter import Frame, Label
from tkinter import ttk
from tkinter import Entry
from tkinter import StringVar
import modelo


class Principal(Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master, width=1082, height=402)
        self.master = master
        self.master.resizable(0, 0)
        self.pack()
        self.widget()
        self.objeto = modelo.Registro()

    def widget(self):
        self.area1 = Frame(self, bg='#ffffe0')
        self.area1.place(x=0, y=0, width=880, height=300)

        self.area2 = Frame(self, bg='#7f11e0')
        self.area2.place(x=0, y=300, width=880, height=100)

        self.area3 = Frame(self, bg='#7f11e0')
        self.area3.place(x=880, y=0, width=200, height=400)

        (
            self.valor1, self.valor2, self.valor3, self.valor4,
            self.valor5, self.valor6,
        ) = (
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
            StringVar(),
        )

        self.data_pro = ttk.Treeview(self.area1)
        self.data_pro["columns"] = ("col1", "col2", "col3", "col4", "col5",
                                    "col6")
        self.data_pro.column("#0", width=40, minwidth=20, anchor="w")
        self.data_pro.column("col1", width=150, minwidth=50)
        self.data_pro.column("col2", width=90, minwidth=80)
        self.data_pro.column("col3", width=40, minwidth=10)
        self.data_pro.column("col4", width=340, minwidth=80)
        self.data_pro.column("col5", width=120, minwidth=80)
        self.data_pro.column("col6", width=100, minwidth=80)
        self.data_pro.heading("#0", text="ID")
        self.data_pro.heading("col1", text="Proveedor")
        self.data_pro.heading("col2", text="Codigo")
        self.data_pro.heading("col3", text="Cant.")
        self.data_pro.heading("col4", text="Descripción")
        self.data_pro.heading("col5", text="OCI/RTO/INV/PACK")
        self.data_pro.heading("col6", text="Fecha")
        self.scroll_y = ttk.Scrollbar(self.area1, orient="vertical",
                                      command=self.data_pro.yview)
        self.data_pro.configure(yscrollcommand=self.scroll_y.set)
        # Posicionamos Treeview y scrollbar en grid
        self.data_pro.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        # Configuración de expansión de filas y columnas
        self.area1.rowconfigure(0, weight=1)
        self.area1.columnconfigure(0, weight=1)
        self.data_pro.grid(row=0, column=0, columnspan=6)

        self.btn1 = ttk.Button(self.area2, text='Alta',
                               command=lambda: self.objeto.alta(
                                    self.valor1.get(), self.valor2.get(),
                                    self.valor3.get(), self.valor4.get(),
                                    self.valor5.get(), self.valor6.get(),
                                    self.data_pro, self.entrada1,
                                    self.entrada2, self.entrada3,
                                    self.entrada4, self.entrada5,
                                    self.entrada6))
        self.btn1.grid(row=1, column=1, padx=40, pady=30)
        self.btn2 = ttk.Button(self.area2, text='Modificar',
                               command=lambda: self.objeto.modificacion(
                                    self.valor1.get(), self.valor2.get(),
                                    self.valor3.get(), self.valor4.get(),
                                    self.valor5.get(), self.valor6.get(),
                                    self.data_pro, self.entrada1,
                                    self.entrada2, self.entrada3,
                                    self.entrada4, self.entrada5,
                                    self.entrada6))
        self.btn2.grid(row=1, column=3, padx=40, pady=30)
        self.btn3 = ttk.Button(self.area2, text='Baja',
                               command=lambda: self.objeto.baja(self.data_pro))
        self.btn3.grid(row=1, column=5, padx=40, pady=30)
        self.btn4 = ttk.Button(self.area2, text='Consulta',
                               command=lambda:
                               self.objeto.consultaReg(self.data_pro))
        self.btn4.grid(row=1, column=7, padx=40, pady=30)
        self.btn5 = ttk.Button(self.area2, text='Seleccionar',
                               command=lambda: self.objeto.registroSel(
                                   self.valor1, self.valor2,
                                   self.valor3, self.valor4, self.valor5,
                                   self.valor6, self.data_pro))
        self.btn5.grid(row=1, column=9, padx=40, pady=30)

        self.lb1 = Label(self.area3, text='Nombre Proveedor', bg='#7f11e0',
                         font=("Lucida Console", 10)
                         ).place(relx=0.25, y=5)
        self.entrada1 = Entry(self.area3,
                              textvariable=self.valor1)
        self.entrada1.place(relx=0.25, y=35)
        self.lb2 = Label(self.area3, text='Codigo', bg='#7f11e0',
                         font=("Lucida Console", 10)
                         ).place(relx=0.25, y=65)
        self.entrada2 = Entry(self.area3,
                              textvariable=self.valor2)
        self.entrada2.place(relx=0.25, y=95)
        self.lb3 = Label(self.area3, text='Cant.', bg='#7f11e0',
                         font=("Lucida Console", 10)
                         ).place(relx=0.25, y=125)
        self.entrada3 = Entry(self.area3,
                              textvariable=self.valor3)
        self.entrada3.place(relx=0.25, y=155)
        self.lb4 = Label(self.area3, text='Descripcion', bg='#7f11e0',
                         font=("Lucida Console", 10)
                         ).place(relx=0.25, y=185)
        self.entrada4 = Entry(self.area3,
                              textvariable=self.valor4)
        self.entrada4.place(relx=0.25, y=215)
        self.lb5 = Label(self.area3, text='OCI/RTO/INV/PACK', bg='#7f11e0',
                         font=("Lucida Console", 10)
                         ).place(relx=0.25, y=245)
        self.entrada5 = Entry(self.area3,
                              textvariable=self.valor5)
        self.entrada5.place(relx=0.25, y=275)
        self.lb6 = Label(self.area3, text='Fecha', bg='#7f11e0',
                         font=("Lucida Console", 10)
                         ).place(relx=0.25, y=305)
        self.entrada6 = Entry(self.area3,
                              textvariable=self.valor6)
        self.entrada6.place(relx=0.25, y=335)
