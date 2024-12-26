__author__ = 'Diego J D Arias - diegojdarias@gmail.com'

from tkinter import Tk
import vista
import observador


class Controler:
    def __init__(self, root) -> None:
        self.root = root
        self.objeto_vista = vista.Principal(self.root)
        self.el_observador = observador.ObservadorConcretoA(
            self.objeto_vista.objeto
            )


if __name__ == '__main__':
    root = Tk()
    root.wm_title('Productos - Reverse Engineering by Diego J D Arias')
    root.wm_iconbitmap("icono/1DA.ico")
    Aplicacion = Controler(root)
    root.mainloop()
