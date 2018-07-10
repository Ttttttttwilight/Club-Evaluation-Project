import csv
import numpy as np
print(np.__file__)
def read_x():
    with open("y.csv", "r") as csvfile:
        # print("open success")
        reader = csv.reader(csvfile)
        prepare, name = [], []
        count = -1
        # print("read_x")
        for line in reader:
            # print(line)
            if count == -1:
                count += 1
                continue

            for i in range(3):
                if not line[i]:
                    line[i] = "空缺"
            name.append(line[0:3])

            for i in range(3, len(line)):
                if not line[i]:
                    line[i] = 0
            prepare.append(line[3:])

            length = len(line)
            for i in range(length - 3):
                if not prepare[count][i]:
                    prepare[count][i] = 0
                else:
                    prepare[count][i] = float(prepare[count][i])
            count += 1
    prepare = np.array(prepare, dtype = float)
    # print(prepare, type(prepare), prepare.dtype, prepare.shape)
    # print(count, name, type(name))

    x1 = [[0]*16 for _ in range(count)]
    x1 = np.array(x1, dtype=float)
    x1[:, 0] = prepare[:, 0]
    x1[:, 1] = -prepare[:, 1]
    x1[:, 2] = prepare[:, 2]
    x1[:, 3] = prepare[:, 3]
    x1[:, 4] = prepare[:, 3]/prepare[:,15]
    x1[:, 5] = prepare[:, 5]
    x1[:, 6] = prepare[:, 6]
    x1[:, 7] = prepare[:, 7]
    x1[:, 8] = prepare[:, 9]
    x1[:, 9] = prepare[:, 9]
    x1[:, 10] = prepare[:, 10]
    x1[:, 11] = prepare[:, 11]
    x1[:, 12] = prepare[:, 12]
    x1[:, 13] = prepare[:, 13]
    x1[:, 14] = prepare[:, 14]
    x1[:, 15] = prepare[:, 15]

    # print(x1, type(x1), x1.dtype, x1.shape)

    # with open("x1_temp.csv", "w", newline='') as temp:
    #     writer = csv.writer(temp)
    #     writer.writerows(x1)
    # print(x1, len(x1[2]))
    # print(count)
    # print(name)
    return x1, count, name
    
if __name__ == '__main__':
    read_x()