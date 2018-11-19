wlec = [0.65, 0.8, 0.8, 0.9]
weight = [0.3, 0.2, 0.9]


def neural_network(input, weights):
    pred = ele_mul(input, weights)
    return pred


def ele_mul(a, vector):
    output = [0, 0, 0]
    assert(len(output) == len(vector))

    for i in range(len(vector)):
        output[i] = a * vector[i]

    return output


input = wlec[0]
prediction = neural_network(input, weight)
print(prediction)
