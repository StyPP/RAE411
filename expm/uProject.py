#import
import matplotlib.pyplot as plt
import math as m

#-------------------------------------------------------------------------------

#parameters
nbcol_lines = 2
step = 1
begin = 0
end = 2
color = "red"

a = [[-12, 12], [3, -3]]

#-------------------------------------------------------------------------------

#expm function
def initmat(X):
    """Init the matric with 0"""
    l = len(X)
    result = []
    for i in range(l):
        result.append([0] * l)
    return result

def power2(X):
    """Power of two square matrix"""
    l = len(X)
    result = initmat(X)
            
    for i in range(l):
        for j in range(l):
            for k in range(l):
                result[i][j] += X[i][k] * X[k][j]
    return result

def swapmat(X, Y):
    """Change two matrix"""
    l = len(X)
    for i in range(l):
        for j in range(l):
            X[i][j] = Y[i][j]
            Y[i][j] = 0
    return (X, Y)
            
def powermat(X, p):
    """Power of square matrix"""
    l = len(X)
    m = 2
    result = initmat(X)
    
    Y = power2(X)
    
    while m < p:
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    result[i][j] += Y[i][k] * X[k][j]
                
        Y, result = swapmat(Y, result)
        m = m + 1
        
    return Y

def facto(n):
    """Computes n factorial, begins 3"""
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

def matxl(X, n):
    """Computes the multiplication between a square matrix and a number"""
    l = len(X)
    result = initmat(X)
    
    for i in range(l):
        for j in range(l):
            result[i][j] = X[i][j] * n
    return result

def addmat(X, Y):
    """Computes the additional of two matrix"""
    l = len(X)
    result = initmat(X)
    
    for i in range(l):
        for j in range(l): 
            result[i][j] = X[i][j] + Y[i][j]
    return result

def matid(X):
    """Returns the identity matrix of the X matrix"""
    l = len(X)
    result = initmat(X)
        
    for i in range(l):
        for j in range(l):
            if(i == j):
                result[i][j] = 1
                
    return result
    
def expmat(X, value):
    """Computes exponential of matrix (O until value)"""
    l = len(X)
    result = initmat(X)
        
    for k in range(2, value):
        result = addmat(matxl(powermat(X, k),(1 / facto(k))), result)
        
    result = addmat(result, X)
    result = addmat(result, matid(X))
    
    return result

def probability(X, t, n):
    """Final function"""
    Y = matxl(X, t)
    Y = expmat(Y, n)
    return Y

#-------------------------------------------------------------------------------
    
#graphics settings
plt.xlim(0, 3)
plt.ylim(0, 1)

plt.grid(b=None, axis='both', linestyle = '--')
plt.title("Micro project 1")
plt.xlabel("Time")
plt.ylabel("Probability")

fig = plt.gcf()
fig.set_size_inches(17.5, 8.5)

#-------------------------------------------------------------------------------

#points
vect = []

for i in range(nbcol_lines * nbcol_lines):
    vect.append([])

for i in range(begin, end * 100, step):
    m = probability(a, i / 100, 100)
    cpt = 0
    
    for j in range(nbcol_lines):
        for k in range(nbcol_lines):
            vect[cpt].append(m[j][k])
            cpt = cpt + 1

x = [i / 100 for i in range(begin, end * 100, step)]

#-------------------------------------------------------------------------------

#display
for i in range(nbcol_lines * nbcol_lines):
    plt.plot(x, vect[i], color="red")

plt.savefig('graph.pdf')
plt.savefig('graph.png')