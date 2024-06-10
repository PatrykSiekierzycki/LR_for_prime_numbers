import numpy as np
import sklearn, pickle
from sklearn import linear_model
import keyboard as kb

"""
Brief: Create three numpy arrays:
    - one with integer numbers from 0 to provided number
    - second with 0, if number is not primal and 1 if it is primal.
    - third with 0, if number is odd and 1 if it is even.
Return: three numpy arrays
"""
def prime_numbers(number:int) -> tuple:

    numbers_list = np.array([1])
    is_prime = np.array([0])
    even_number = np.array([0])

    i = 2
    while i <= number:
        print(i)  # You can delete this line to speed up a little function, but you lost possibility to know, on what number function actually is.
        flag = False
        for num in range(2, i+1):
            if num != 1 and num != i:
                if i % num == 0:
                    numbers_list = np.append(numbers_list, [i])
                    is_prime = np.append(is_prime, [0])
                    flag = True
                    break
        # If it is a prime number:
        if flag is False:
            numbers_list = np.append(numbers_list, [i])
            is_prime = np.append(is_prime, [1])
        # Check is it even number.
        if i % 2 == 0:
            even_number = np.append(even_number, [1])
        else:
            even_number = np.append(even_number, [0])
        i += 1
        flag = False
    return numbers_list, is_prime, even_number

"""
Brief: Creat linear regression model, and train it and test it untill the accuracy is smaller than 90, or untill user press: q. When one of that happen the most accurate model will be saved as: prime_numbers_model_lr.pickle file.
"""
def linear_regresion_for_prime_numbers():

    how_many_numbers = int(input("How many numbers preper: "))

    numbers_list, is_prime, even_number = prime_numbers(how_many_numbers)

    x = np.stack((numbers_list, even_number), axis=1)
    y = is_prime

    accuracy = 0
    max_accuracy = 0
    best_model = None
    
    while accuracy < 0.90:  # It basicly never happen.
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y ,test_size=0.1)  # Get parts for training and test.

        linear = linear_model.LinearRegression()  # Creat linear regression model.
        linear.fit(x_train, y_train)  # Train model.
        accuracy = linear.score(x_test, y_test)  # Get model's accuracy
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            best_model = linear
            print(max_accuracy)

        if kb.is_pressed("q"):
            break
    
    # Save trained model
    with open("prime_numbers_model_lr.pickle", "wb") as file:
        pickle.dump(best_model, file)

linear_regresion_for_prime_numbers()
