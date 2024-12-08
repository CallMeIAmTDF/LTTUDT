import pandas as pd
from tabulate import tabulate
import numpy as np
import sympy as sp
import settings

inf = 9999999999999999999
M = sp.symbols('M')
A = settings.A
c = settings.c
"""tạo header cho bảng"""
tieu_de = ["Ẩn chính", 'Chuẩn/Cột', 0]
so_nghiem = len(c)
for i in range(1, so_nghiem + 1):
    tieu_de.append(f"x{i}")
buoc = 1

def tim_an_chinh(ma_tran):
    an_chinh = []
    ma_tran_tam_thoi = np.array(ma_tran)
    cot_don_vi = []
    for i in range(ma_tran_tam_thoi.shape[1]):
        cot = ma_tran_tam_thoi[:, i]
        if np.sum(cot) == 1 and np.count_nonzero(cot) == 1:
            cot_don_vi.append(i)
    for hang in ma_tran:
        for cot in cot_don_vi:
            if hang[cot] == 1:
                an_chinh.append(cot)
    return an_chinh


def so_sanh(gia_tri_1, gia_tri_2, dau):
    """
    :param gia_tri_1:
    :param gia_tri_2:
    :param dau:
    :return:
    """
    global bieuthuc
    if dau == '>':
        bieuthuc = gia_tri_1 > gia_tri_2
    elif dau == '<':
        bieuthuc = gia_tri_1 < gia_tri_2
    elif dau == '>=':
        bieuthuc = gia_tri_1 >= gia_tri_2
    elif dau == '<=':
        bieuthuc = gia_tri_1 <= gia_tri_2
    if (isinstance(gia_tri_1, (sp.core.mul.Mul, sp.core.symbol.Symbol, sp.core.add.Add)) or
            isinstance(gia_tri_2, (sp.core.mul.Mul, sp.core.symbol.Symbol, sp.core.add.Add))):
        return bieuthuc.subs(M, inf)
    return bieuthuc


def tim_gia_tri_lon_nhat(array):
    lon_nhat = -inf
    for i in array:
        if so_sanh(i, lon_nhat, '>'):
            lon_nhat = i
    return lon_nhat


def in_ket_qua(du_lieu, tieu_de, buoc):
    df = pd.DataFrame(du_lieu, columns=tieu_de)
    table = tabulate(df, headers='keys', tablefmt='grid', showindex=False)
    _len = (len(table.split('\n')[1]) - len(f"Buoc {buoc}")) // 2
    print("_" * _len + f"Buoc {buoc}" + "_" * _len)
    print(table)

def tinh_ket_qua(so_nghiem, an_chinh):
    kq = []
    kq.extend(['_', '_'])
    for i in range(-1, so_nghiem):
        chuan_cot = 0  # cột đầu(kết quả ràng buộc) thì = 0
        if i != -1:
            chuan_cot = c[i]  # cột sau thì = hệ số
        k = -chuan_cot  # phải - đi
        for j in range(len(an_chinh)):
            k += (c[an_chinh[j] - 1] * A[j][i + 1])  # tính kết quả
        kq.append(k)
    return kq



while True:
    an_chinh = tim_an_chinh(A) # Lấy danh sách ẩn chính

    """tạo dòng ẩn chính"""
    du_lieu = []
    for i in range(len(an_chinh)):
        x = an_chinh[i]
        row = []
        row.extend([f'x{x}', c[x - 1]])                                             # chuẩn
        row.extend([j for j in A[i]])                                               # giá trị hệ số của phương trình ràng buộc tương ứng
        du_lieu.append(row)

    """tạo dòng kết quả"""
    kq = tinh_ket_qua(so_nghiem=so_nghiem, an_chinh=an_chinh)
    du_lieu.append(kq)

    """In"""
    in_ket_qua(du_lieu=du_lieu, tieu_de=tieu_de, buoc=buoc)
    buoc += 1

    """ Tìm max của kết quả """
    m = tim_gia_tri_lon_nhat(kq[3:])
    # m = 1
    if so_sanh(gia_tri_1=m, gia_tri_2=0, dau='<='):
        print(f"Bài toán tối ưu: ")
        print(f"    giá trị = {kq[2]}")
        for i in range(len(an_chinh)):
            print(f"    x{an_chinh[i]} = {A[i][0]}")
        break # thoát nếu các giá trị đều <= 0

    an_moi = kq[2:].index(m) # vị trí của ẩn mới

    # tìm vị trí ẩn thay thế
    vi_tri_the = -1
    gia_tri_nho_nhat = inf
    for i in range(len(A)):
        gia_tri = A[i][0] / A[i][an_moi]
        if A[i][an_moi] > 0 and gia_tri_nho_nhat > gia_tri > 0:
            vi_tri_the = i
            gia_tri_nho_nhat = gia_tri
    if gia_tri_nho_nhat == inf: # nếu không tìm thấy aij > 0:
        print("Bài toán tối ưu vô nghiệm, giá trị tiến đến -\u221E")
        break

    g = A[vi_tri_the][an_moi] # giá trị chia
    for j in range(len(A[vi_tri_the])):
        A[vi_tri_the][j] /= g # chia dòng ẩn chính mới
    for i in range(len(A)):
        if i != vi_tri_the:
            ajr = A[i][an_moi]
            for j in range(len(A[i])):
                A[i][j] = A[i][j] - A[vi_tri_the][j] * ajr # cập nhật các dòng ẩn chính khác