from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt

path = "/home/ed/Dropbox/HSE_2016/problems/"
path_answer = "/home/ed/Документы/Classifier Results/"
name = input()
path += name
path += '/'

def main():
    train = genfromtxt(path + "train_input.csv", delimiter=',')
    target = genfromtxt(path + "train_output.csv", delimiter=',')
    test = genfromtxt(path + "test_input.csv", delimiter=',')
    label = genfromtxt(path + "test_output.csv", delimiter=',')

    sgd = RandomForestClassifier()
    sgd.fit(train, target)
    result = sgd.score(test, label)
    print(result)
    number = input()
    f = open(path_answer + "RF.csv", "a")
    f.write(number + "," + str(result) + "\n")
    f.close()

if __name__=="__main__":
    main()