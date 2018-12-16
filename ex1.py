from keras.models import Sequential
from keras.layers import Dense
import numpy

numpy.random.seed(7)
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter= ".")
X = dataset[:, 0:8]
Y = dataset[:, 8]

model = Sequential()
model.add(Dense, (12, input_dim=8, activation=relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=10, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print(f"The metric is {model.metrics_names[1]}\n And its score is {scores[1]*100}")
