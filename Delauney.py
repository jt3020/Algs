import numpy as np
import matplotlib.pyplot as plt

def DELAUN(NUMPTS,N,X,Y,LIST,BIN,V,E,NUMTRI):
    # Parameters
    C00000 = 0.0
    C00100 = 100.0

    # DEFINE VERTEX AND ADJACENCY LISTS FOR SUPERTRIANOLE 
    VI = NUMPTS+1 
    V2 = NUMPTS+2 
    V3 = NUMPTS+3 
    V[1,1] = V1 
    V[2,1] = V2 
    V[3,1] = V3 
    E[1,1] = 0 
    E[2,1] = 0 
    E[3,1] = 0 

    # SET COORDS OF SUPERTRIANGLE 
    X[V1] = -C00100 
    X[V2] =  C00100 
    X[V3] =  C00000 
    Y[V1] = -C00100  
    Y[V2] = -C00100  
    Y[V3] =  C00100 

    # LOOP OVER EACH POINT 
    NUMTRI = I 
    TOPSTK = 0 
    MAXSTK = NUMPTS 
    for I in range(1,N): 
        P=LIST[I] 
        XP=X[P] 
        YP=Y[P] 
        # LOCATE TRIANGLE IN WHICH POINT LIES 
        T = 0 # T = TRILOC(XP,YP,X,X,V,E,NUMTRI) 

        # CREATE N~ VERTEX AND ADJACENCY LISTS FOR TRIANGLE T 
        A = E[1,T] 
        B = E[2,T] 
        C = E[3,T] 
        V1 = V[1,T] 
        V2 = V[2,T] 
        V3 = V[3,T] 
        V[1,T] = P 
        V[2,T] = V1 
        V[3,T] = V2 
        E[1,T] = NUMTRI + 2 
        E[2,T] = A 
        E[3,T] = NUMTRI + 1 

        # CREATE NEW TRIANGLES 
        NUMTRI = NUMTRI + 1 
        V[1,NUMTRI] = P 
        V[2,NUMTRI] = V2 
        V[3,NUMTRI] = V3 
        E[1,NUMTRI] = T 
        E[2,NUMTRI] = B 
        E[3,NUMTRI] = NUMTRI+1 
        NUMTRI=NUMTRI+I 
        V[1,NUMTRI] = P 
        V[2,NUMTRI] = V3 
        V[3,NUMTRI] = V1 
        E[1,NUMTRI] = NUMTRI-1 
        E[2,NUMTRI] = C 
        E[3,NUMTRI] = T










# Start of Program

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
# BSORT(N,X,Y,XMIN,XMAX,YMIN,YMAX,DMAX,BIN,LIST) 

# COMPUTE DELAUNAY TRIANGULATION 
DELAUN(NUMPTS,N,X,Y,LIST,BIN,V,E,NUMTRI) 

# RESET X-Y COORDs TO ORIGINAL VALUES 
for I in range(1,N):
    P=LIST[I] 
    X[P] = X[P]*DMAX*XMIN 
    Y[P] = Y[P]*DMAX+YMIN 

# End of program
