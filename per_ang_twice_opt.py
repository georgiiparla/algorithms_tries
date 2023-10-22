def gcd_rec(m, n):
    if n == 0:
        return m
    else:
        return gcd_rec(n, m%n)


def per_ang_twice(N):
    triangles = {}
    N_required = round(N*1.75)
    n = 1
    while True:
        m = n + 1
        while 0 < n < m < 2*n:
            if gcd_rec(m, n) == 1:
                a = n**2
                b = m * n
                c = m**2 - n**2
                triangle = tuple(sorted((a, b, c)))
                if triangles.get(sum(triangle)):
                    triangles[sum(triangle)] = triangles.get(sum(triangle)), triangle
                else:
                    triangles[sum(triangle)] = triangle
                if len(triangles) == N_required:
                    perimeters = sorted(list(triangles.keys()))
                    sorted_triangles = {i: triangles[i] for i in perimeters}
                    if len(sorted_triangles[perimeters[N-1]]) == 2:
                        return [perimeters[N-1], [i for i in sorted(sorted_triangles[perimeters[N-1]])]]
                    else:
                        return [perimeters[N-1], [sorted_triangles[perimeters[N-1]]]]
                m += 1
            else:
                m += 1
        n += 1


print(per_ang_twice(44953))
