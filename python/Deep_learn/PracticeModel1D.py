#if using first time please comment out pip below
#to install keras and tensorflow kindly use below command in terminal of vscode
#pip install keras tensorflow pydot



import matplotlib.pyplot as plt
from keras.layers import Dense,Flatten
from keras.models import Sequential
from keras.utils import to_categorical
from keras.datasets import mnist
from keras import utils

(X_train,Y_train),(X_test,Y_test)=mnist.load_data()
X_train.shape,X_test.shape,X_train.size,X_test.size

fig,axis=plt.subplots(ncols=10,sharex=False,sharey=True,figsize=(20,4))
for i in range(10):
    axis[i].set_title(Y_train[i])
    axis[i].imshow(X_train[i],cmap='gray')
    axis[i].get_xaxis().set_visible(False)
    axis[i].get_yaxis().set_visible(False)
plt.show()

Y_train = to_categorical(Y_train, num_classes=10)
Y_test = to_categorical(Y_test, num_classes=10)

Y_train.shape

#model
model=Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(10,activation='sigmoid'))
model.add(Dense(5,activation='sigmoid'))
model.add(Dense(10,activation='softmax'))
model.summary()

utils.plot_model(model,show_shapes=True)

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X_train,Y_train,epochs=10,batch_size=32,validation_data=(X_test,Y_test))

model.evaluate(X_test,Y_test)
model.save('practice.keras')