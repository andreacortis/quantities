from quantities import Q_, Mass, Volume, density
from uncertainties import ufloat
from IPython.display import display

m = Mass(name='m', magnitude=ufloat(6, 0.1), units='kg')
display(m)

v = Volume(name='v', quantity=Q_(ufloat(3, 0.2),'m^3'))
display(v)

rho_1 = density(r'\zeta',m,v)
display(rho_1)

m2 = Mass(name=r'm_2', magnitude=ufloat(6, 0.1), units='kg')
display(m2)

rho_2 = density(r'\rho_2',m2,v)
display(rho_2)
