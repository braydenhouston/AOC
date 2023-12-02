import os

def only_nums(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))


ll = [x for x in open(os.path.join(os.path.dirname(__file__),'input.txt')).read().strip().split('\n')]
sum = 0

for l in ll: 
    n = only_nums(l)
    print("First {} Last: {}".format(n[0], n[-1]))
    sum += int(n[0] + n[-1])
    
print("Sum {}".format(sum))