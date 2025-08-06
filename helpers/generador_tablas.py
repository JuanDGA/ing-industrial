"""
Se asume que lee un archivo donde cada linea es un item de una fila.
Una vez se leen 4 items se imprime el TR y se reinicia la construcción de una nueva fila.
"""

info = open("table.txt", "r").read().strip().split("\n")
info = list(filter(lambda x: len(x.strip()) > 0, info))

table = []

current_idx = 0
current_piece = ["" for _ in range(4)]

for piece in info:
    part = current_idx % 4
    current_piece[part] = piece.strip()
    if part == 3:
        table.append(current_piece)
        current_piece = ["" for _ in range(4)]
    current_idx += 1


for apellido, nombre, correo, clase in table:
    correos = [c.strip() for c in correo.split(";")]
    clases = [c.strip() for c in clase.split(",")]

    correo_html = "\n".join(
        f'<p class="rtecenter"><span style="color:#696969;"><span style="font-family:times new roman,times,serif;"><u>{c}</u></span></span></p>'
        for c in correos
    )

    clase_html = "\n".join(
        f'<p><span style="color:#696969;"><span style="font-family:times new roman,times,serif;">{c}</span></span></p>'
        for c in clases
    )

    tr = f"""
        <tr>
			<td nowrap="nowrap" style="width: 211px;">
			<p class="rtecenter"><span style="color:#696969;"><span style="font-family:times new roman,times,serif;">{apellido}</span></span></p>
			</td>
			<td nowrap="nowrap" style="width: 231px;">
			<p class="rtecenter"><span style="color:#696969;"><span style="font-family:times new roman,times,serif;">{nombre}</span></span></p>
			</td>
			<td nowrap="nowrap" style="width: 140px;">
			{correo_html}
			</td>
			<td nowrap="nowrap">
			{clase_html}
			</td>
		</tr>
    """
    print(tr.strip())