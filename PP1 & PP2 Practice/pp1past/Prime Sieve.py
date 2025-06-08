n=int(input())
prime_sieve = []
for i in range(2,n+1):
    prime_sieve.append(i)
def delete(n,list):
    for j in list:
        if j==n:
            continue
        elif float(j)%n==0:
            prime_sieve.remove(j)
    return (prime_sieve)
prime_sieve=delete(2,prime_sieve)
prime_sieve=delete(3,prime_sieve)
for i in prime_sieve:
    prime_sieve=delete(i,prime_sieve)
for k in prime_sieve:
    print(k,end=" ")