from PIL import Image, ImageDraw

frames = []

# Création de 5 frames avec variations d'opacité
for i in range(5):
    img = Image.new("RGB", (240, 220), "black")
    draw = ImageDraw.Draw(img)
    opacity = int(255 * (0.8 + 0.05*i))
    color = (246, 212, 0, opacity)  # jaune
    # Triforce simplifiée
    draw.polygon([(120,30),(80,90),(160,90)], fill=color)
    draw.polygon([(80,130),(40,190),(120,190)], fill=color)
    draw.polygon([(160,130),(120,190),(200,190)], fill=color)
    frames.append(img)

frames[0].save("triforce.gif", save_all=True, append_images=frames[1:], duration=150, loop=0)
