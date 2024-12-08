import numpy as np
from collections import Counter
import warnings

from sympy.parsing.sympy_parser import _T

from tabulate import tabulate
import settings as st
M = 10000000
P = st.P  # Phát
T = st.T  # Thu
C = st.c  # chi phí

if sum(P) < sum(T):
    P.append(sum(T) - sum(P))
    C.append([M for i in range(len(T))])
elif sum(P) > sum(T):
    T.append(sum(P) - sum(T))
    for ct in C:
        ct.append(0)

P = np.array(P)
T = np.array(T)
C = np.array(C)
suy_bien = (-1, -1)

def in_phuong_an(C, P, T, s, X, u=None, v=None):
    n, m = C.shape
    if u is None:
        u = [[0] * n]
        v = [[0] * m]
    l_res1 = [[0] * m for i in range(n)]
    l_res2 = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            new_cost = C[i, j] - v[j] - u[i]
            if X[i, j] == 0:
                l_res1[i][j] = f"___[{C[i, j]}]"
            else:
                l_res1[i][j] = f"{X[i, j]}[{C[i, j]}]"
            l_res2[i][j] = f"[{C[i, j]}] --> [{new_cost}]"
    l_res1 = np.array(l_res1)
    l_res1 = np.column_stack((P, l_res1))
    l_res1 = np.vstack((np.append(s, T), l_res1))

    l_res2 = np.array(l_res2)
    l_res2 = np.column_stack((u, l_res2))
    l_res2 = np.vstack((np.append("v/u", v), l_res2))

    print(tabulate(l_res1, tablefmt="grid"))
    print(f"Tổng chi phí của phương án: {np.sum(X * C)}")
    print("__Bảng chi phí biến đổi__")
    print(tabulate(l_res2, tablefmt="grid"))


def tim_phuong_an_ban_dau(C, T, P):
    cuoc = np.copy(C)
    phat = np.copy(P)
    thu = np.copy(T)

    n, m = cuoc.shape

    X = np.zeros((n, m))
    chi_so = [(i, j) for i in range(n) for j in range(m)]
    sorted_cuoc_phi = sorted(zip(chi_so, cuoc.flatten()), key=lambda x: x[1])

    for (i, j), cuoc in sorted_cuoc_phi:
        if cuoc == 0 or thu[j] == 0:
            continue
        else:
            minn = min(phat[i], thu[j])
            if phat[i] == thu[j]:
                X[i, j] = 0
            else:
                X[i, j] = minn
                phat[i] -= minn
                thu[j] -= minn
    for i in range(n):
        for j in range(m):
            if thu[j] != 0 and phat[i] != 0:
                minn = min(phat[i], thu[j])
                X[i, j] = minn
                phat[i] -= minn
                thu[j] -= minn
    return X


def cap_nhat(u, v, khac_0, C):
    for i, j in khac_0:
        if np.isnan(u[i]) and not np.isnan(v[j]):
            u[i] = C[i, j] - v[j]
        elif not np.isnan(u[i]) and np.isnan(v[j]):
            v[j] = C[i, j] - u[i]
        else:
            continue
    return u, v


def tim_chu_trinh(T, bat_dau):
    T[bat_dau] = 1
    while True:
        _xs, _ys = np.nonzero(T)
        xcount, ycount = Counter(_xs), Counter(_ys)
        for x, count in xcount.items():
            if count <= 1:
                T[x, :] = 0
        for y, count in ycount.items():
            if count <= 1:
                T[:, y] = 0
        if all(x > 1 for x in xcount.values()) and all(y > 1 for y in ycount.values()):
            break
    di = lambda kv1, kv2: abs(kv1[0] - kv2[0]) + abs(kv1[1] - kv2[1])
    vien = [tuple(p) for p in np.argwhere(T > 0)]

    size = len(vien)
    path = [bat_dau]
    while len(path) < size:
        l = path[-1]
        if l in vien:
            vien.remove(l)
        n = min(vien, key=lambda x: di(l, (x[0], x[1])))
        path.append(n)
    return path


def find_potential(X, C, loai_tru_suy_bien = None):
    n, m = X.shape

    u = np.array([np.nan] * n)
    v = np.array([np.nan] * m)

    _x, _y = np.where(X > 0)
    none_zero = list(zip(_x, _y))
    f = none_zero[0][0]
    u[f] = 0
    if len(none_zero) == m + n - 1:
        while any(np.isnan(u)) or any(np.isnan(v)):
            u, v = cap_nhat(u, v, none_zero, C)
        return u, v
    else:
        _xx, _yy = np.where(X == 0)
        zero = list(zip(_xx, _yy))
        for a, b in zero:
            if (a, b) not in loai_tru_suy_bien:
                nonzero_temp = none_zero.copy()
                nonzero_temp.append((a, b))
                count = m + n
                u_temp = np.copy(u)
                v_temp = np.copy(v)
                u_temp[f] = 0
                while any(np.isnan(u_temp)) or any(np.isnan(v_temp)) and count > 0:
                    u_temp, v_temp = cap_nhat(u_temp, v_temp, nonzero_temp, C)
                    count = count - 1
                if count > 0:
                    if len(tim_chu_trinh(np.copy(X), (a, b))) != 1:
                        continue
                    else:
                        global suy_bien
                        suy_bien = (a, b)
                        return u_temp, v_temp


n, m = C.shape
X = tim_phuong_an_ban_dau(C=C, T=T, P=P)
loai_tru_suy_bien = []
print("Phương án cơ bản")
while True:
    S = np.zeros((n, m))
    # print(X)
    u, v = find_potential(X=X, C=C, loai_tru_suy_bien=loai_tru_suy_bien)
    in_phuong_an(C=C, T=T, P=P, s="P/T", X=X, u=u, v=v)
    # print(X)
    for i in range(n):
        for j in range(m):
            S[i, j] = C[i, j] - v[j] - u[i]
    s = np.min(S)
    if s >= 0:
        print("Bài toán đã tối ưu")
        break
    i, j = np.argwhere(S == s)[0]
    start = (i, j)
    T_temp = np.copy(X)
    if suy_bien != (-1, -1):
        T_temp[suy_bien] = 1
    path = tim_chu_trinh(T_temp, start)
    print(f"Chu trình:", *path,"\n\n")
    neg = path[1::2]
    pos = path[::2]
    if suy_bien not in neg:
        neg_val = [X[i, j] for i, j in neg]
        q = min(neg_val)
        for i, j in neg:
            X[i, j] -= q
        for i, j in pos:
            X[i, j] += q
    else:
        loai_tru_suy_bien.append(suy_bien)
    suy_bien = (-1, -1)