weight = [[0.1, 0.1, -0.3],
          [0.1, 0.2, 0.0],
          [0.0, 1.3, 0.1]]


def neural_network(input, weights):
    pred = vect_mat_mul(input, weights)
    return pred


def vect_mat_mul(vector, matrix):
    assert (len(vector) == len(matrix))
    sum_output = 0
    output = [0] * len(vector)

    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            output[j] += vector[i] * matrix[j][i]
            print(output)

    return output


toss = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]


input = [toss[0], wlrec[0], nfans[0]]
prediction = neural_network(input, weight)
print(prediction)
