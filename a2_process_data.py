import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

fatality_before=0
fatality_after=0
for i in range (1,57):
	fatality_before += float (contents[i][4])
	fatality_after += float (contents[i][7])
	
fatality_before=fatality_before/56
fatality_after=fatality_after/56

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
    table td, table th {
    padding: 10px;
    }
    h1 {
    text-align: center;
    font-size: 18 px;
    margin: 2px ,2px, 1.5px, 1.5px;
    }
     </style>
</head>
<h1>Airline safety</h1>
<body>

<p id="source">Dataset supplied by <a href="https://github.com/fivethirtyeight/data/tree/master/airline-safety">
Airline data</a></p>
<p>The aim of this  assignment calculations was to emphasize the dercreasing number of fatalities by the technology improvement:</p>

<p>Average of fatalities 1985-1999 is: %02.f ; 
<p>Average of fatalities 2000-2014 is:  %0.2f ;
""" % (fatality_before,fatality_after))
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
def accidents():
    s="Airlines that have low number of accidents:"
    d=" Airlines that have high number of accidents:"
    for i in range(56):
        if int(contents[i+1][2])>0:
            s=s+", " + contents[i+1][1]
        else:
            d=d+", " + contents[i+1][1]
    return(s+d)
print("<table>")
for i in range(57):
    print("<tr>")
    for m in range(8):
        print("<td>" + contents[i][m] + "</td>")
    print("</tr>")
print("</table>")
print("""

</body>
</html>""")

