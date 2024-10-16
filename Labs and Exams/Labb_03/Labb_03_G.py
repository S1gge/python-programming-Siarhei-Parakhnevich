import matplotlib.pyplot as plt

# Creates functions.
def convert_to_float (input_list):          # function for convert to float.
    output_list_float = []
    for element in input_list:
        sublist = []
        for string in element:
            converted_float = float(string)
            sublist.append(converted_float)
        output_list_float.append(sublist)
    return output_list_float

def points_classification(k,m, points):         # function for point classification.
    points_class = []
    for l in points:
        l=l.copy()
        if l[1] > k*l[0]+m:
            l.append(1)
        else:
            l.append(0)
        points_class.append(l)
    return points_class

# Cleans data in unlabeled_data file.
with open ("./Labs and Exams/Labb_03/unlabelled_data.csv","r") as f_read:

    data_list_step_01 = [data.strip("\n").replace(","," ") for data in f_read.readlines()]
    data_list_step_02 = [data.split() for data in data_list_step_01]

# Data converts from String to Float.
data_list_float = convert_to_float(data_list_step_02)           # function for convert to float calls.  

# Creates lists for x and y. 
x_list = [data[0] for data in data_list_float]
y_list = [data[1] for data in data_list_float]

# Creates linear function.
x = list(range(-4,5))
k = -1.5
m = 0.2
y = [k*x+m for x in x]

# Points classification.
points_class = points_classification(k,m, data_list_float)          # function for points classification calls.

points_class_0, points_class_1 = [], []                             # classification lists creates.
for element in points_class:
    if element[2] == 0:
        points_class_0.append(element)
    else:
        points_class_1.append(element)

x_point_class_0 = [element[0] for element in points_class_0]
y_point_class_0 = [element[1] for element in points_class_0]
x_point_class_1 = [element[0] for element in points_class_1]
y_point_class_1 = [element[1] for element in points_class_1]

#Output information.
print(f'''\n===============Labeled data===============\n
      Points with class 0 - {len(points_class_0)}.\n
      Points with class 1 - {len(points_class_1)}.\n\n''')

# Plotts classificated data and linear function.
plt.plot(x,y, 'r')
plt.scatter(x_point_class_0, y_point_class_0)
plt.scatter(x_point_class_1, y_point_class_1)
plt.title("Linear classification.")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["y=-1.5x+0.2", "Label - 0", "Label - 1"], loc=4)
plt.show()

# Creates file labeled_data.csv with classificated data.
with open ("./Labs and Exams/Labb_03/labelled_data.csv", "w") as f_write:
    f_write.write("===============Labeled data===============\n")
    f_write.write(f"\nPoints with class 0 - {len(points_class_0)}.\n")
    f_write.write(f"Points with class 1 - {len(points_class_1)}.\n\n")
    for element in points_class:
        f_write.write(f"{element}\n")