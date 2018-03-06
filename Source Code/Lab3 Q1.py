#Don Baker
#Comp-Sci 5590
#Lab 3, Question 1
#Pick any dataset and make a prediction model using LDA.  Compare the results to logistic regression

#Guidance and example code taken from Learn&Teach YouTube videos at https://www.youtube.com/channel/UCGD8R7ct8cQfMMuUFImqDdQ


#Import Packages/Libraries
import matplotlib.pyplot as plt
import numpy as np

#Import Wine data
from sklearn import datasets
wine = datasets.load_wine()

#Split the Wine data into training and testing data sets for cross-validation
from sklearn import model_selection as cv
X=wine.data
y=wine.target
splits=cv.train_test_split(X,y,test_size=0.20)
X_train,X_test,y_train,y_test=splits

#Scale the data to provide more accurate evalaution
from sklearn.preprocessing import StandardScaler
Scale_X=StandardScaler()
X_train=Scale_X.fit_transform(X_train)
X_test=Scale_X.transform(X_test)

#Complete Logistic Regression and Linear Discriminant Analysis to compare

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda_wine=LDA(n_components=2)
X_train=lda_wine.fit_transform(X_train,y_train)
X_test=lda_wine.transform(X_test)

#Logistic Regression
from sklearn.linear_model import LogisticRegression
wine_LDA_classifier=LogisticRegression(random_state=5)
wine_LDA_classifier.fit(X_train,y_train)

#Predict the results of the model using the test set of data
y_pred_LDA=wine_LDA_classifier.predict(X_test)

#Create and display the confusion matrix for the analysis
from sklearn.metrics import confusion_matrix
confusion_LDA=confusion_matrix(y_test,y_pred_LDA)
print("The confusion matrix for the Linear Discriminat Analysis is:\n",confusion_LDA)

#Plot the training set results for the LDA
from matplotlib.colors import ListedColormap
X_set,y_set=X_train,y_train
X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01),
                  np.arange(start=X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1,X2,wine_LDA_classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75,cmap=ListedColormap(('red','green','blue')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],
                c=ListedColormap(('red','green','blue'))(i),label=j)
plt.title('Linear Discriminant Analysis Training Data')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.legend()
plt.show()

#Plot the test set results for the LDA
from matplotlib.colors import ListedColormap
X_set,y_set=X_test,y_test
X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01),
                  np.arange(start=X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1,X2,wine_LDA_classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75,cmap=ListedColormap(('red','green','blue')))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],
                c=ListedColormap(('red','green','blue'))(i),label=j)
plt.title('Linear Discriminant Analysis Test Data')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.legend()
plt.show()