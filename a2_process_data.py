import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]
print("""<!DOCTYPE html> 
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\" />
    <title>Airline safety data</title>
    <style>
    table,td {
    border: 2px solid black;
    border-collapse: collapse;
    }
    </style>
</head>
<body>""")

#print("This assignment (assignment 2) hasn't been finished.")
#print("All it can do is print out the contents of a couple of cells of the file a2_input.csv:")
#print("Cell at index 0,0:")
#print(contents[0][0])
#print("Cell at index 0,1:")
#print(contents[0][1])
#print("Cell at index 1,0:")
#print(contents[1][0])
#print(contents)
#print(contents[0])
#print(contents[0][0])
#print(type(contents))
#print(type(contents[0]))
#print(type(contents[0][0]))
#print(contents[3][3])
#print(contents[23][2])
#av_seat = 0.0
#for i in range(1, 57):
#	av_seat += float(contents[i][1])
#av_seat = av_seat / 56
#print(av_seat)
#dan_airlines=0
#for i in range(1,57):
#	if int(contents[i][2])>=12:
#		dan_airlines += 1
#print(dan_airlines)
#str1 = contents[0][3]+contents[3][1]
#str2 = 2*contents[0][3] 
#print(str1)
#print(str2)
#print(type(str1),type(str2))
print("<table>")
for i in range(57):
    print("<tr>")
    for m in range(8):
        print("<td>" + contents[i][m] + "</td>")
    print("</tr>")
print("</table>")
print("""</body>
</html>""")

