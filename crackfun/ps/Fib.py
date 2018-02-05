class fib():
    def fib_num(self,n):
        if n==1:
            return 1
        if n==2:
            return 1
        return self.fib_num(n-2)+self.fib_num(n-1)

    def fib_num2(self,n):
        if n==1:
            return 1
        if n==2:
            return 1
        fibs = [0]*(n+1)
        fibs[1] = 1
        fibs[2] = 1
        for i in range(3,n+1):
            fibs[i] = fibs[i-1] + fibs[i-2]
        return fibs[-1]
