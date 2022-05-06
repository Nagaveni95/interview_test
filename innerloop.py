def max1(a, b, c):
    def max2(x, y):
        return x if (x > y) else y

    return max2(a, max2(b, c))


ans = max1
print(ans(40, 60, 30))
