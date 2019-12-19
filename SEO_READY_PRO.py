import numpy as np

gruppi = [
	{'id': 1, 'name': 'uno', 'keyword': ['01', '02', '03','05','06','07']},
	{'id': 2, 'name': 'due', 'keyword': ['01', '02', '03']},
	{'id': 2, 'name': 'tre', 'keyword': ['01', '02', '03','04']},
	{'id': 2, 'name': 'quattro', 'keyword': ['01', '02', '03']},
]

biggroup = 0


for i in gruppi:
	if len(i["keyword"]) > biggroup:
		biggroup = len(i["keyword"])
	

a = np.zeros((biggroup,len(gruppi)))

a[0][1].add("ciao")

for i in a:
	print(str(i)+"cc")
	for x in i:
		print(str(x)+"sss")


print(a)
count = 0
header = ""
line = ""
column = ""
modulo = len(gruppi)


for i in gruppi:
	mod = count % 2
	colline = ''

	# if(mod==0):
	# 	colline = "| " +  
	# 	print("pari" + str(mod))
	# else:

	if count == 0:
		header = "| " + i["name"] + " | "
		line = "|:--"
	else:
		header += i["name"] + " |"
		line += "|:--|"
	count+= 1

print(header)




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