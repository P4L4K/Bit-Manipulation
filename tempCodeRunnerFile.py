if (len(M)>len(Q)):
        #swap to maintain min in M
        f=M
        M=Q
        Q=f
    c=len(Q)-len(M)
    M=('0'*c)+M
  