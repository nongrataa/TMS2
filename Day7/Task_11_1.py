
def decorate(func):
    def results(details, **kwargs):
        # data = {}
        # for i, j in kwargs.items():
        #     data[str(j)] = str(i)
        # func(**data)
        data = {}
        for i, j in kwargs.items():
            data[i] = j*details
        func(details,**data)
    return results

def dec2(func):
    def results(details, **kwargs):
        print(kwargs)
        data = {}
        for i, j in kwargs.items():
            if j%3==0:
                data[i] = 0
            else:
                data[i]=j
        func(details, **data)

    return results


@decorate
@dec2
def result(dateils, **kwargs):
    print(kwargs)


result(details=2, a=1, b=2, c=3, d=4, e=5)
