


# import qrcode

# def escape_wifi_str(text: str) -> str:
#     """Escapa caracteres especiales requeridos por el formato Wi-Fi QR."""
#     for char in [r"\\", ";", ":", ","]:
#         text = text.replace(char, f"\\{char}")
#     return text

# ssid = input("Nombre de la red Wi-Fi (SSID): ")
# password = input("Contraseña (deja en blanco si es una red abierta): ")
# is_hidden = input("¿Es una red oculta? (s/n): ").strip().lower() == 's'

# ssid_esc = escape_wifi_str(ssid)
# password_esc = escape_wifi_str(password)

# hidden_flag = "H:true;" if is_hidden else ""

# if not password:
#     wifi_string = f"WIFI:T:nopass;S:{ssid_esc};{hidden_flag};"
# else:
#     wifi_string = f"WIFI:T:WPA;S:{ssid_esc};P:{password_esc};{hidden_flag};"

# img = qrcode.make(wifi_string)
# img.save("wifi_qr.png")

# print("Código QR generado exitosamente como 'wifi_qr.png'.")



