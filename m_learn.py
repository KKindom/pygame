from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
#读取数据
data ,target=load_iris(return_X_y=True)
print(target)
x_train,x_test,y_train,y_test=train_test_split(data,target,test_size=0.2)
# 选择模型
# 聚类问题
# model=KMeans(n_clusters=3)
#分类问题
# model=KNeighborsClassifier();
model=DecisionTreeClassifier();
#训练
# lable=model.fit_predict(data)
model.fit(x_train,y_train)
# print(lable)
#查看结果
# for a,b in zip(target,lable):
#     print(a,b)
result=model.predict(x_test)
print(classification_report(y_test,result))
# print(data)