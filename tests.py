from quantities import quantity_maker, Limits, Q_
from pint import DimensionalityError
from uncertainties import ufloat
from typeguard import typechecked

Mass = quantity_maker('Mass','kg')
Volume = quantity_maker('Volume','m^3')

def test_00():
    try:
        m = Mass(name='m', quantity=Q_('6 kg'))
    except DimensionalityError as exc:
        raise exc

    try:
        m = Mass(name='m', magnitude=ufloat(6, 0.1), units='kg')
    except DimensionalityError as exc:
        raise exc

    try:
        m = Mass(name='m', limits=Limits([Q_('6 kg'), Q_('7 kg')]))
    except DimensionalityError as exc:
        raise exc

    try:
        r = Mass(r'\bar{m}',quantity=Q_(np.array([ufloat(3,0.1),ufloat(4,0.2)]),'kg'))
    except DimensionalityError as exc:
        raise exc

def test_01():
    try:
        m = Mass(name='m', magnitude=ufloat(6, 0.1), units='m')
    except DimensionalityError as exc:
        pass
    
def test_02():

    Density = quantity_maker('Density','kg/m^3')
    @typechecked
    def density(name:str, m:Mass, v:Volume) -> Density:
        name = f'{name} = \\frac{{{m.name}}}{{{v.name}}}'
        return Density(name = name, quantity = (m/v))

    m = Mass(name='m', magnitude=ufloat(6, 0.1), units='kg')
    v = Volume(name='v', quantity=Q_(ufloat(3, 0.2),'m^3'))
    rho_1 = density(r'\rho',m,v)
    rho_expected = Density('', quantity = Q_(ufloat(2.00, 0.14), "kg/m^3"))
    assert rho_1 == rho_expected
    
# # -----------

# Density = quantity_maker('Density','kg/m^3')
# Permittivity = quantity_maker('Permittivity','1')
# @typechecked
# def dryrock_permittivity(name:str, rho:Density) -> Permittivity:
#     name = f'\kappa = exp(\\frac{{{rho.name}}}{{1.5455 [g/cm^3]}})'
#     rho_ref = Density('',quantity = Q_('1.5455 g/cm^3'))
#     p = np.exp(rho / rho_ref)
#     return Permittivity(name=name,magnitude=p,units='')

# rho = Density('',quantity = Q_('2.32 g/cm^3'))
# k_quartz = dryrock_permittivity('\kappa' , rho)
# k_quartz_measured = 4.30 # https://academic.oup.com/gji/article/163/3/1195/2127261
# display(k_quartz)