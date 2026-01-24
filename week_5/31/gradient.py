import numpy as np

def main():
    feature = np.array([
    [10, 2, 1],
    [20, 4, 2],
    [30, 6, 3],
    [40, 8, 4]])

    target = np.array([1, 2, 3, 4])
    # alpha_list = [0.1,0.2,0.3,0.4]
    # for i in alpha_list:
    ow, ob = gradient_descent(feature,target,learning_rate=0.00001)
    for x in feature:
        pred = sum(ow[j] * x[j] for j in range(len(ow))) + ob
        print(pred)

def gradients(feature, target, weights, data_len, bias):
    # Calculate the gradient with respect to weight:
    sum_w = [0]*len(weights)
    sum_b = 0
    for i in range(data_len):
        X = feature[i]
        prediction = sum(weights[j] * X[j] for j in range(len(weights))) + bias
        error = target[i] - prediction
        for j in range(len(weights)):
            sum_w[j] += error * X[j]

        sum_b += error
    default = -2/data_len
    dw = [default * sw for sw in sum_w]
    db = default * sum_b

    return (dw,db)

def cost_function(feature, target, weights, bias, data_len):
    total = 0
    for i in range(data_len):
        X = feature[i]
        prediction = sum(weights[j] * X[j] for j in range(len(weights))) + bias
        total += (target[i] - prediction)**2
    return total

def gradient_descent(feature,target, learning_rate):
    initial_weight = [0]*len(feature[0])
    initial_bias = 0
    data_len = len(feature)
    cost = cost_function(feature, target, initial_weight, initial_bias, data_len)

    for _ in range(10000):   
        dw, db = gradients(feature, target, initial_weight, data_len, initial_bias)
        for j in range(len(initial_weight)):
            initial_weight[j] -= learning_rate * dw[j]

        initial_bias -= learning_rate*db

        new_cost = cost_function(feature, target, initial_weight, initial_bias, data_len)
        if abs(cost - new_cost) < 1e-6:
            break
        cost = new_cost
    return initial_weight, initial_bias 

if __name__ == "__main__":
    main()
    
