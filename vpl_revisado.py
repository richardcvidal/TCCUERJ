# -*- coding: utf-8 -*-

import numpy as np

# VPL
# somatorio de: t =1 até t=n, sendo n = vida util do isolamento em anos
def VPL(FCt, n, i):
    vpl = 0
    for t in range(1, n+1):
        vpl = vpl + FCt/(1+i)**t
    return vpl

def VPL_lista(custo_inicial_aerogel, FCt, n, i):
    vpl = custo_inicial_aerogel
    vpl_lista = [vpl]
    for t in range(1, n+1):
        vpl = vpl + FCt/(1+i)**t
        vpl_lista.append(vpl)
    return vpl_lista

# VPLAE (Valor presente líquido anualizado equivalente)
def VPLAE(FCt, n, i):
    vpl = VPL(FCt, n, i)
    vplae = vpl*((i*((1+i)**n))/(((1+n)**n)-1))
    return vplae

#PAYBACK
def payback(lci, FCt, n, i): # retorna o t necessesário para
    vpl = lci #que o investimento passe a gerar
    for t in range(1, n+1):          #retorno do capital investido.
        vpl = vpl + FCt/(1+i)**t
        if vpl >= 0:
            return t
        else:
            continue
