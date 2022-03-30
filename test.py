import screeninfo as si

screens = []
for m in si.get_monitors():
    size = [m.is_primary, m.height, m.width]
    screens.append(size)

print(screens)