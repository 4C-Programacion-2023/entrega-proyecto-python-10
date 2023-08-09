import tkinter as tk

app = tk.Tk()
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)
app.geometry("300x600")
app.configure(background="white")
tk.Wm.wm_title(app, "hola")
tk.Button(
    app,
    text= "Actuales",
    font= ("Courier", 14),
    bg= "#D3D88C",
    fg= "#000000",
    relief="flat",
    command=lambda: print("hola  " + entrada.get()) ,
).pack(
    fill= tk.BOTH,
    expand=True
)
tk.Button(
    app,
    text= "retro",
    font= ("Courier", 14),
    bg= "#D3D88C",
    fg= "#000000",
    relief="flat",
    command=lambda: print("chau  " + entrada.get()) ,
).pack(
    fill= tk.BOTH,
    expand=True
)
tk.Label(
    app,
    text= "etiqueta",
    font= ("Courier", 14),
    bg= "#000000",
    fg= "#D3D88C",
    justify= "center"

).pack(
    fill= tk.BOTH,
    expand=True
)
tk.Entry(
 app,
    font= ("Courier", 14),
    bg= "#000000",
    fg= "#D3D88C",
    justify= "center",
    textvariable= entrada

).pack(
    fill= tk.BOTH,
    expand=True
)
app.mainloop()