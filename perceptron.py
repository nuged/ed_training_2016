from sklearn.linear_model import Perceptron
from numpy import genfromtxt

path = "/home/ed/Dropbox/HSE_2016/problems/"
path_answer = "/home/ed/Документы/Classifier Results/"
name = input()
path += name
path += '/'
name = input()

def main():
    train = genfromtxt(path + name + "_train_input.csv", delimiter=',')
    target = genfromtxt(path + name + "_train_output.csv", delimiter=',')
    test = genfromtxt(path + name + "_test_input.csv", delimiter=',')
    label = genfromtxt(path + name + "_test_output.csv", delimiter=',')

    per = Perceptron()
    per.fit(train, target)
    result = per.score(test, label)
    print(result)
    number = input()
    f = open(path_answer + "perceptron.txt", "a")
    f.write(number + "," + str(result) + "\n")
    f.close()

if __name__=="__main__":
    main()