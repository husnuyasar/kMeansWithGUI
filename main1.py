from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import random
from tkinter import *
from var_dump import var_dump

#x = np.array([3, 1, 1,4,3, 2, 1, 6, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8,11,3])
#y = np.array([5, 4, 6,6,3, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3,5,11])

root = Tk()
root.geometry('500x500')
root.title("K Means Fillable Form")

label_0 = Label(root, text="K Means Fillable Form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_small = Label(root, text="** Please use comma ',' in Array Fields", fg="red", width=35, font=("bold", 8))
label_small.place(x=150, y=93)

label_1 = Label(root, text="First Array", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)
v1 = StringVar()
warning_1 = Label(root, textvariable=v1, fg="red", width=35, font=("bold", 8))
warning_1.place(x=190, y=150)

label_2 = Label(root, text="Second Array", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root)
entry_2.place(x=240, y=180)
v2 = StringVar()
warning_2 = Label(root, textvariable=v2, fg="red", width=35, font=("bold", 8))
warning_2.place(x=190, y=200)

label_3 = Label(root, text="K Value", width=20, font=("bold", 10))
label_3.place(x=68, y=230)

entry_3 = Entry(root)
entry_3.place(x=240, y=230)
v3 = StringVar()
warning_3 = Label(root, textvariable=v3, fg="red", width=35, font=("bold", 8))
warning_3.place(x=190, y=250)

def classificate(text):
    if not entry_1.get() or not entry_2.get() or not entry_3.get():
        if not entry_1.get():
            v1.set("You must fill out the first array")
        if not entry_2.get():
            v2.set("You must fill out the second array")
        if not entry_3.get():
            v3.set("You must fill out the k value")

        return
    v1.set("")
    v2.set("")
    v3.set("")
    x = entry_1.get()
    x = (x.split(","))
    y = entry_2.get()
    y = (y.split(","))
    for i in range(len(x)):
        x[i] = int(x[i])
    for i in range(len(y)):
        y[i] = int(y[i])
    K = (entry_3.get())
    K = int(K)
    if (len(x) != len(y)):
        v2.set("Lengths of arrays must be equal")
        return

    if (len(x) == len(y)):
        lx = max(x)+1
        ly = max(y)+1
        plt.plot()
        plt.xlim([0, lx])
        plt.ylim([0, ly])
        plt.title('My Kmeans Table')
        plt.scatter(x, y)
        plt.show()

        plt.plot()

        X = np.array(list(zip(x, y))).reshape(len(x), 2)
        markers = 'o'

        colors = []
        # KMeans algorithm
        kmeans_model = KMeans(n_clusters=K).fit(X)
        # Random color generater
        for i in range(K):
            r = lambda: random.randint(0, 255)
            colors.append('#%02X%02X%02X' % (r(), r(), r()))

        plt.plot()
        # Plot classificate arrays
        for i, a in enumerate(kmeans_model.labels_):
            plt.plot(x[i], y[i], color=colors[a], marker=markers, ls='None')
            plt.xlim([0, lx])
            plt.ylim([0, ly])

        plt.show()
        return


Button(root, text='Calculate & Plot', width=20, bg='blue', fg='white', command=lambda: classificate(entry_1.get())).place(x=180,
                                                                                                             y=380)

root.mainloop()
