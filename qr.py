import qrcode

qr = qrcode.QRCode(
    version=1,              # 1–40, controls size (1 = 21×21 modules)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # L / M / Q / H
    box_size=10,            # pixels per module
    border=4,               # quiet zone (min 4 recommended)
)

qr.add_data("https://www.youtube.com/watch?v=jGwO_UgTS7I&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU")
qr.make(fit=True)           # auto-upgrade version if data is too large

img = qr.make_image(fill_color="black", back_color="white")
img.save("best_machine_learing_course.png")