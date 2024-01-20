# %% 7.1 装饰器基础知识
def decorate(func):
    # def inner(num):
    #     print("running xxx", num)
    print("inner")
    return func


@decorate
def fun(num):
    if num:
        nums = 1+num
    else:
        nums = 1
    # print("*** fun()")
    print(nums)


# %% 7.2 Python何时执行装饰器
def f2():
    print("f2")

def main():
    # fun(1)
    f2()

if __name__ ==  "__main__":
    main()

# %% 7.3 使用装饰器改进“策略”模式
