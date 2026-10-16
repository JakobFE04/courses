import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt 
import numpy as np
import keras
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from keras import ops 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = ops.ones((10,2)) # Makes an input matrix with 2 rows and 10 coloums with ones (1).

model = Sequential()
model.add(keras.Input(shape=(2,)))
model.add(Dense(6, activation="relu", name="layer1"))
model.add(Dense(7, activation="relu", name="layer2"))
model.add(Dense(1, activation="sigmoid", name="output"))

model(x)
model.compile(
        optimizer="SGD",
        loss="binary_crossentropy",
        metrics=["accuracy"]
        )


X, y = make_moons(n_samples=2000, shuffle=True, noise=0.2, random_state=42)

x_temp, x_test, y_temp, y_test = train_test_split(X, y, test_size=0.2)
x_train, x_val, y_train, y_val = train_test_split(x_temp, y_temp, test_size=0.2)

history = model.fit(x_train, y_train, batch_size=64, epochs=10, validation_data=(x_val, y_val))

predictions = model.predict(x_test)
predictions = (predictions > 0.5).astype(int)

x_t, y_t = np.array(x_test).T
x_tr, y_tr = np.array(x_train).T

fig, (ax, xa) = plt.subplots(1,2, figsize=(15,10))
ax.scatter(x_t, y_t, c=predictions[:,0], cmap="coolwarm", label="Predictions")
xa.scatter(x_tr, y_tr, c=y_train, cmap="magma", label="Train")
fig.legend()

#train_losses = history.history["loss"]
#val_losses = history.history["val_loss"]
#epochs = np.arange(1, len(train_losses)+1)
#plt.plot(epochs, train_losses, label="Train loss")
#plt.plot(epochs, val_losses, label="Validation loss")
#plt.xlabel("Epochs")
#plt.ylabel("Loss")
#plt.legend()
plt.show()



