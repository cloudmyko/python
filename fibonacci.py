# fibonacci sequence

length = int(input())

seq = [1,1]

for i in range(length - 1):
    x = seq[-1] + seq[-2] # <-- does the adding for the current number and the one prior
    seq.append(x)

print(seq)


