#Don Baker
#Comp-Sci 5590
#Lab 3, Question 2 (RBF Kernel)

#Implement Support Vector Machine classification,
#1)	Choose one of the dataset using the datasets features in the scikit-learn
#2)	Load the dataset
#3)	According to your dataset, split the data to 20% testing data, 80% training data(you can also use any other number)
#4)	Apply SVC with Linear kernel
#5)	Apply SVC with RBF kernel
#6)	Report the accuracy of the model on both models separately and report their differences if there is
#7)	Report your view how can you increase the accuracy and which kernel is the best for your dataset and why


#Guidance and example code taken from Learn&Teach YouTube videos at https://www.youtube.com/channel/UCGD8R7ct8cQfMMuUFImqDdQ

#Import Packages/Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Import Data
dataset=pd.read_csv('d:/Social_Network_Ads.csv')
X=dataset.iloc[:, [2,3]].values
y=dataset.iloc[:, 4].values

#Split the data into training and testing data sets for cross-validation
from sklearn import model_selection as cv
splits=cv.train_test_split(X,y,test_size=0.20)
X_train,X_test,y_train,y_test=splits

#Scale the data to provide more accurate evalaution
from sklearn.preprocessing import StandardScaler
Scale_X=StandardScaler()
X_train=Scale_X.fit_transform(X_train)
X_test=Scale_X.transform(X_test)

#Complete SVM using SVC - RBF Kernel

from sklearn.svm import SVC
SVC_classifier=SVC(kernel='rbf', random_state=0)
SVC_classifier.fit(X_train,y_train)

#Predict the results of the model using the test set of data
y_pred_weather=SVC_classifier.predict(X_test)

#Create and display the confusion matrix for the analysis
from sklearn.metrics import confusion_matrix
confusion_SVC=confusion_matrix(y_test,y_pred_weather)
print("The confusion matrix for the SVM analysis is:\n",confusion_SVC)

#Plot the training set results for the SVM analysis
from matplotlib.colors import ListedColormap
X_set,y_set=X_train,y_train
X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01),
                  np.arange(start=X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1,X2,SVC_classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75,cmap=ListedColormap(('red','green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],
                c=ListedColormap(('red','green','blue'))(i),label=j)
plt.title('Support Vector Machine (Training Data) - RBF Kernel')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

#Plot the test set results for the SVM analysis
from matplotlib.colors import ListedColormap
X_set,y_set=X_test,y_test
X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01),
                  np.arange(start=X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1,X2,SVC_classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75,cmap=ListedColormap(('red','green','blue')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],
                c=ListedColormap(('red','green'))(i),label=j)
plt.title('Support Vector Machine (Test Data) - RBF')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()