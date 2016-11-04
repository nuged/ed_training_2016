import matplotlib.pyplot as plt

f = open("C://results.csv", "r")
results = []
for line in f:
    results.append(line.rstrip().split(",")[1:])
for i in range(len(results)):
    for j in range(len(results[i])):
        results[i][j] = 100 - float(results[i][j])
        if results[i][j] == 0:
            results[i][j] = 0.1  # 100%-accurate methods are impossible
X = []
Y = []
for i in range(18):
    x_current = []
    for line in results:
        best = line.index(min(line))
        if line[best] == 100:
            continue  # some tasks are excluded
        ratio = line[i] / line[best]
        x_current.append(ratio)
    x_current.sort()
    X.append(x_current)

for x in X:
    y_current = []
    for elem in x:
        counter = 0
        for num in x:
            if num <= elem:
                counter += 1
        counter -= 1
        y_current.append(counter / 23)
    Y.append(y_current)

segments = [0, 5, 10, 14, 18]

for i in range(len(segments) - 1):
    for j in range(segments[i], segments[i + 1]):
        plt.step(X[j], Y[j])
    plt.show()

best = [3, 7, 12, 15]
for item in best:
    plt.step(X[item], Y[item])
plt.show()
