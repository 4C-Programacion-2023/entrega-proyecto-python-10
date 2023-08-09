import sqlite3

conexion=sqlite3.connect("Usuarios.db")
cursorBD=conexion.cursor()

def tablaexiste(nombreTabla):
    cursorBD.execute(""" SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = "table" AND name ="{}" """,format(nombreTabla))
    if cursorBD.fetchone()[0]==1:
        return True
    else:
        cursorBD.execute(""" CREATE TABLE USUARIOS (NOMBRE TEXT,CONTRASEÑA TEXT) """)
    return False

tablaexiste("USUARIOS")

#VER COMO INSERTARLE DATOS
