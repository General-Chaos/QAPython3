import showcard

number = input("Pick a card (1-52):")

filename = "BMP"+number+".GIF"

showcard.set_timeout(10)
showcard.display_file(filename)
