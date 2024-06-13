import  matplotlib.pyplot as plt

# Data
x=[1,2,3,4,5]
y=[2,3,5,7,11]

# Creating a line plot
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls="-")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

# Creating a dotted plot
plt.plot(x,y,linestyle="dotted")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls=":")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

# Creating a dashed plot
plt.plot(x,y,linestyle="dashed")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls="--")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

# Creating a dashed dotted plot
plt.plot(x,y,ls="-.",color='r',linewidth="10")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls="-.",color='r',lw="3",marker="o")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls="-.",color='r',lw="3",marker="*")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls="-.",color='r',lw="3",marker="x")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls="-.",color='r',lw="3",marker="+")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls="-.",color='r',lw="3",marker="s",mec='r')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

plt.plot(x,y,ls="-.",color='r',lw="3",marker="s",mfc='r',ms="10")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

### Using Numpy
import numpy as np
y1=np.array([3,8,1,10])
y2=np.array([6,2,7,11])
plt.plot(y1)
plt.plot(y2)
plt.show()


# Creating a simple scatter plot
# Data
x=[1,2,3,4,5]
y=[2,3,5,7,11]

# Creating a scatter plot
plt.scatter(x,y,color="r")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Simple Scatter Plot")
plt.show()

# Creating a simple bar plot with matplotlib

# Data
categories=['PC','TV','REF','MICRO']
sales=[4,7,1,8]

# Creating a bar plot
plt.bar(categories, sales,color="violet",width=0.1)
plt.xlabel('Products')
plt.ylabel('Sales(in 1000s)')
plt.title('Simple Bar Plot')
plt.show()


# Creating a horizontal bar plot
plt.barh(categories, sales,color="violet",height=0.1)
plt.xlabel('Products')
plt.ylabel('Sales(in 1000s)')
plt.title('Simple Bar Plot')
plt.show()


# Creating a Simple histogram

# Data
data=[1,2,2,3,3,3,4,4,4,4]
# creating a histogram
plt.hist(data,bins=4)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Simple Histogram')
plt.show()


# Creating a SubPlot

# Data
x=[1,2,3,4,5]
y1=[2,3,5,7,11]
y2=[1,4,6,8,10]
# Creating subplots
fig, axs=plt.subplots(2)
axs[0].plot(x,y1)
axs[0].set_title('First Plot')
axs[1].plot(x,y2,'tab:Orange')
axs[1].set_title('Second Plot')

# Displaying the plot
plt.tight_layout()
plt.show()


# Adding annotations with matplotlib

# Data
x=[1,2,3,4,5]
y=[2,3,5,7,11]

# Creating a plot with annotations
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot With Annotations')
plt.annotate('Peak',xy=(5,11),xytext=(4,10),
             arrowprops=dict(facecolor='black',shrink=0.05))
plt.show()



# Creating a Simple line plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Data
x=[1,2,3,4,5]
y=[2,3,5,7,11]

# Creating a line plot
sns.lineplot(x=x,y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot with Seaborn')
plt.show()


# Creating a simple scatter plot with seaborn

# Data
x=[1,2,3,4,5]
y=[2,3,5,7,11]

# Creating a Scatter plot
sns.scatterplot(x=x,y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot with Seaborn')
plt.show()


# Creating a simple bar plot with seaborn

# Data
categories=['A','B','C','D']
sales=[4,7,1,8]

# Creating a bar plot
sns.barplot(x=categories,y=sales)
plt.xlabel('categories')
plt.ylabel('sales')
plt.title('Simple Bar Plot with Seaborn')
plt.show()


# Creating  a Simple Hitogram with seaborn
data=[1,2,2,3,3,3,4,4,4,4]

# Creating a Histogram
sns.histplot(data,bins=4)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Simple Histogram with Seaborn')
plt.show()


# Creating a Pair plot with seaborn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris=load_iris()
iris_data=sns.load_dataset("iris")

# Creating a pair plot
sns.pairplot(iris_data,hue='species')
plt.title('pair plot with seaborn')
plt.show()


# Creating a Heat Map with seaborn
import numpy as np

# Data
data=np.random.rand(10,12)
sns.heatmap(data)
plt.title('HeatMap with Seaborn')
plt.show()