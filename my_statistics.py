from math import sqrt, fsum

def mean(data):
    return fsum(data)/len(data)

def std(data):
	m = mean(data)
	return sqrt(fsum(map(lambda a: (a-m)*(a-m), data)))

if __name__ == '__main__':
	print mean([1,2,3])
	print std([1,2,3])