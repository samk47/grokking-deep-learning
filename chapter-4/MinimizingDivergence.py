weight = 0.5
input = 2
goal_prediction = 0.8
alpha = 0.1

for iteration in range(20):
    pred = input * weight
    error = (pred - goal_prediction) ** 2
    delta = pred - goal_prediction
    weight_delta = delta * input
    weight -= (weight_delta * alpha)

    print("Error: " + str(error) + " Prediction: " + str(pred))
