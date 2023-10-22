from math import cos, radians, sqrt, acos, degrees

# def triangle_rule(a, b, c):
#     if all([a+b>c, a+c>b, b+c>a]):
#         return True
#     else:
#         return False
    

def factorize(n):
    x = 2
    factors = []
    while n != x:
        if n % x == 0:
            factors.append(x)
            n = n // x
        else:
            x += 1
    if factors:
        factors.append(n)
    if not factors:
        factors.append(n)
    return factors


def gcd(a, b, c):
    factors_a = factorize(a)
    factors_b = factorize(b)
    factors_c = factorize(c)
    for factor in factors_a:
        if all([factor in factors_b, factor in factors_c]):
            return False
    for factor in factors_b:
        if all([factor in factors_a, factor in factors_c]):
            return False
    for factor in factors_c:
        if all([factor in factors_a, factor in factors_b]):
            return False
    return True


def cosine_rule_side(b, c, A):
    a = sqrt(b**2 + c**2 - 2*b*c*cos(radians(A)))
    return a

def cosine_rule_angle_A(a, b, c):
    A = (b**2 + c**2 - a**2) / (2*b*c)
    return A

def cosine_rule_angle_B(a, b, c):
    B = (c**2 + a**2 - b**2) / (2*c*a)
    return B

def cosine_rule_angle_C(a, b, c):
    C = (a**2 + b**2 - c**2) / (2*a*b)
    return C


def per_ang_twice(N):
    triangles = []
    n = 1
    while True:
        m = n + 1
        while 0 < n < m < 2*n:
            a = n**2
            b = m * n
            c = m**2 - n**2
            if gcd(a, b, c):
                triangle = tuple(sorted((a, b, c)))
                triangles.append(
                    [sum(triangle), [triangle]]
                    )
                if len(triangles) == N:
                    for i, t in enumerate(sorted(triangles)):
                        i += 1
                        print(f'{i}.', t, degrees(acos(cosine_rule_angle_A(t[1][0][0], t[1][0][1], t[1][0][2]))), degrees(acos(cosine_rule_angle_B(t[1][0][0], t[1][0][1], t[1][0][2]))), degrees(acos(cosine_rule_angle_C(t[1][0][0], t[1][0][1], t[1][0][2]))))
                    return True
                m += 1
            else:
                m += 1
        n += 1


# r = [2, 3, 3, 4, 5, 4, 5, 6, 5, 7, 5, 7, 8, 7, 6, 9, 7, 8, 9, 7, 10, 7, 8, 11, 9, 10, 11, 9, 12, 8, 11, 13, 11, 9, 13, 11, 14, 9, 10, 13, 11, 12, 15, 13, 11, 14, 15, 10, 13, 16, 11, 12, 13, 11, 14, 17, 15, 13, 16, 11, 17, 18, 13, 17, 13, 16, 19, 17, 12, 15, 13, 19, 14, 17]

# s = [3, 4, 5, 5, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 11, 10, 11, 11, 11, 12, 11, 13, 13, 12, 13, 13, 13, 14, 13, 15, 14, 14, 15, 16, 15, 16, 15, 17, 17, 16, 17, 17, 16, 17, 18, 17, 17, 19, 18, 17, 19, 19, 19, 20, 19, 18, 19, 20, 19, 21, 19, 19, 21, 20, 22, 21, 20, 21, 23, 22, 23, 21, 23, 22]

# for i in range(len(r)):
#     print(sorted((r[i]*s[i],s[i]**2 - r[i]**2,r[i]**2)))

print(per_ang_twice(10000))
