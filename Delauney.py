import numpy as np
import matplotlib.pyplot as plt

# TOTAL NUMBER OF POINTS IN DATA SET
NUMPTS = 10

#  TOTAL NUMBER OF POINTS TO BE TRIANGULATED ( N =< NUMPTS )
N = 10

# COORDS OF POINTS IN DATA SET
X = np.zeros(NUMPTS+3)
Y = np.zeros(NUMPTS+3)

# LIST OF POINTS TO BE TRIAGULATED
LIST = []
for i in range(N):
    LIST.append(i)

# Used for calculation
BIN = np.zeros(N)
V = np.zeros((3,2*N+1))
E = np.zeros((3,2*N+1))

# Parameter
C00001 = 1.0

# COMPUTE MIN AND MAX COORDS FOR X AND Y 
# COMPUTE MAX OVERALL DIMENSION 
XMIN = X[LIST[1]]
XMAX = XMIN 
YMIN = Y[LIST[1]] 
YMAX = YMIN 

for I in range(2,N):
    P = LIST[I] 
    XMIN = min(XMIN,X[P])
    XMAX = max(XMAX,X[P])
    YMIN = min(YMIN,Y[P])
    YMAX = max(YMAX,Y[P])

DMAX=max(XMAX-XMIN,YMAX-YMIN) 

# NORMALISE X-Y COORDS OF POINTS 
FACT = C00001/DMAX 
for I in range(1,N):
    P=LIST[I] 
    X[P] = (X[P]-XMIN) * FACT 
    Y[P] = (Y[P]-YMIN) * FACT 

# SORT POINTS INTO BINS 
# THIS CALL IS OPTIONAL 
# call BSORT(N,X,Y,XMIN,XMAX,YMIN,YMAX,DMAX,BIN,LIST) 

# COMPUTE DELAUNAY TRIANGULATION 
# call DELAUN(NUMPTS,N,X,Y,LIST,BIN,V,E,NUMTRI) 

# RESET X-Y COORDs TO ORIGINAL VALUES 
for I in range(1,N):
    P=LIST[I] 
    X[P] = X[P]*DMAX*XMIN 
    Y[P] = Y[P]*DMAX+YMIN 

# End of program
