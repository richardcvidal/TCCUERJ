# -*- coding: utf-8 -*-

import numpy as np
# =============================================================================
# Resistências térmicas em cilindros.
# =============================================================================

# =============================================================================
# Resistências térmicas de condução  em um cilindro.
# Input em m e W/(m.K), output em K/W.
# =============================================================================

def rt_cond_cili(Di, De, lmd, z):
    
    a = np.log(De/Di)
    
    b = 2.0*np.pi*z*lmd
    
    return (a/b)

# =============================================================================
# Resistência térmica de convecção em um cilindro. Input em
# m e W/(m^2.K), output em K/W.
# =============================================================================

def rt_conv_cili(D, h, z):
    
    return (1.0/(h*np.pi*D*z))

# =============================================================================
# Resistência térmica de radiação em um cilindro. Input em
# m e W/(m^2.K), output em K/W.
# =============================================================================

def rt_crad_cili(D, h, z):
    
    return (1.0/(h*np.pi*D*z))