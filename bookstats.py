import tools
f = open("Gutenberg_Flatland_Ettubrute.txt","r")
content = f.read()
f.close()
tools.letterfreq(content)

