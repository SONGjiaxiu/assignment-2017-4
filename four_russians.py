import csv
import math
import sys
import os.path

def four_russians(input_1, input_2):
    n = len(input_1)
    m = math.floor(math.log2(n))

    diff = math.ceil(n/m)*m - n

    # apply padding
    if diff > 0:
        for i in range(n):
            for j in range(diff):
                input_1[i].append(0)
                input_2[i].append(0)

        for j in range(diff):
            new = []
            for i in range(n+diff):
                new.append(0)
            input_1.append(new)

            new = []
            for i in range(n+diff):
                new.append(0)
            input_2.append(new)

    # allocate output and init to zero
    output = []
    for i in range(n):
        new = []
        for j in range(n):
            new.append(0)
        output.append(new)

    for step in range(1, math.ceil(n/m)+1):
        # allocate output
        rs = []
        for i in range(2**m):
            new = []
            for j in range(n):
                new.append(0)
            rs.append(new)

        bp = 1
        k = 0

        for j in range(1, 2**m):
            for i in range(n):
                if rs[j-2**k][i] == 1 or input_2[(step)*m-1-k][i] == 1:
                    rs[j][i] = 1
                else:
                    rs[j][i] = 0

            if bp == 1:
                bp = j + 1
                k = k + 1
            else:
                bp = bp - 1


        # allocate ci
        ci = []
        for i in range(n):
            new = []
            for j in range(n):
                new.append(0)
            ci.append(new)

        # calculate power
        for i in range(n):
            power = 0
            for j in range(m):
                power = power + (input_1[i][(step-1) * m + j]) * (2 ** (m - 1 - j))

            for j in range(n):
                ci[i][j] = rs[power][j]

        for i in range(n):
            for j in range(n):
                if output[i][j] == 1 or ci[i][j] == 1:
                    output[i][j] = 1
                else:
                    output[i][j] = 0
    return output


def main():
    if len(sys.argv) == 3:
        input_a = sys.argv[1]
        input_b = sys.argv[2]

        print("Input A:  %s" % (input_a))
        print("Input B:  %s" % (input_b))

        if not os.path.isfile(input_a):
            print("File %s not found." % (input_a))
            return
        else:
            with open(input_a, 'rt') as f:
                reader = csv.reader(f)
                input_1 = list(reader);

        if not os.path.isfile(input_b):
            print("File %s not found." % (input_b))
            return
        else:
            with open(input_b, 'rt') as f:
                reader = csv.reader(f)
                input_2 = list(reader);

        for i in range(len(input_1)):
            for j in range(len(input_1[i])):
                input_1[i][j] = int(input_1[i][j])

        for i in range(len(input_2)):
            for j in range(len(input_2[i])):
                input_2[i][j] = int(input_2[i][j])

        output = four_russians(input_1, input_2)

        print("########################################")
        print("                 output")
        print("########################################")

        for i in range(len(output)):
            for j in range(len(output[i])):
                if j > 0:
                    print(',', end='')
                print(output[i][j], end='')
            print()
    else:
        print("Invalid number of arguments")

# ---------------------------------------------------------------------------
main()