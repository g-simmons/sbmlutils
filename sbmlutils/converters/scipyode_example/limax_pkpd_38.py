"""
limax_pkpd_38
"""
import numpy as np


xids = ["Aar_apap", "Aar_co2c13", "Aar_metc13", "Abo_apap", "Abo_co2c13", "Abo_co2c13_fix", "Abo_metc13", "Abreath_co2c13", "Agu_apap", "Agu_co2c13", "Agu_metc13", "Ahe_apap", "Ahe_co2c13", "Ahe_metc13", "Aki_apap", "Aki_co2c13", "Aki_metc13", "Ali_apap", "Ali_co2c13", "Ali_metc13", "Alu_apap", "Alu_co2c13", "Alu_metc13", "Are_apap", "Are_co2c13", "Are_metc13", "Asp_apap", "Asp_co2c13", "Asp_metc13", "Aurine_apap", "Aurine_co2c13", "Aurine_metc13", "Ave_apap", "Ave_co2c13", "Ave_metc13", "DIV_apap", "DIV_co2c13", "DIV_metc13", "D_apap", "D_co2c13", "D_metc13", "cum_dose_apap", "cum_dose_co2c13", "cum_dose_metc13", ]
pids = ["APAPD_HLM_CL", "APAPD_Km_apap", "BP_apap", "BP_co2c13", "BP_metc13", "BW", "CLrenal_apap", "CLrenal_co2c13", "CLrenal_metc13", "CO2FIX_HLM_CL", "CO2FIX_Km_co2", "COBW", "COHRI", "CYP1A2MET_CL", "CYP1A2MET_Km_met", "FQbo", "FQgu", "FQh", "FQhe", "FQki", "FQlu", "FQsp", "FVar", "FVbo", "FVgu", "FVhe", "FVki", "FVli", "FVlu", "FVpl", "FVsp", "FVve", "F_PAR", "F_apap", "F_co2c13", "F_metc13", "HEIGHT", "HR", "HRrest", "IVDOSE_apap", "IVDOSE_co2c13", "IVDOSE_metc13", "KBO_FIXCO2", "KBO_MAXCO2", "KBO_RELCO2", "KLU_EXCO2", "Ka_apap", "Ka_co2c13", "Ka_metc13", "Kpbo_apap", "Kpbo_co2c13", "Kpbo_metc13", "Kpgu_apap", "Kpgu_co2c13", "Kpgu_metc13", "Kphe_apap", "Kphe_co2c13", "Kphe_metc13", "Kpki_apap", "Kpki_co2c13", "Kpki_metc13", "Kpli_apap", "Kpli_co2c13", "Kpli_metc13", "Kplu_apap", "Kplu_co2c13", "Kplu_metc13", "Kpre_apap", "Kpre_co2c13", "Kpre_metc13", "Kpsp_apap", "Kpsp_co2c13", "Kpsp_metc13", "MPPGL", "Mr_apap", "Mr_co2c13", "Mr_metc13", "PODOSE_apap", "PODOSE_co2c13", "PODOSE_metc13", "P_CO2BSA", "R_PDB", "Ri_apap", "Ri_co2c13", "Ri_metc13", "fumic_apap", "fumic_co2c13", "fumic_metc13", "fup_apap", "fup_co2c13", "fup_metc13", "ti_apap", "ti_co2c13", "ti_metc13", ]
yids = ["BSA", "CO", "FQre", "FVre", "Ki_apap", "Ki_co2c13", "Ki_metc13", "Var", "Vbo", "Vgu", "Vhe", "Vki", "Vli", "Vlu", "Vpl", "Vsp", "Vve", "Xar_apap", "Xar_co2c13", "Xar_metc13", "Xbo_apap", "Xbo_co2c13", "Xbo_co2c13_fix", "Xbo_metc13", "Xbreath_co2c13", "Xgu_apap", "Xgu_co2c13", "Xgu_metc13", "Xhe_apap", "Xhe_co2c13", "Xhe_metc13", "Xki_apap", "Xki_co2c13", "Xki_metc13", "Xli_apap", "Xli_co2c13", "Xli_metc13", "Xlu_apap", "Xlu_co2c13", "Xlu_metc13", "Xre_apap", "Xre_co2c13", "Xre_metc13", "Xsp_apap", "Xsp_co2c13", "Xsp_metc13", "Xurine_apap", "Xurine_co2c13", "Xurine_metc13", "Xve_apap", "Xve_co2c13", "Xve_metc13", "APAPD_CLliv", "CO2FIX_CLliv", "CYP1A2MET_CLliv", "Car_apap", "Car_co2c13", "Car_metc13", "Cbo_apap", "Cbo_co2c13", "Cbo_co2c13_fix", "Cbo_metc13", "Cgu_apap", "Cgu_co2c13", "Cgu_metc13", "Che_apap", "Che_co2c13", "Che_metc13", "Cki_apap", "Cki_co2c13", "Cki_metc13", "Cli_apap", "Cli_co2c13", "Cli_metc13", "Clu_apap", "Clu_co2c13", "Clu_metc13", "Csp_apap", "Csp_co2c13", "Csp_metc13", "Cve_apap", "Cve_co2c13", "Cve_metc13", "Mar_apap", "Mar_co2c13", "Mar_metc13", "Mbo_apap", "Mbo_co2c13", "Mbo_metc13", "Mgu_apap", "Mgu_co2c13", "Mgu_metc13", "Mhe_apap", "Mhe_co2c13", "Mhe_metc13", "Mki_apap", "Mki_co2c13", "Mki_metc13", "Mli_apap", "Mli_co2c13", "Mli_metc13", "Mlu_apap", "Mlu_co2c13", "Mlu_metc13", "Msp_apap", "Msp_co2c13", "Msp_metc13", "Mve_apap", "Mve_co2c13", "Mve_metc13", "P_CO2", "QC", "Vplas_art", "Vplas_ven", "Vre", "Xbody_apap", "Xbody_co2c13", "Xbody_metc13", "Cki_free_apap", "Cki_free_co2c13", "Cki_free_metc13", "Cli_free_apap", "Cli_free_co2c13", "Cli_free_metc13", "Cpl_ve_apap", "Cpl_ve_co2c13", "Cpl_ve_metc13", "Cre_apap", "Cre_co2c13", "Cre_metc13", "Mre_apap", "Mre_co2c13", "Mre_metc13", "P_CO2c12", "P_CO2c13", "Qbo", "Qgu", "Qh", "Qhe", "Qki", "Qlu", "Qre", "Qsp", "DOB", "P_CO2Fc13", "P_CO2R", "Qha", ]

x0 = [
    0.0,		# Aar_apap [0]
    0.0,		# Aar_co2c13 [1]
    0.0,		# Aar_metc13 [2]
    0.0,		# Abo_apap [3]
    0.0,		# Abo_co2c13 [4]
    0.0,		# Abo_co2c13_fix [5]
    0.0,		# Abo_metc13 [6]
    0.0,		# Abreath_co2c13 [7]
    0.0,		# Agu_apap [8]
    0.0,		# Agu_co2c13 [9]
    0.0,		# Agu_metc13 [10]
    0.0,		# Ahe_apap [11]
    0.0,		# Ahe_co2c13 [12]
    0.0,		# Ahe_metc13 [13]
    0.0,		# Aki_apap [14]
    0.0,		# Aki_co2c13 [15]
    0.0,		# Aki_metc13 [16]
    0.0,		# Ali_apap [17]
    0.0,		# Ali_co2c13 [18]
    0.0,		# Ali_metc13 [19]
    0.0,		# Alu_apap [20]
    0.0,		# Alu_co2c13 [21]
    0.0,		# Alu_metc13 [22]
    0.0,		# Are_apap [23]
    0.0,		# Are_co2c13 [24]
    0.0,		# Are_metc13 [25]
    0.0,		# Asp_apap [26]
    0.0,		# Asp_co2c13 [27]
    0.0,		# Asp_metc13 [28]
    0.0,		# Aurine_apap [29]
    0.0,		# Aurine_co2c13 [30]
    0.0,		# Aurine_metc13 [31]
    0.0,		# Ave_apap [32]
    0.0,		# Ave_co2c13 [33]
    0.0,		# Ave_metc13 [34]
    0.0,		# DIV_apap [35]
    0.0,		# DIV_co2c13 [36]
    0.0,		# DIV_metc13 [37]
    0.0,		# D_apap [38]
    0.0,		# D_co2c13 [39]
    0.0,		# D_metc13 [40]
    0.0,		# cum_dose_apap [41]
    0.0,		# cum_dose_co2c13 [42]
    0.0,		# cum_dose_metc13 [43]
]

p = [
    2.5,		# APAPD_HLM_CL [0]
    0.5,		# APAPD_Km_apap [1]
    1.0,		# BP_apap [2]
    1.0,		# BP_co2c13 [3]
    1.0,		# BP_metc13 [4]
    75.0,		# BW [5]
    0.714,		# CLrenal_apap [6]
    0.0,		# CLrenal_co2c13 [7]
    10.0,		# CLrenal_metc13 [8]
    1.5,		# CO2FIX_HLM_CL [9]
    0.2,		# CO2FIX_Km_co2 [10]
    1.548,		# COBW [11]
    150.0,		# COHRI [12]
    1.5,		# CYP1A2MET_CL [13]
    0.02,		# CYP1A2MET_Km_met [14]
    0.05,		# FQbo [15]
    0.146,		# FQgu [16]
    0.215,		# FQh [17]
    0.04,		# FQhe [18]
    0.19,		# FQki [19]
    1.0,		# FQlu [20]
    0.017,		# FQsp [21]
    0.0257,		# FVar [22]
    0.0856,		# FVbo [23]
    0.0171,		# FVgu [24]
    0.0047,		# FVhe [25]
    0.0044,		# FVki [26]
    0.021,		# FVli [27]
    0.0076,		# FVlu [28]
    0.0424,		# FVpl [29]
    0.0026,		# FVsp [30]
    0.0514,		# FVve [31]
    0.85,		# F_PAR [32]
    0.87,		# F_apap [33]
    1.0,		# F_co2c13 [34]
    1.0,		# F_metc13 [35]
    170.0,		# HEIGHT [36]
    70.0,		# HR [37]
    70.0,		# HRrest [38]
    0.0,		# IVDOSE_apap [39]
    0.0,		# IVDOSE_co2c13 [40]
    0.0,		# IVDOSE_metc13 [41]
    0.1,		# KBO_FIXCO2 [42]
    0.2,		# KBO_MAXCO2 [43]
    0.0001,		# KBO_RELCO2 [44]
    1.2,		# KLU_EXCO2 [45]
    2.5,		# Ka_apap [46]
    8.0,		# Ka_co2c13 [47]
    4.0,		# Ka_metc13 [48]
    1.0,		# Kpbo_apap [49]
    1.0,		# Kpbo_co2c13 [50]
    1.0,		# Kpbo_metc13 [51]
    1.0,		# Kpgu_apap [52]
    1.0,		# Kpgu_co2c13 [53]
    1.0,		# Kpgu_metc13 [54]
    1.0,		# Kphe_apap [55]
    1.0,		# Kphe_co2c13 [56]
    1.0,		# Kphe_metc13 [57]
    1.0,		# Kpki_apap [58]
    1.0,		# Kpki_co2c13 [59]
    1.0,		# Kpki_metc13 [60]
    1.0,		# Kpli_apap [61]
    1.0,		# Kpli_co2c13 [62]
    1.0,		# Kpli_metc13 [63]
    1.0,		# Kplu_apap [64]
    1.0,		# Kplu_co2c13 [65]
    1.0,		# Kplu_metc13 [66]
    0.8,		# Kpre_apap [67]
    1.0,		# Kpre_co2c13 [68]
    0.2,		# Kpre_metc13 [69]
    1.0,		# Kpsp_apap [70]
    1.0,		# Kpsp_co2c13 [71]
    1.0,		# Kpsp_metc13 [72]
    45.0,		# MPPGL [73]
    151.16,		# Mr_apap [74]
    62.02,		# Mr_co2c13 [75]
    165.19,		# Mr_metc13 [76]
    0.0,		# PODOSE_apap [77]
    0.0,		# PODOSE_co2c13 [78]
    0.0,		# PODOSE_metc13 [79]
    300.0,		# P_CO2BSA [80]
    0.01123,		# R_PDB [81]
    0.0,		# Ri_apap [82]
    0.0,		# Ri_co2c13 [83]
    0.0,		# Ri_metc13 [84]
    1.0,		# fumic_apap [85]
    1.0,		# fumic_co2c13 [86]
    1.0,		# fumic_metc13 [87]
    1.0,		# fup_apap [88]
    1.0,		# fup_co2c13 [89]
    1.0,		# fup_metc13 [90]
    10.0,		# ti_apap [91]
    10.0,		# ti_co2c13 [92]
    10.0,		# ti_metc13 [93]
]

def f_dxdt(x, t, p):
    """ ODE system """
    y = np.zeros(shape=(147, 1))
    y[0] = 0.024265 * (p[5] / 1)**0.5378 * (p[36] / 1)**0.3964,		# BSA [0]
    y[1] = p[5] * p[11] + (p[37] - p[38]) * p[12] / 60,		# CO [1]
    y[2] = 1 - (p[15] + p[18] + p[16] + p[19] + p[17] + p[21]),		# FQre [2]
    y[3] = 1 - (p[23] + p[25] + p[24] + p[26] + p[27] + p[28] + p[30] + p[31] + p[22] + p[29]),		# FVre [3]
    y[4] = (1.386 / p[91]) * 3600,		# Ki_apap [4]
    y[5] = (1.386 / p[92]) * 3600,		# Ki_co2c13 [5]
    y[6] = (1.386 / p[93]) * 3600,		# Ki_metc13 [6]
    y[7] = p[5] * p[22],		# Var [7]
    y[8] = p[5] * p[23],		# Vbo [8]
    y[9] = p[5] * p[24],		# Vgu [9]
    y[10] = p[5] * p[25],		# Vhe [10]
    y[11] = p[5] * p[26],		# Vki [11]
    y[12] = p[5] * p[27],		# Vli [12]
    y[13] = p[5] * p[28],		# Vlu [13]
    y[14] = p[5] * p[29],		# Vpl [14]
    y[15] = p[5] * p[30],		# Vsp [15]
    y[16] = p[5] * p[31],		# Vve [16]
    y[17] = x[0] * p[74],		# Xar_apap [17]
    y[18] = x[1] * p[75],		# Xar_co2c13 [18]
    y[19] = x[2] * p[76],		# Xar_metc13 [19]
    y[20] = x[3] * p[74],		# Xbo_apap [20]
    y[21] = x[4] * p[75],		# Xbo_co2c13 [21]
    y[22] = x[5] * p[75],		# Xbo_co2c13_fix [22]
    y[23] = x[6] * p[76],		# Xbo_metc13 [23]
    y[24] = x[7] * p[75],		# Xbreath_co2c13 [24]
    y[25] = x[8] * p[74],		# Xgu_apap [25]
    y[26] = x[9] * p[75],		# Xgu_co2c13 [26]
    y[27] = x[10] * p[76],		# Xgu_metc13 [27]
    y[28] = x[11] * p[74],		# Xhe_apap [28]
    y[29] = x[12] * p[75],		# Xhe_co2c13 [29]
    y[30] = x[13] * p[76],		# Xhe_metc13 [30]
    y[31] = x[14] * p[74],		# Xki_apap [31]
    y[32] = x[15] * p[75],		# Xki_co2c13 [32]
    y[33] = x[16] * p[76],		# Xki_metc13 [33]
    y[34] = x[17] * p[74],		# Xli_apap [34]
    y[35] = x[18] * p[75],		# Xli_co2c13 [35]
    y[36] = x[19] * p[76],		# Xli_metc13 [36]
    y[37] = x[20] * p[74],		# Xlu_apap [37]
    y[38] = x[21] * p[75],		# Xlu_co2c13 [38]
    y[39] = x[22] * p[76],		# Xlu_metc13 [39]
    y[40] = x[23] * p[74],		# Xre_apap [40]
    y[41] = x[24] * p[75],		# Xre_co2c13 [41]
    y[42] = x[25] * p[76],		# Xre_metc13 [42]
    y[43] = x[26] * p[74],		# Xsp_apap [43]
    y[44] = x[27] * p[75],		# Xsp_co2c13 [44]
    y[45] = x[28] * p[76],		# Xsp_metc13 [45]
    y[46] = x[29] * p[74],		# Xurine_apap [46]
    y[47] = x[30] * p[75],		# Xurine_co2c13 [47]
    y[48] = x[31] * p[76],		# Xurine_metc13 [48]
    y[49] = x[32] * p[74],		# Xve_apap [49]
    y[50] = x[33] * p[75],		# Xve_co2c13 [50]
    y[51] = x[34] * p[76],		# Xve_metc13 [51]
    y[52] = (p[0] / p[85]) * p[73] * y[12] * p[32] * 60 / 1000,		# APAPD_CLliv [52]
    y[53] = p[9] * p[73] * y[12] * p[32] * 60 / 1000,		# CO2FIX_CLliv [53]
    y[54] = (p[13] / p[87]) * p[73] * y[12] * p[32] * 60 / 1000,		# CYP1A2MET_CLliv [54]
    y[55] = x[0] / y[7],		# Car_apap [55]
    y[56] = x[1] / y[7],		# Car_co2c13 [56]
    y[57] = x[2] / y[7],		# Car_metc13 [57]
    y[58] = x[3] / y[8],		# Cbo_apap [58]
    y[59] = x[4] / y[8],		# Cbo_co2c13 [59]
    y[60] = x[5] / y[8],		# Cbo_co2c13_fix [60]
    y[61] = x[6] / y[8],		# Cbo_metc13 [61]
    y[62] = x[8] / y[9],		# Cgu_apap [62]
    y[63] = x[9] / y[9],		# Cgu_co2c13 [63]
    y[64] = x[10] / y[9],		# Cgu_metc13 [64]
    y[65] = x[11] / y[10],		# Che_apap [65]
    y[66] = x[12] / y[10],		# Che_co2c13 [66]
    y[67] = x[13] / y[10],		# Che_metc13 [67]
    y[68] = x[14] / y[11],		# Cki_apap [68]
    y[69] = x[15] / y[11],		# Cki_co2c13 [69]
    y[70] = x[16] / y[11],		# Cki_metc13 [70]
    y[71] = x[17] / y[12],		# Cli_apap [71]
    y[72] = x[18] / y[12],		# Cli_co2c13 [72]
    y[73] = x[19] / y[12],		# Cli_metc13 [73]
    y[74] = x[20] / y[13],		# Clu_apap [74]
    y[75] = x[21] / y[13],		# Clu_co2c13 [75]
    y[76] = x[22] / y[13],		# Clu_metc13 [76]
    y[77] = x[26] / y[15],		# Csp_apap [77]
    y[78] = x[27] / y[15],		# Csp_co2c13 [78]
    y[79] = x[28] / y[15],		# Csp_metc13 [79]
    y[80] = x[32] / y[16],		# Cve_apap [80]
    y[81] = x[33] / y[16],		# Cve_co2c13 [81]
    y[82] = x[34] / y[16],		# Cve_metc13 [82]
    y[83] = (x[0] / y[7]) * p[74],		# Mar_apap [83]
    y[84] = (x[1] / y[7]) * p[75],		# Mar_co2c13 [84]
    y[85] = (x[2] / y[7]) * p[76],		# Mar_metc13 [85]
    y[86] = (x[3] / y[8]) * p[74],		# Mbo_apap [86]
    y[87] = (x[4] / y[8]) * p[75],		# Mbo_co2c13 [87]
    y[88] = (x[6] / y[8]) * p[76],		# Mbo_metc13 [88]
    y[89] = (x[8] / y[9]) * p[74],		# Mgu_apap [89]
    y[90] = (x[9] / y[9]) * p[75],		# Mgu_co2c13 [90]
    y[91] = (x[10] / y[9]) * p[76],		# Mgu_metc13 [91]
    y[92] = (x[11] / y[10]) * p[74],		# Mhe_apap [92]
    y[93] = (x[12] / y[10]) * p[75],		# Mhe_co2c13 [93]
    y[94] = (x[13] / y[10]) * p[76],		# Mhe_metc13 [94]
    y[95] = (x[14] / y[11]) * p[74],		# Mki_apap [95]
    y[96] = (x[15] / y[11]) * p[75],		# Mki_co2c13 [96]
    y[97] = (x[16] / y[11]) * p[76],		# Mki_metc13 [97]
    y[98] = (x[17] / y[12]) * p[74],		# Mli_apap [98]
    y[99] = (x[18] / y[12]) * p[75],		# Mli_co2c13 [99]
    y[100] = (x[19] / y[12]) * p[76],		# Mli_metc13 [100]
    y[101] = (x[20] / y[13]) * p[74],		# Mlu_apap [101]
    y[102] = (x[21] / y[13]) * p[75],		# Mlu_co2c13 [102]
    y[103] = (x[22] / y[13]) * p[76],		# Mlu_metc13 [103]
    y[104] = (x[26] / y[15]) * p[74],		# Msp_apap [104]
    y[105] = (x[27] / y[15]) * p[75],		# Msp_co2c13 [105]
    y[106] = (x[28] / y[15]) * p[76],		# Msp_metc13 [106]
    y[107] = (x[32] / y[16]) * p[74],		# Mve_apap [107]
    y[108] = (x[33] / y[16]) * p[75],		# Mve_co2c13 [108]
    y[109] = (x[34] / y[16]) * p[76],		# Mve_metc13 [109]
    y[110] = y[0] * p[80] / 60,		# P_CO2 [110]
    y[111] = (y[1] / 1000) * 3600,		# QC [111]
    y[112] = y[14] * y[7] / (y[16] + y[7]),		# Vplas_art [112]
    y[113] = y[14] * y[16] / (y[16] + y[7]),		# Vplas_ven [113]
    y[114] = p[5] * y[3],		# Vre [114]
    y[115] = y[17] + y[20] + y[28] + y[25] + y[31] + y[34] + y[37] + y[43] + y[40] + y[49],		# Xbody_apap [115]
    y[116] = y[18] + y[21] + y[29] + y[26] + y[32] + y[35] + y[38] + y[44] + y[41] + y[50],		# Xbody_co2c13 [116]
    y[117] = y[19] + y[23] + y[30] + y[27] + y[33] + y[36] + y[39] + y[45] + y[42] + y[51],		# Xbody_metc13 [117]
    y[118] = y[68] * p[88],		# Cki_free_apap [118]
    y[119] = y[69] * p[89],		# Cki_free_co2c13 [119]
    y[120] = y[70] * p[90],		# Cki_free_metc13 [120]
    y[121] = y[71] * p[88],		# Cli_free_apap [121]
    y[122] = y[72] * p[89],		# Cli_free_co2c13 [122]
    y[123] = y[73] * p[90],		# Cli_free_metc13 [123]
    y[124] = y[80] / p[2],		# Cpl_ve_apap [124]
    y[125] = y[81] / p[3],		# Cpl_ve_co2c13 [125]
    y[126] = y[82] / p[4],		# Cpl_ve_metc13 [126]
    y[127] = x[23] / y[114],		# Cre_apap [127]
    y[128] = x[24] / y[114],		# Cre_co2c13 [128]
    y[129] = x[25] / y[114],		# Cre_metc13 [129]
    y[130] = (x[23] / y[114]) * p[74],		# Mre_apap [130]
    y[131] = (x[24] / y[114]) * p[75],		# Mre_co2c13 [131]
    y[132] = (x[25] / y[114]) * p[76],		# Mre_metc13 [132]
    y[133] = (1 / (1 + p[81])) * y[110],		# P_CO2c12 [133]
    y[134] = (p[81] / (1 + p[81])) * y[110] + Exhalation_co2c13 / 60,		# P_CO2c13 [134]
    y[135] = y[111] * p[15],		# Qbo [135]
    y[136] = y[111] * p[16],		# Qgu [136]
    y[137] = y[111] * p[17],		# Qh [137]
    y[138] = y[111] * p[18],		# Qhe [138]
    y[139] = y[111] * p[19],		# Qki [139]
    y[140] = y[111] * p[20],		# Qlu [140]
    y[141] = y[111] * y[2],		# Qre [141]
    y[142] = y[111] * p[21],		# Qsp [142]
    y[143] = ((y[134] / y[133] - p[81]) / p[81]) * 1000,		# DOB [143]
    y[144] = y[134] / (y[133] + y[134]),		# P_CO2Fc13 [144]
    y[145] = y[134] / y[133],		# P_CO2R [145]
    y[146] = y[137] - y[136] - y[142],		# Qha [146]


    # reactions
    APAPD = y[52] * 1 * (y[121] / (y[121] + p[1]))
    Absorption_apap = (p[46] * x[38] / p[74]) * p[33]
    Absorption_co2c13 = (p[47] * x[39] / p[75]) * p[34]
    Absorption_metc13 = (p[48] * x[40] / p[76]) * p[35]
    CO2FIX = y[53] * 1 * (y[72] / (y[72] + p[10]))
    CYP1A2MET = y[54] * 1 * (y[123] / (y[123] + p[14]))
    Exhalation_co2c13 = p[45] * 60 * y[75] * y[13]
    Fixation_co2c13 = p[42] * 60 * y[81] * y[16] * (1 - y[60] / p[43])
    Infusion_apap = (p[82] / p[74]) * 60
    Infusion_co2c13 = (p[83] / p[75]) * 60
    Infusion_metc13 = (p[84] / p[76]) * 60
    Injection_apap = y[4] * x[35] / p[74]
    Injection_co2c13 = y[5] * x[36] / p[75]
    Injection_metc13 = y[6] * x[37] / p[76]
    Release_co2c13 = p[44] * 60 * y[60] * y[16]
    ar_bo_apap = y[135] * y[55]
    ar_bo_co2c13 = y[135] * y[56]
    ar_bo_metc13 = y[135] * y[57]
    ar_gu_apap = y[136] * y[55]
    ar_gu_co2c13 = y[136] * y[56]
    ar_gu_metc13 = y[136] * y[57]
    ar_he_apap = y[138] * y[55]
    ar_he_co2c13 = y[138] * y[56]
    ar_he_metc13 = y[138] * y[57]
    ar_ki_apap = y[139] * y[55]
    ar_ki_co2c13 = y[139] * y[56]
    ar_ki_metc13 = y[139] * y[57]
    ar_li_apap = y[146] * y[55]
    ar_li_co2c13 = y[146] * y[56]
    ar_li_metc13 = y[146] * y[57]
    ar_re_apap = y[141] * y[55]
    ar_re_co2c13 = y[141] * y[56]
    ar_re_metc13 = y[141] * y[57]
    ar_sp_apap = y[142] * y[55]
    ar_sp_co2c13 = y[142] * y[56]
    ar_sp_metc13 = y[142] * y[57]
    bo_ve_apap = y[135] * (y[58] / p[49]) * p[2]
    bo_ve_co2c13 = y[135] * (y[59] / p[50]) * p[3]
    bo_ve_metc13 = y[135] * (y[61] / p[51]) * p[4]
    gu_li_apap = y[136] * (y[62] / p[52]) * p[2]
    gu_li_co2c13 = y[136] * (y[63] / p[53]) * p[3]
    gu_li_metc13 = y[136] * (y[64] / p[54]) * p[4]
    he_ve_apap = y[138] * (y[65] / p[55]) * p[2]
    he_ve_co2c13 = y[138] * (y[66] / p[56]) * p[3]
    he_ve_metc13 = y[138] * (y[67] / p[57]) * p[4]
    ki_ve_apap = y[139] * (y[68] / p[58]) * p[2]
    ki_ve_co2c13 = y[139] * (y[69] / p[59]) * p[3]
    ki_ve_metc13 = y[139] * (y[70] / p[60]) * p[4]
    li_ve_apap = y[137] * (y[71] / p[61]) * p[2]
    li_ve_co2c13 = y[137] * (y[72] / p[62]) * p[3]
    li_ve_metc13 = y[137] * (y[73] / p[63]) * p[4]
    lu_ar_apap = y[140] * (y[74] / p[64]) * p[2]
    lu_ar_co2c13 = y[140] * (y[75] / p[65]) * p[3]
    lu_ar_metc13 = y[140] * (y[76] / p[66]) * p[4]
    re_ve_apap = y[141] * (y[127] / p[67]) * p[2]
    re_ve_co2c13 = y[141] * (y[128] / p[68]) * p[3]
    re_ve_metc13 = y[141] * (y[129] / p[69]) * p[4]
    sp_li_apap = y[142] * (y[77] / p[70]) * p[2]
    sp_li_co2c13 = y[142] * (y[78] / p[71]) * p[3]
    sp_li_metc13 = y[142] * (y[79] / p[72]) * p[4]
    ve_lu_apap = y[140] * y[80]
    ve_lu_co2c13 = y[140] * y[81]
    ve_lu_metc13 = y[140] * y[82]
    vre_apap = p[6] * y[118]
    vre_co2c13 = p[7] * y[119]
    vre_metc13 = p[8] * y[120]


    return [
         + lu_ar_apap - ar_re_apap - ar_bo_apap - ar_gu_apap - ar_he_apap - ar_ki_apap - ar_sp_apap - ar_li_apap,		# Aar_apap [0]
         + lu_ar_co2c13 - ar_re_co2c13 - ar_bo_co2c13 - ar_gu_co2c13 - ar_he_co2c13 - ar_ki_co2c13 - ar_sp_co2c13 - ar_li_co2c13,		# Aar_co2c13 [1]
         + lu_ar_metc13 - ar_re_metc13 - ar_bo_metc13 - ar_gu_metc13 - ar_he_metc13 - ar_ki_metc13 - ar_sp_metc13 - ar_li_metc13,		# Aar_metc13 [2]
         + ar_bo_apap - bo_ve_apap,		# Abo_apap [3]
         + ar_bo_co2c13 - bo_ve_co2c13,		# Abo_co2c13 [4]
         + Fixation_co2c13 - Release_co2c13,		# Abo_co2c13_fix [5]
         + ar_bo_metc13 - bo_ve_metc13,		# Abo_metc13 [6]
         + Exhalation_co2c13,		# Abreath_co2c13 [7]
         + Absorption_apap + ar_gu_apap - gu_li_apap,		# Agu_apap [8]
         + Absorption_co2c13 + ar_gu_co2c13 - gu_li_co2c13,		# Agu_co2c13 [9]
         + Absorption_metc13 + ar_gu_metc13 - gu_li_metc13,		# Agu_metc13 [10]
         + ar_he_apap - he_ve_apap,		# Ahe_apap [11]
         + ar_he_co2c13 - he_ve_co2c13,		# Ahe_co2c13 [12]
         + ar_he_metc13 - he_ve_metc13,		# Ahe_metc13 [13]
         - vre_apap + ar_ki_apap - ki_ve_apap,		# Aki_apap [14]
         - vre_co2c13 + ar_ki_co2c13 - ki_ve_co2c13,		# Aki_co2c13 [15]
         - vre_metc13 + ar_ki_metc13 - ki_ve_metc13,		# Aki_metc13 [16]
         + CYP1A2MET - APAPD + gu_li_apap + sp_li_apap + ar_li_apap - li_ve_apap,		# Ali_apap [17]
         + CYP1A2MET - CO2FIX + gu_li_co2c13 + sp_li_co2c13 + ar_li_co2c13 - li_ve_co2c13,		# Ali_co2c13 [18]
         - CYP1A2MET + gu_li_metc13 + sp_li_metc13 + ar_li_metc13 - li_ve_metc13,		# Ali_metc13 [19]
         + ve_lu_apap - lu_ar_apap,		# Alu_apap [20]
         - Exhalation_co2c13 + ve_lu_co2c13 - lu_ar_co2c13,		# Alu_co2c13 [21]
         + ve_lu_metc13 - lu_ar_metc13,		# Alu_metc13 [22]
         + ar_re_apap - re_ve_apap,		# Are_apap [23]
         + ar_re_co2c13 - re_ve_co2c13,		# Are_co2c13 [24]
         + ar_re_metc13 - re_ve_metc13,		# Are_metc13 [25]
         + ar_sp_apap - sp_li_apap,		# Asp_apap [26]
         + ar_sp_co2c13 - sp_li_co2c13,		# Asp_co2c13 [27]
         + ar_sp_metc13 - sp_li_metc13,		# Asp_metc13 [28]
         + vre_apap,		# Aurine_apap [29]
         + vre_co2c13,		# Aurine_co2c13 [30]
         + vre_metc13,		# Aurine_metc13 [31]
         + Injection_apap + Infusion_apap - ve_lu_apap + re_ve_apap + bo_ve_apap + he_ve_apap + ki_ve_apap + li_ve_apap,		# Ave_apap [32]
         - Fixation_co2c13 + Release_co2c13 + Injection_co2c13 + Infusion_co2c13 - ve_lu_co2c13 + re_ve_co2c13 + bo_ve_co2c13 + he_ve_co2c13 + ki_ve_co2c13 + li_ve_co2c13,		# Ave_co2c13 [33]
         + Injection_metc13 + Infusion_metc13 - ve_lu_metc13 + re_ve_metc13 + bo_ve_metc13 + he_ve_metc13 + ki_ve_metc13 + li_ve_metc13,		# Ave_metc13 [34]
        -Injection_apap * p[74],		# DIV_apap [35]
        -Injection_co2c13 * p[75],		# DIV_co2c13 [36]
        -Injection_metc13 * p[76],		# DIV_metc13 [37]
        -Absorption_apap * p[74],		# D_apap [38]
        -Absorption_co2c13 * p[75],		# D_co2c13 [39]
        -Absorption_metc13 * p[76],		# D_metc13 [40]
        p[82] * 60,		# cum_dose_apap [41]
        p[83] * 60,		# cum_dose_co2c13 [42]
        p[84] * 60,		# cum_dose_metc13 [43]
    ]

