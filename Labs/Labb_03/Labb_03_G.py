import matplotlib.pyplot as plt
from functools import cache
import csv

@cache
def get_data():
    with open ("./Labs/Labb_03/unlabelled_data.csv","r") as f_read:
        data = [data.strip("\n").replace(","," ").split() for data in f_read.readlines()]
        data_array = [[float(item) for item in l] for l in data]
    return data_array


def points_classification(k,m, data=get_data()):         # function for point classification.
    points_class = []
    for l in data:
        l=l.copy()
        if l[1] > k*l[0]+m:
            l.append(1)
        else:
            l.append(0)
        points_class.append(l)
    return points_class

def x_and_y_class(points_class):
    points_class_0, points_class_1 = [], []                             # classification lists creates.
    for element in points_class:
        if element[2] == 0:
            points_class_0.append(element)
        else:
            points_class_1.append(element)
    return points_class_0, points_class_1


def save_data(points_class, points_class_0, points_class_1):
    with open ("./Labs/Labb_03/labelled_data.csv", "w", newline='') as f_write:
        f_write.write("============== Labeled data ==============\n")
        f_write.write(f"\nPoints with class 0 - {len(points_class_0)}.\n")
        f_write.write(f"Points with class 1 - {len(points_class_1)}.\n\n")
        rows =  points_class
        write = csv.writer(f_write)
        write.writerows(rows)

def main():
    k = -1.5
    m = 0.2
    x = list(range(-4,5))   
    y = [k*x+m for x in x]
    p_class = points_classification(k,m)
    p_class_0, p_class_1 = x_and_y_class(p_class)
    save_data(p_class, p_class_0, p_class_1)
    x_class_0 = [element[0] for element in p_class_0]
    y_class_0 = [element[1] for element in p_class_0]
    x_class_1 = [element[0] for element in p_class_1]
    y_class_1 = [element[1] for element in p_class_1]
    print(f'''\n============== Labeled data ==============\n
        Points with class 0 - {len(p_class_0)}.\n
        Points with class 1 - {len(p_class_1)}.\n\n''')
    plt.plot(x,y, 'r')
    plt.scatter(x_class_0, y_class_0)
    plt.scatter(x_class_1, y_class_1)
    plt.title("Linear classification.")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(["y=-1.5x+0.2", "Label - 0", "Label - 1"], loc=4)
    plt.show()

if __name__=="__main__":
    main()