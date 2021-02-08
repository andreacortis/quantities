from quantities import quantity_maker, Mass, Limits, Q_
from pint import DimensionalityError
from uncertainties import ufloat

def test_00():
    try:
        m = Mass(name='m', magnitude=ufloat(6, 0.1), units='kg')
    except DimensionalityError as exc:
        raise exc

def test_01():
    try:
        m = Mass(name='m', magnitude=ufloat(6, 0.1), units='m')
    except DimensionalityError as exc:
        pass
    
    
# from quantities import Q_, Mass, Volume, density, Limits
# from uncertainties import ufloat
# from IPython.display import display

# m = Mass(name='m', magnitude=ufloat(6, 0.1), units='kg')
# display(m)

# v = Volume(name='v', quantity=Q_(ufloat(3, 0.2),'m^3'))
# display(v)

# rho_1 = density(r'\zeta',m,v)
# display(rho_1)

# m2 = Mass(name=r'm_2', magnitude=ufloat(6, 0.1), units='kg')
# display(m2)

# rho_2 = density(r'\rho_2',m2,v)
# display(rho_2)

# m0 = Mass(name='m_0', limits=Limits([Q_('2.8 kg'),Q_('6.07 kg')]))
# v0 = Volume(name='v_0', limits=Limits([Q_('3.21 m^3'),Q_('3.6 m^3')]))

# rho_0 = density(r'\zeta',m0,v0)
# display(rho_0)

# # -----------

# Permittivity = quantity_maker('Permittivity','1')
# @typechecked
# def dryrock_permittivity(name:str, rho:Density) -> Permittivity:
#     name = f'\kappa = exp(\\frac{{{rho.name}}}{{1.5455 [g/cm^3]}})'
#     rho_ref = Density('',quantity = Q_('1.5455 g/cm^3'))
#     p = np.exp(rho / rho_ref)
#     return Permittivity(name=name,magnitude=p,units='')
# rho = Density(name=r'{\rho_0}', quantity=Q_('2.32 g/cm^3'))

# k_quartz = dryrock_permittivity('\kappa' , rho)
# k_quartz_measured = 4.30 # https://academic.oup.com/gji/article/163/3/1195/2127261
# display(k_quartz)