from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt
from sklearn import cross_validation

path = "C:/Pendigits/pendigits_"
train = genfromtxt(path + "train_input.csv", delimiter=',')
target = genfromtxt(path + "train_output.csv", delimiter=',')
test = genfromtxt(path + "test_input.csv", delimiter=',')
label = genfromtxt(path + "test_output.csv", delimiter=',')

max_score = 0
best_parameter = 0
for i in range(10, 200, 10):
    rf = RandomForestClassifier(n_estimators=i)
    rf.fit(train, target)
    score = cross_validation.cross_val_score(rf, train, y=target, cv=25).mean()
    if score > max_score + 0.00009:
        max_score = score
        best_parameter = i
print('n_estimators=', best_parameter)

gini = RandomForestClassifier(n_estimators=best_parameter, criterion='gini')
gini.fit(train, target)
score_gini = cross_validation.cross_val_score(gini, train, y=target, cv=25).mean()

entropy = RandomForestClassifier(n_estimators=best_parameter, criterion='entropy')
entropy.fit(train, target)
score_entropy = cross_validation.cross_val_score(entropy, train, y=target, cv=25).mean()

criterion = ""
if score_gini > score_entropy:
    criterion = "gini"
else:
    criterion = "entropy"

print("criterion=", criterion)

RF = RandomForestClassifier(n_estimators=best_parameter, criterion=criterion)
RF.fit(train, target)
print(RF.score(test, label))