gruppi = [{'id': 1, 'name': 'uno', 'keyword': ['01', '02', '03']}, {'id': 2, 'name': 'due', 'keyword': ['01', '02', '03']}]



count = 0
header = ""
line = ""
column = ""
modulo = len(gruppi)


for i in gruppi:
	if count == 0:
		header = "| " + i["name"] + " | "
		line = "|:--"
	else:
		header += i["name"] + " |"
		line += "|:--|"
	count+= 1




# linecount = 0
# for i in gruppi:
# 	print(i["name"])
# 	for x in i["keyword"]:
# 		column +
# 		print(x)
# 		linecount+=1


comp = (header+"\n"+ line + "\n" + column)
print (modulo)
# print( "|" + i["name"] + "|")
# 	for x in i["keyword"]:
# 		print(x)

# filemarkdown+="""
# <li class="lista">
# 		<img src="{urlimage}">
# 		<span class="title">
# 			<a href="{link}">Link - ({name})</a>
# 		</span>
# </li>
# """.format(urlimage=(curpath+e) , link=(vectorpath+e[:-3]+'ai'), name=(e)  )