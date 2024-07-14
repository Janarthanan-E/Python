class pattern():

    def inc_tri(n):
        for i in range(n):
            for j in range(i+1):
                print('$',end=' ')
            print()

    def dec_tri(n):
        for i in range(n):
            for j in range(i,n):
                print('*',end=' ')
            print()
    
    def ri_tri(n):
        for i in range(n):
            for j in range(i,n):
                print(' ',end=' ')
            for j in range(i+1):
                print('*',end=' ')
            print()
    
    def rd_tri(n):
        for i in range(n):
            for j in range(i+1):
                print(' ',end=' ')
            for j in range(i,n):
                print('*',end=' ')
            print()
    
    def hill(n):
        for i in range(n):
            for j in range(i,n):
                print(' ',end=' ')
            for j in range(i+1):
                print('*',end=' ')
            for j in range(i):
                print('*',end=' ')
            print()
    
    def down_hill(n):
        for i in range(n):
            for j in range(i+1):
                print(' ',end=' ')
            for j in range(i,n):
                print('*',end=' ')
            for j in range(i,n-1):
                print('*',end=' ')
            print()

    def diamond(n):
        for i in range(n-1):
            for j in range(i,n):
                print(' ',end=' ')
            for j in range(i+1):
                print('*',end=' ')
            for j in range(i):
                print('*',end=' ')
            print()
        for i in range(n):
            for j in range(i+1):
                print(' ',end=' ')
            for j in range(i,n):
                print('*',end=' ')
            for j in range(i,n-1):
                print('*',end=' ')
            print()

pattern.diamond(5)
