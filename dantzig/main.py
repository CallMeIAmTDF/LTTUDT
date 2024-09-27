import pandas as pd
from tabulate import tabulate
import numpy as np
import sympy as sp
import settings
yEQEJxPMEDHDwhNlzovVANkEElWFMqnb = 9999999999999999999
WUVtDTBkHsgkhYgKtCLNYfKwuGQOYzHF = sp.symbols('M')
docZAbKWgNnKRDYZqCqduGvELJyiQjGM = settings.A
ueZLOJWgJFJdVBVLhNCMhfgZqQCiUDCC = settings.c
GoxPtAYsJiSRPqetjmchnsPmrqPwAlBL = ["Ẩn chính", 'Chuẩn/Cột', 0]
BdORISeodFbNARBzgpbACulPFdZbWyAf = len(ueZLOJWgJFJdVBVLhNCMhfgZqQCiUDCC)
for WcpgQgbJdKBWIzEitowiqcntkFdKCzus in range(1, BdORISeodFbNARBzgpbACulPFdZbWyAf + 1):
    GoxPtAYsJiSRPqetjmchnsPmrqPwAlBL.append(f"x{WcpgQgbJdKBWIzEitowiqcntkFdKCzus}")
IuusLHxtRaEJkEkvohDMEfpFdxvSCDnT = 1
def YjTiQuzWpEBckTDhWkYZyWvwtCEMdzAS(ma_tran):
    QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY = []
    weWbInzaMkTwpSsBThzRRfHgBSBQMVVD = np.array(ma_tran)
    xYLOFUqXlWCiJGeOFMeFdtSwokCZevcn = []
    for WcpgQgbJdKBWIzEitowiqcntkFdKCzus in range(weWbInzaMkTwpSsBThzRRfHgBSBQMVVD.shape[1]):
        CfoBdnxcEKJJhoUnxtjArQIzJAEwULRn = weWbInzaMkTwpSsBThzRRfHgBSBQMVVD[:, WcpgQgbJdKBWIzEitowiqcntkFdKCzus]
        if np.sum(CfoBdnxcEKJJhoUnxtjArQIzJAEwULRn) == 1 and np.count_nonzero(CfoBdnxcEKJJhoUnxtjArQIzJAEwULRn) == 1:
            xYLOFUqXlWCiJGeOFMeFdtSwokCZevcn.append(WcpgQgbJdKBWIzEitowiqcntkFdKCzus)
    for FmAdolbWKfmSPHJOmekoCwMxIbngaRFl in ma_tran:
        for CfoBdnxcEKJJhoUnxtjArQIzJAEwULRn in xYLOFUqXlWCiJGeOFMeFdtSwokCZevcn:
            if FmAdolbWKfmSPHJOmekoCwMxIbngaRFl[CfoBdnxcEKJJhoUnxtjArQIzJAEwULRn] == 1:
                QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY.append(CfoBdnxcEKJJhoUnxtjArQIzJAEwULRn)
    return QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY
def dFKabqksShhZcHomZrUhrUFsmIaMzlzo(gia_tri_1, gia_tri_2, dau):
    global UtSTFytGLasAqIdeyRKuuoIYRzuRcpiQ
    if dau == '>':
        UtSTFytGLasAqIdeyRKuuoIYRzuRcpiQ = gia_tri_1 > gia_tri_2
    elif dau == '<':
        UtSTFytGLasAqIdeyRKuuoIYRzuRcpiQ = gia_tri_1 < gia_tri_2
    elif dau == '>=':
        UtSTFytGLasAqIdeyRKuuoIYRzuRcpiQ = gia_tri_1 >= gia_tri_2
    elif dau == '<=':
        UtSTFytGLasAqIdeyRKuuoIYRzuRcpiQ = gia_tri_1 <= gia_tri_2
    if (isinstance(gia_tri_1, (sp.core.mul.Mul, sp.core.symbol.Symbol, sp.core.add.Add)) or
            isinstance(gia_tri_2, (sp.core.mul.Mul, sp.core.symbol.Symbol, sp.core.add.Add))):
        return UtSTFytGLasAqIdeyRKuuoIYRzuRcpiQ.subs(WUVtDTBkHsgkhYgKtCLNYfKwuGQOYzHF, yEQEJxPMEDHDwhNlzovVANkEElWFMqnb)
    return UtSTFytGLasAqIdeyRKuuoIYRzuRcpiQ
def GnozIFKopGEpnkPKZBbLySmSFdbHVGMI(array):
    wEwMNBEEQcFJPLqzLYEezcBCsquUYIfF = -yEQEJxPMEDHDwhNlzovVANkEElWFMqnb
    for WcpgQgbJdKBWIzEitowiqcntkFdKCzus in array:
        if dFKabqksShhZcHomZrUhrUFsmIaMzlzo(WcpgQgbJdKBWIzEitowiqcntkFdKCzus, wEwMNBEEQcFJPLqzLYEezcBCsquUYIfF, '>'):
            wEwMNBEEQcFJPLqzLYEezcBCsquUYIfF = WcpgQgbJdKBWIzEitowiqcntkFdKCzus
    return wEwMNBEEQcFJPLqzLYEezcBCsquUYIfF
def KYXMttcsInGvnbffeSaULWendpexXEMw(tWvfUiPeNMqoSPQQzvCoByIDXQAqMfRj, GoxPtAYsJiSRPqetjmchnsPmrqPwAlBL, IuusLHxtRaEJkEkvohDMEfpFdxvSCDnT):
    esPzkmzGzbNWBmQXHUubEhPzpEWMjnIh = pd.DataFrame(tWvfUiPeNMqoSPQQzvCoByIDXQAqMfRj, columns=GoxPtAYsJiSRPqetjmchnsPmrqPwAlBL)
    YNzdTYnWFJwOCrFyjWKIiKUJcwuekEMQ = tabulate(esPzkmzGzbNWBmQXHUubEhPzpEWMjnIh, headers='keys', tablefmt='grid', showindex=False)
    xkeNZndIoxOmMoPrlHExwlUGTBdFUIjK = (len(YNzdTYnWFJwOCrFyjWKIiKUJcwuekEMQ.split('\n')[1]) - len(f"Buoc {IuusLHxtRaEJkEkvohDMEfpFdxvSCDnT}")) // 2
    print("_" * xkeNZndIoxOmMoPrlHExwlUGTBdFUIjK + f"Buoc {IuusLHxtRaEJkEkvohDMEfpFdxvSCDnT}" + "_" * xkeNZndIoxOmMoPrlHExwlUGTBdFUIjK)
    print(YNzdTYnWFJwOCrFyjWKIiKUJcwuekEMQ)
def XOLErJZIMmYrqDbOhDrUfvPIhgMyWwrf(BdORISeodFbNARBzgpbACulPFdZbWyAf, QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY):
    sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO = []
    sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO.extend(['_', '_'])
    for WcpgQgbJdKBWIzEitowiqcntkFdKCzus in range(-1, BdORISeodFbNARBzgpbACulPFdZbWyAf):
        ighTONxNMWsoMOlcTsSsZvAsNriCoyvf = 0
        if WcpgQgbJdKBWIzEitowiqcntkFdKCzus != -1:
            ighTONxNMWsoMOlcTsSsZvAsNriCoyvf = ueZLOJWgJFJdVBVLhNCMhfgZqQCiUDCC[WcpgQgbJdKBWIzEitowiqcntkFdKCzus]
        k = -ighTONxNMWsoMOlcTsSsZvAsNriCoyvf
        for PkSFLNxeqFxNkINroGKYcluNYmMyAxyR in range(len(QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY)):
            k += (ueZLOJWgJFJdVBVLhNCMhfgZqQCiUDCC[QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY[PkSFLNxeqFxNkINroGKYcluNYmMyAxyR] - 1] * docZAbKWgNnKRDYZqCqduGvELJyiQjGM[PkSFLNxeqFxNkINroGKYcluNYmMyAxyR][WcpgQgbJdKBWIzEitowiqcntkFdKCzus + 1])
        sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO.append(k)
    return sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO
while True:
    QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY = YjTiQuzWpEBckTDhWkYZyWvwtCEMdzAS(docZAbKWgNnKRDYZqCqduGvELJyiQjGM)
    tWvfUiPeNMqoSPQQzvCoByIDXQAqMfRj = []
    for WcpgQgbJdKBWIzEitowiqcntkFdKCzus in range(len(QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY)):
        uFnJJuXquZUJTskAVeeDXwobqtHURSTX = QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY[WcpgQgbJdKBWIzEitowiqcntkFdKCzus]
        HvNuTnosZXYjkxvdyeLMOwrxpRCvlYCr = []
        HvNuTnosZXYjkxvdyeLMOwrxpRCvlYCr.extend([f'x{uFnJJuXquZUJTskAVeeDXwobqtHURSTX}', ueZLOJWgJFJdVBVLhNCMhfgZqQCiUDCC[uFnJJuXquZUJTskAVeeDXwobqtHURSTX - 1]])
        HvNuTnosZXYjkxvdyeLMOwrxpRCvlYCr.extend([PkSFLNxeqFxNkINroGKYcluNYmMyAxyR for PkSFLNxeqFxNkINroGKYcluNYmMyAxyR in docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus]])
        tWvfUiPeNMqoSPQQzvCoByIDXQAqMfRj.append(HvNuTnosZXYjkxvdyeLMOwrxpRCvlYCr)
    sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO = XOLErJZIMmYrqDbOhDrUfvPIhgMyWwrf(BdORISeodFbNARBzgpbACulPFdZbWyAf=BdORISeodFbNARBzgpbACulPFdZbWyAf, QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY=QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY)
    tWvfUiPeNMqoSPQQzvCoByIDXQAqMfRj.append(sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO)
    KYXMttcsInGvnbffeSaULWendpexXEMw(tWvfUiPeNMqoSPQQzvCoByIDXQAqMfRj=tWvfUiPeNMqoSPQQzvCoByIDXQAqMfRj, GoxPtAYsJiSRPqetjmchnsPmrqPwAlBL=GoxPtAYsJiSRPqetjmchnsPmrqPwAlBL, IuusLHxtRaEJkEkvohDMEfpFdxvSCDnT=IuusLHxtRaEJkEkvohDMEfpFdxvSCDnT)
    IuusLHxtRaEJkEkvohDMEfpFdxvSCDnT += 1
    otYxedPHOaPkYpihniGcgCGSdmlNLzkI = GnozIFKopGEpnkPKZBbLySmSFdbHVGMI(sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO[3:])
    if dFKabqksShhZcHomZrUhrUFsmIaMzlzo(gia_tri_1=otYxedPHOaPkYpihniGcgCGSdmlNLzkI, gia_tri_2=0, dau='<='):
        print(f"Bài toán tối ưu: ")
        print(f"    giá trị = {sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO[2]}")
        for WcpgQgbJdKBWIzEitowiqcntkFdKCzus in range(len(QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY)):
            print(f"    x{QaeFzCQvUuMlLOFMQEpJxHKcfdIjireY[WcpgQgbJdKBWIzEitowiqcntkFdKCzus]} = {docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus][0]}")
        break
    nMKVdVNyAScCYgkMFMfFvBDjxtfKYWiK = sYUfNmTqvOSDeWTPIzROFlQqrNQMmrcO[2:].index(otYxedPHOaPkYpihniGcgCGSdmlNLzkI)
    ZeFpRxNjUqEnTiKubPoXVRrjFwSXnMFW = -1
    VytlJOIWiWwTAxRjFekrbnaLtevPHpoe = yEQEJxPMEDHDwhNlzovVANkEElWFMqnb
    for WcpgQgbJdKBWIzEitowiqcntkFdKCzus in range(len(docZAbKWgNnKRDYZqCqduGvELJyiQjGM)):
        HYzTUPzHRLlZLLKdSOyKEmzdItUvbiqy = docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus][0] / docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus][nMKVdVNyAScCYgkMFMfFvBDjxtfKYWiK]
        if docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus][nMKVdVNyAScCYgkMFMfFvBDjxtfKYWiK] > 0 and VytlJOIWiWwTAxRjFekrbnaLtevPHpoe > HYzTUPzHRLlZLLKdSOyKEmzdItUvbiqy > 0:
            ZeFpRxNjUqEnTiKubPoXVRrjFwSXnMFW = WcpgQgbJdKBWIzEitowiqcntkFdKCzus
            VytlJOIWiWwTAxRjFekrbnaLtevPHpoe = HYzTUPzHRLlZLLKdSOyKEmzdItUvbiqy
    if VytlJOIWiWwTAxRjFekrbnaLtevPHpoe == yEQEJxPMEDHDwhNlzovVANkEElWFMqnb:
        print("Bài toán tối ưu vô nghiệm, giá trị tiến đến -\u221E")
        break
    kAAcVIslJQdqgNewfGOiAbOOJvYzbMWq = docZAbKWgNnKRDYZqCqduGvELJyiQjGM[ZeFpRxNjUqEnTiKubPoXVRrjFwSXnMFW][nMKVdVNyAScCYgkMFMfFvBDjxtfKYWiK]
    for PkSFLNxeqFxNkINroGKYcluNYmMyAxyR in range(len(docZAbKWgNnKRDYZqCqduGvELJyiQjGM[ZeFpRxNjUqEnTiKubPoXVRrjFwSXnMFW])):
        docZAbKWgNnKRDYZqCqduGvELJyiQjGM[ZeFpRxNjUqEnTiKubPoXVRrjFwSXnMFW][PkSFLNxeqFxNkINroGKYcluNYmMyAxyR] /= kAAcVIslJQdqgNewfGOiAbOOJvYzbMWq
    for WcpgQgbJdKBWIzEitowiqcntkFdKCzus in range(len(docZAbKWgNnKRDYZqCqduGvELJyiQjGM)):
        if WcpgQgbJdKBWIzEitowiqcntkFdKCzus != ZeFpRxNjUqEnTiKubPoXVRrjFwSXnMFW:
            wMENPRheoKEHAoHFSxlKgJtNESXINlrD = docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus][nMKVdVNyAScCYgkMFMfFvBDjxtfKYWiK]
            for PkSFLNxeqFxNkINroGKYcluNYmMyAxyR in range(len(docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus])):
                docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus][PkSFLNxeqFxNkINroGKYcluNYmMyAxyR] = docZAbKWgNnKRDYZqCqduGvELJyiQjGM[WcpgQgbJdKBWIzEitowiqcntkFdKCzus][PkSFLNxeqFxNkINroGKYcluNYmMyAxyR] - docZAbKWgNnKRDYZqCqduGvELJyiQjGM[ZeFpRxNjUqEnTiKubPoXVRrjFwSXnMFW][PkSFLNxeqFxNkINroGKYcluNYmMyAxyR] * wMENPRheoKEHAoHFSxlKgJtNESXINlrD
