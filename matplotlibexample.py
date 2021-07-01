import matplotlib.pyplot as plt
import numpy as np

x=np.arange(10)
print(x)

y1=x**2
print(y1)

y2=3*x+5
print(y2)

themes=plt.style.available
print(themes)



#line plot
plt.style.use("dark_background")
plt.plot(x,y1,color="red", label="Apple", linestyle="dashed", marker="*")
plt.plot(x,y2,color="yellow", label="Melon", marker="o")
plt.xlabel("Time")
plt.ylabel("price")
plt.title("Fruits prices over time")
plt.legend()
plt.show()

#Scatter plot
plt.style.use("bmh")
plt.figure(figsize=(6,6))
plt.scatter(x,y1,color="red", label="Apple", marker="*")
plt.scatter(x,y2,color="yellow", label="Melon", marker="o")
plt.xlabel("Time")
plt.ylabel("price")
plt.title("Scatter plot- prices over time")
plt.legend()
plt.show()

# Bar Graph
plt.style.use("seaborn")
x_coordinates=np.array([0,1,2])*2
plt.bar(x_coordinates-0.25,[10,20,30],width=0.5,color="blue",tick_label=["Metal","Silver","Gold"],label="year:2020")
plt.bar(x_coordinates+0.25,[15,25,35],width=0.5,color="green",label="year:2021")
plt.xlabel("Metals")
plt.ylabel("price")
plt.title("Metal prices of current and next year")
plt.legend()
plt.show()

# Pie chart
plt.style.use("bmh")
plt.figure(figsize=(10,10))
titles = ["Maths", "English", "Hindi", "Science", "Computer"]
weightages=[20,20,10,20,10]
plt.pie(weightages, labels=titles, explode=(0.1,0,0,0,0), shadow=True,autopct="%1.1f%%")
plt.title="Subjects chart"
plt.show()

