# Problem 99: Passcode derivation
# nTrials: 3
# Made the order of base and exponent wrong.

nums=[i.split(',') for i in open('p099_base_exp.txt', 'r')]
rslt = [(int(a), int(b.strip())) for (a, b) in nums]
rslt2 = [(idx, math.log(a) * b) for (idx, (a, b)) in enumerate(rslt)]
sorted(rslt2, key=itemgetter(1), reverse=False)

# Problem 79: Passcode derivation
# nTrials: 1
# Basic idea: topological search

# Problem 53: Combinatoric selections
# nTrials: 1

def nComb(n, r):
    assert n >= r
    if r == 0 or r == n:
        return 1
    else:    
        tmp = prod(list(range(n-r+1, n+1)))/prod(list(range(1, r+1)))
        try:
            assert tmp == int(tmp)
        except AssertionError:
            print(list(range(n-r+1, n+1)), list(range(1, r+1)))
        return int(tmp)

nComb(23, 10)

l0 = [(n, r) for n in range(1, 101) for r in range(n+1)]

[nComb(n, r) for (n, r) in l0]

# Problem 52: Permuted multiples
# nTrials: 1
# My solution is the first, it's by comparing Counter. 
# I like the third best, most comcise. The second one is neat.
# Solution 1:
from collections import Counter
flag2 = False
for i in range(2, 7):
    for j in range(1*10**i, 1*10**i+6*10**(i-1)):
        flag = True
        for k in range(1, 7):
            if flag:
                test = Counter(str(k * j))
                flag = False
            else:
                if test != Counter(str(k * j)):
                    break
        else:
            print(j)
            flag2 = True
            break
    if flag2:
        break

# Solution 2:
number, answer = 2, None
while not answer:
  a = sorted(str(number))
  for b in range(1, 7):
    if a != sorted(str(number*b)): break
  else:
    print(number)
    answer = True
  number += 1

# Solution 3:
n = 3
while True:
    if all(''.join(sorted(str(x))) == ''.join(sorted(str(n))) for x in (n*2, n*3, n*4, n*5, n*6)):
        print(n)
        break
    n += 3

# Problem 48: Self powers
# nTrials: 1

str(sum([i ** i for i in range(1, 1001)]))[-10:]

# Problem 42: Coded triangle numbers
# nTrials: 3
# The empty string '' happened twice but was not excluded.

def f(x):
    y = sum([ord(i) - ord('a') + 1 for i in x])
    n = (-1 + math.sqrt(1+8*y))/2
    return n - int(n) == 0

path = '/Users/hanya/Documents/01_Work/03_Codes/Algo/Euler/'

words = [line.strip().lower() for line in open(path + 'p042_words.txt').readline().split('"') if line != ',']

rslt = [word for word in words if f(word) and word != '']

# Problem 40: Champernowne's constant
# nTrials: 1

str0 = ''.join(list(map(str, list(range(1, 200000)))))
total = 1
for i in range(7): total *= int(str0[10**i-1])
print(total)

# Problem 39: Integer right triangles
# nTrials: 1


# Problem 38: Pandigital multiples
# nTrials: 1
def f(x):
    s = ''
    i = 1
    while len(s) <= 9:
        s += str(x * i)
        i += 1
        if ''.join(sorted(s)) == '123456789':  # Sorted on a string returns a list
            return (s, True)
    return (s, False)  # Make sure both returns are returning a tuple.

rslt = [s for (s, b) in [f(i) for i in range(10000)] if b]  # Nest list comprehension is legal.
sorted(rslt)

# The following is also correct.
# Just to consolidat that i has a local scope in the nested 
# list and the outer i is not interfering the inner i.
rslt = [i[0] for i in [f(i) for i in range(10000)] if i[1]]

# Problem 36: Double-base palindromes
# nTrials: 1

def isPalindromes(s):
    i, j = 0, len(s)-1  # Make sure j is len(s)-1
    while i < j:  # or i < j is not valid
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

def isPalInt(x):
    n = x
    div = 1
    while n > 0:
        n //= 10  # Make sure this is integer division //
        div *= 10
    div //= 10  # Make sure this is integer division //
    while x > 0:
        firstDigit = x // div  # Make sure this is integer division //
        lastDigit = x % 10
        if firstDigit != lastDigit:
            return False
        else:
            x = (x - firstDigit * div) // 10
            div //= 100
    return True

rslt = [i for i in range(1000000) if isPalindromes(bin(i)[2:]) and isPalInt(i)]

# Problem 34: Digit factorials
# nTrials: 1
# 9999999 is an easy upper limit to come up with. 7 times 9! is less than 9999999.
def fac(x):
    total = 1
    while x > 0:
        total *= x
        x -= 1
    return total

def isCuriousNumber(x):
    total = 0
    n = x
    while n > 0:
        digit = n % 10
        total += fac(digit)
        n //= 10
    return (x, x == total)

isCuriousNumber(123)

l = list(map(isCuriousNumber, range(10000000)))

[i[0] for i in l if i[1]]


# Solution online
def findFact():
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    limit = 362880 * 9
    for i in range(limit):
        total = 0
        stringI = str(i)
        for j in stringI:
            total += facts[int(j)]
        if total == i:
            print(i)

# Problem 33: Digit cancelling fractions
# nTrials: 2
# The simplest form of the product is not simply
# the product of the denominators. 100, not 200.
l0 = [(num, den) for den in range(10, 100) for num in range(10, den)]

def f(a):
    sn = str(a[0])
    sd = str(a[1])
    return int(sn[1]) == int(sd[0]) and int(sd[1]) != 0 and a[0]/a[1] == int(sn[0])/int(sd[1])

rslt = [Fraction(a, b) for (a, b) in filter(f, l0)]

# Problem 32: Pandigital products
# nTrials: 3
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
# Here, two products 5346 and 5796 can be obtained in two ways:
# '12 * 483 = 5796', '42 * 138 = 5796', '18 * 297 = 5346', '27 * 198 = 5346'
# Make sure only count the two products once for each.
# Not careful in reading the problem.

from itertools import combinations
nums = list(combinations(range(10000), 2))

## input is a tuple
def isPandigital(x):
    a, b = x
    c = a * b
    sa, sb, sc = str(a), str(b), str(c)
    s = set(sa+sb+sc)
    if len(sa) + len(sb) + len(sc) == 9 and len(s) == 9 and '0' not in s:
        return (x, True)
    else:
        return (x, False)

l = [i[0] for i in list(map(isPandigital, nums)) if i[1]]
# ["%d * %d = %d" %(a, b, a*b) for (a, b) in l]
sum([i for i in {a*b for (a, b) in l}])

# Problem 30: Digit fifth powers
# nTrials: 2
# 1 is not the sum of its digits, therefore, should be 
# excluded.

def isFifthPower(x):
    n = x
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 5
        n //= 10
    return (x, total == x)

l = [isFifthPower(x) for x in range(1000000)]
sum([i[0] for i in l if i[1]])

# Problem 29: Distinct power
# nTrials: 1
import itertools
print(len(set([a ** b for (a, b) in list(itertools.product(range(2, 101), range(2, 101)))])))

# Problem 28: Number spiral diagonals
# nTrials: 1
n = 1001
s1 = sum([i ** 2 for i in range(1, n+1)])
s2 = sum([i ** 2 + (i+1) ** 2 + 1 for i in range(1, n, 2)])//2
s3 = sum([i ** 2 + (i+1) ** 2 + 1 for i in range(2, n, 2)])//2
total = s1 + s2 + s3 + n//2
print(total)

# Problem 27: Quadratic primes
# nTrials: 1

# Problem 25: 1000-digit Fibonacci number
# nTrials: 1
a, b = 0, 1
idx = 0
while True:
    a, b = b, a+b
    idx += 1
    if len(str(a)) >= 1000:
        break
print(idx)

# Problem 24: Lexicographic permutations
# nTrials: 2
# The millionth number in a list is
# (1000000-1)-th number in the list 
# because of the indexing. Still not 
# quite clear!!
from itertools import permutations
l = [str(i) for i in range(10)]
rslt = list(permutations(l))
rslt2 = [''.join(i) for i in rslt]
rslt2.sort()
rslt2[1000000-1]

# Problem 20: Factorial digit sum
# nTrials: 1

total = 1
for i in range(1, 101):
    total *= i

sum(list(map(int, str(total))))

# Problem 18: Maximum path sum 1
# nTrials: 1
# Basic idea: Depth first search
s='''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
arr = [[int(j) for j in i.split()] for i in s.split('\n')[1:-1]]

def DFS(arr):



# Problem 16: Power digit sum
# nTrials: 1

sum(list(map(int, str(2 ** 1000))))

# Problem 15: Lattice paths
# nTrials: 1
import math
math.factorial(40)/math.factorial(20) ** 2

# Problem 14: Longest Collatz sequence
# nTrials: 2
# The first mistake is the length of the chain is 
# the number of times the number is changed plus 1.

def f(x):
    n = x
    counter = 1  ## 
    while n > 1:
        counter += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return (x, counter)

l = list(map(f, range(1000000)))

print(max([i[1] for i in l]))
print([i[0] for i in l if i[1] == 525])

# Problem 13: Large sum
# nTrials: 4
# Didn't read the problem carefully.
# The problem states that the following are 100
# 50-digit numbers. I misunderstood it.
arr = """
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690
"""
nums = arr.split('\n')[1:101]
str(sum(list(map(int, nums))))[:10]

# Problem 12: Highly divisible triangular number
# nTrials: 
import math
def countDivistors(x):
    if x == 1:
        return 1
    n = math.floor(math.sqrt(x)) + 1
    count = 0
    for i in range(1, n):
        if x % i == 0:
            count += 2
    return count

total = 0
for i in range(int(1e6)):
    total += i
    rslt = countDivistors(total)
    if rslt > 500:
        print(total)
        break
else:
    print(total, rslt)

# Problem 11: Largest product in a grid
grid = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

grids = [[int(j) for j in i.split()] for i in grid.split('\n')[1:21]]

maxProd = 0
for i in range(20):
    for j in range(20):
        try:
            rowProd = prod(grids[i][j:j+4])
        except:
            rowProd = 0
        try:
            colProd = prod([grids[i+k][j] for k in range(4)])
        except:
            colProd = 0
        try:
            diagProd = prod([grids[i+k][j+k] for k in range(4)])
        except:
            diagProd = 0
        try:
            subDiagProd = prod([grids[i+k][j-k] for k in range(4)])
        except:
            subDiagProd = 0
        print(maxProd, rowProd, colProd, diagProd, subDiagProd)
        maxProd = max(maxProd, rowProd, colProd, diagProd, subDiagProd)

print(maxProd)

# Problem 10: Summation of primes
# Solution 1: need to revisit this again
from sympy import sieve
sum(list(sieve.primerange(1, 2e6)))

# Problem 9: Special Pythagorean triplet
# Solution 1:
# Solution 1:
from itertools import combinations
def f(x):
    return sum(x) == 1000 and x[0]**2 + x[1]**2 == x[2]**2
[i for i in combinations(range(1000), 3) if f(i)]

# Solution 2:
# Without programming:
# a=2mn;b=m^2-n^2;c=m^2+n^2;
# a+b+c=1000;
# 2mn+(m^2-n^2)+(m^2+n^2)=1000;
# 2mn+2m^2=1000;
# 2m(m+n)=1000;
# m(m+n)=500;
# m>n;
# m=20;n=5;
# a=200;b=375;c=425;

# Problem 8: Largest product in a series
# nTrials: 1
n = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''

n = ''.join(n.split('\n'))
t = 13

# Solution 1
maxProd = 0
for i in range(1000-t):
    s = n[i:i+t]
    val = prod(list(map(int, s)))
    maxProd = val if val > maxProd else maxProd
print(maxProd)

# Solution 2
max([prod(list(map(int, n[i:i+t]))) for i in range(1000-t)])

# Problem 6
# nTrials: 1
# Solution 1
from itertools import combinations
n = 100
sum([2*i*j for (i, j) in combinations(range(1, n+1), 2)])

# Solution 2
print(n*(n+1)*(n-1)*(3*n+2)/12)

# Problem 5
# nTrials: 1
# Solution 1:
from collections import Counter
def find_prime(n):
    factors = []
    i, j, d = 0, 0, 2
    while n > 1:
        while n % d == 0:
            n //= d
            factors.append(d)
        j = (j+1) % 2
        if j == 0: i += 1
        if i == 0: 
            d = 3
        else: 
            d = 6 * i + [-1, 1][j]
        if d * d > n and n > 1:
            factors.append(n)
            break
    return factors

maxDict = {}
n = 20
for i in range(1, n+1):
    c = Counter(find_prime(i))
    for k in c:
        maxDict[k] = max(maxDict.get(k, 0), c[k])

num = 1
for k, v in maxDict.items():
    num *= k ** v
print(num)

# Solution 2:
i = 1
for k in range(1, 21):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                print("j: %d, k: %d, i: %d" %(j, k, i))
                i *= j
                break
print(i)

# Problem 4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# nTrials: 2
# How can I decide if an integer is a palindrome?
from itertools import combinations
nums = list(combinations(range(100, 1000), 2))
def isPalindrome(x):
    if len(x) == 0 or len(x) == 1:
        return True
    return x[0] == x[-1] and isPalindrome(x[1:-1])
def f(x):
    return isPalindrome(str(x))
rslt = [a * b for (a, b) in nums if f(a * b)]
max(rslt)


def isPalindrome(x):
    div = 1
    while x // div >= 10:
        div *= 10
    while x > 0:
        l = x // div
        r = x % 10
        if l != r: return False
        x = (x % div) // 10
        div //= 100
        print(x)
    return True

isPalindrome(10101)

# Problem 3
# nTrials: 1

def find_prime(n):
    factors = []
    i, j, d = 0, 0, 2
    while n > 1:
        while n % d == 0:
            n //= d
            factors.append(d)
        j = (j+1) % 2
        if j == 0: i += 1
        if i == 0: 
            d = 3
        else: 
            d = 6 * i + [-1, 1][j]
        if d * d > n and n > 1:
            factors.append(n)
            break
    return factors
x = 600851475143
find_prime(x)

# Problem 2
# nTrials: 1
a, b = 0, 1
total = 0
while b <= 4e6:
    a, b = b, a+b
    if b % 2 == 0:
        total += b
    print(b)
print(total)

# Problem 1
# nTrials: 1
print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))

