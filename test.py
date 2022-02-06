class A:
    a='1'

    @staticmethod
    def test():
        print(A.a)

if __name__ =='__main__':
    q=A()
    q.test()