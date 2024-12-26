__author__ = 'Diego J D Arias - diegojdarias@gmail.com'

from peewee import SqliteDatabase
from peewee import Model
from peewee import CharField
from peewee import DateField
from tkinter import END
from observador import Sujeto
from tkinter import messagebox
import re
import datetime


db = SqliteDatabase("Base_Datos_Proveedores.db")


class BaseDeDatos(Model):
    class Meta:
        database = db


class Solicitud(BaseDeDatos):
    proveedor = CharField(unique=False)
    codigo = CharField()
    cant = CharField()
    descripcion = CharField()
    oci = CharField()
    fecha = DateField()


db.connect
db.create_tables([Solicitud])

# Decoradores por consolas, de las tres funciones, Alta, Baja, Modificacion.


def decorador_Alta(funcion):
    def datos(self, *args):
        print("Realizando las comprobaciones...")
        funcion(self, *args)
        print("comprobacion finalizada!")
    return datos


def decorador_Baja(funcion):
    def datos(self, *args):
        print("Realizando la consulta...")
        funcion(self, *args)
        print("Operacion finalizada!")
    return datos


def decorador_Modificacion(funcion):
    def datos(self, *args):
        print("Realizando las comprobaciones...")
        funcion(self, *args)
        print("comprobacion finalizada!")
    return datos


class Registro(Sujeto):
    def __init__(self):
        pass

    def limpiarReg(self, entrada1, entrada2, entrada3, entrada4,
                   entrada5, entrada6):
        entrada1.delete(0, END)
        entrada2.delete(0, END)
        entrada3.delete(0, END)
        entrada4.delete(0, END)
        entrada5.delete(0, END)
        entrada6.delete(0, END)

    @decorador_Alta
    def alta(self, proveedor, codigo, cant, descripcion, oci, fecha,
             mitreeview, entrada1, entrada2, entrada3, entrada4, entrada5,
             entrada6):

        cadena1 = fecha
        patron1 = "^(0?[1-9]|[12][0-9]|3[01])[\ /](0?[1-9]|1[012])[\ /]\d{4}$"  # noqa: W605, E501
        if re.match(patron1, cadena1):

            if (datetime.datetime.strptime(fecha, "%d/%m/%Y") > datetime.datetime.now()):  # noqa: E501
                messagebox.showerror(
                    title="Error",
                    message="La fecha de Alta es mayor a la actual")
                print("No se pudo realizar el Alta, La fecha sobrepasa la actual")  # noqa: E501
                return 0

            solicitud = Solicitud()
            solicitud.proveedor = proveedor
            solicitud.codigo = codigo
            solicitud.cant = cant
            solicitud.descripcion = descripcion
            solicitud.oci = oci
            solicitud.fecha = fecha
            solicitud.save()

            self.limpiarReg(entrada1, entrada2,
                            entrada3, entrada4,
                            entrada5, entrada6)

            messagebox.showinfo(
                title="Alta de Registro",
                message="Se realizo el Alta en el Registro!",
            )
            self.actualizarDatos(mitreeview)
            self.notificar(proveedor, codigo, cant, descripcion, oci, fecha)
            return mitreeview

        else:
            messagebox.showerror(
                title="Error!", message="Formato de fecha invalido. \nPor favor, ingrese la fecha en el formato dd/mm/yyyy")  # noqa: E501
            print("No se pudo realizar el Alta, Formato de fecha invalido.")

    @decorador_Baja
    def baja(self, mitreeview):
        self.btnop = messagebox.askokcancel(
            "Ejecutar", "Estas seguro que quieres borrar el registro?")
        if self.btnop is True:
            item_seleccionado = mitreeview.focus()
            valor_id = mitreeview.item(item_seleccionado)
            borrar = Solicitud.get(Solicitud.id == valor_id["text"])
            borrar.delete_instance()
            self.actualizarDatos(mitreeview)
            messagebox.showinfo("Programa", "Se realizo la baja en el registro")  # noqa: E501
            print("Se ha eliminado un registro")
        else:
            messagebox.showinfo("Programa", "Se cancelo la baja")
            print("Se cancelo la baja del Registro")
        return 0

    def registroSel(self, valor1, valor2, valor3,
                    valor4, valor5, valor6, tree):
        valor = tree.selection()
        registro = tree.item(valor)
        print(registro)
        valor1.set(registro["values"][0])
        valor2.set(registro["values"][1])
        valor3.set(registro["values"][2])
        valor4.set(registro["values"][3])
        valor5.set(registro["values"][4])
        valor6.set(registro["values"][5])

    @decorador_Modificacion
    def modificacion(self, proveedor, codigo, cant, descripcion, oci, fecha,
                     mitreeview, entrada1, entrada2, entrada3, entrada4,
                     entrada5, entrada6):
        cadena1 = fecha
        patron1 = "^(0?[1-9]|[12][0-9]|3[01])[\/](0?[1-9]|1[012])[\/]\d{4}$"  # noqa: W605, E501
        if re.match(patron1, cadena1):

            if (datetime.datetime.strptime(fecha, "%d/%m/%Y") > datetime.datetime.now()):  # noqa: E501
                messagebox.showerror(
                    title="Error",
                    message="La fecha de modificacion es mayor a la actual")
                print("No se pudo realizar las modificaciones, La fecha sobrepasa la actual")  # noqa: E501
                return 0

            item_seleccionado = mitreeview.focus()
            valor_id = mitreeview.item(item_seleccionado)
            actualizar = Solicitud.update(
                proveedor=proveedor,
                codigo=codigo,
                cant=cant,
                descripcion=descripcion,
                oci=oci,
                fecha=fecha,
            ).where(Solicitud.id == valor_id["text"])
            actualizar.execute()
            messagebox.showinfo(
                title="Modificacion de Registro",
                message="Registro modificado!",
            )
            self.actualizarDatos(mitreeview)
            print(
                "El Registro del Proveedor "
                + proveedor + ", " + " fue Modificado")

            self.limpiarReg(entrada1, entrada2, entrada3, entrada4,
                            entrada5, entrada6)
        else:
            messagebox.showerror(
                title="Error", message="Formato de fecha invalido. \nPor favor, ingrese la fecha en el formato dd/mm/yyyy")  # noqa: E501
            print("No se pudo realizar las modificaciones, Formato de fecha invalido.")  # noqa: E501

    def actualizarDatos(self, mitreeview):
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)

        for fila in Solicitud.select():
            mitreeview.insert("", 0, text=fila.id, values=(fila.proveedor,
                              fila.codigo, fila.cant, fila.descripcion,
                              fila.oci, fila.fecha))

    def consultaReg(self, mitreeview):
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        for fila in Solicitud.select():
            mitreeview.insert(
                "",
                0,
                text=fila.id,
                values=(fila.proveedor, fila.codigo, fila.cant,
                        fila.descripcion, fila.oci, fila.fecha),
            )
