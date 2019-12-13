gruppi = [{'id': 1, 'name': 'uno', 'keyword': ['01', '02', '03']}, {'id': 2, 'name': 'due', 'keyword': ['01', '02', '03']}]



count = 0
header = ""
for i in gruppi:
	if count == 0:
		header = "| " + i["name"] + " | "
	else:
		header += i["name"] + " |"
	count+= 1

print(header)

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