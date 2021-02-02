import numpy as np
from typeguard import typechecked
from decimal import Decimal
from IPython.display import display, Latex
import numbers
from uncertainties import ufloat
import uncertainties
from pint import UnitRegistry, DimensionalityError
ureg = UnitRegistry(non_int_type=Decimal)
ureg.default_format = "~P"
Q_=ureg.Quantity
from interval import interval, inf, imath

esc = lambda s: s.replace('"\"','"\\"')

class Limits:
    def __init__(self, limits):
        lower, upper = limits
        try:
            assert lower.dimensionality == upper.dimensionality
            if not isinstance(lower.m, Decimal):
                assert lower.m.std_dev == 0
            if not isinstance(upper.m, Decimal):
                assert upper.m.std_dev == 0
        except DimensionalityError as exc:
            raise exc
        lower.ito_base_units()
        upper.ito_base_units()
        self.value = interval([lower.m, upper.m])
        self.units = lower.units
    
    def __mul__(self,other):
        if isinstance(other, numbers.Number):
            return self.value*other
        elif isinstance(other, Limits):
            return self.value*other.value

    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __truediv__(self,other):
        if isinstance(other, numbers.Number):
            return self.value/other
        elif isinstance(other, Limits):
            return self.value/other.value
        
    def __repr__(self):
        return self.value.__str__() + self.units.__str__()

class BasicQuantity:
    units = '1'
    class_units = Q_(f"{units}")
    def __init__(self, name="", **kwargs):
        c1 = set(kwargs.keys()) == {'magnitude','units'}
        c2 = set(kwargs.keys()) == {'quantity'}
        c3 = set(kwargs.keys()) == {'limits'}
        self.name = name
        
        assert c1 ^ c2 ^ c3
        if c1:
            magnitude = kwargs['magnitude']
            units = kwargs['units']
            if isinstance(magnitude,numbers.Number):
                self.magnitude = ufloat(magnitude,0)
            else:
                self.magnitude = magnitude
                self.units = units
            self.value = Q_(self.magnitude, self.units)
        if c2:
            quantity = kwargs['quantity']
            self.value = quantity          
        if c3:
            limits = kwargs['limits']
            self.value = limits 

    def __add__(self,other):
        try:
            return self.value + other.value
        except DimensionalityError as exc:
            raise exc

    def __sub__(self, other):
        try:
            return self.value - other.value
        except DimensionalityError as exc:
            raise exc
            
    def __mul__(self,other):
        if isinstance(other, numbers.Number):
            return self.value*other
        elif isinstance(other, BasicQuantity):
            return self.value*other.value

    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __pow__(self,n):
        return self.value**n
        
    def __truediv__(self,other):
        if isinstance(other, numbers.Number):
            return self.value/other
        elif isinstance(other, BasicQuantity):
            return self.value/other.value
        
    def __str__(self):
        if isinstance(self.value, interval):
            h = self.value.__str__()
            u = self.units
        else:
            h = self.value.m
            u = self.value.units
        s = f"{self.name} = {h} \\, \\rm{{[{u}]}}, \\, \\rm{{({self.__class__.__name__})}}"
        s = s.replace('+/-',r'\pm')
        return s
    
    def __repr__(self):
        s = f"$${self.__str__()}$$"
        display(Latex(s))
        return ""

def quantity_maker(klass, units, expression=lambda x:Q_('0')):
    return type(klass,(BasicQuantity,),{"class_units":Q_(units),'units':units ,'expression':expression})
    
# custom physical quanti    
Mass = quantity_maker('Mass','kg')
Time = quantity_maker('Mass','sec')
Length = quantity_maker('Length','m')
Area = quantity_maker('Area','m^2')
Volume = quantity_maker('Volume','m^3')

Porosity = quantity_maker('Porosity','m^3/m^3')

Velocity = quantity_maker('Velocity','m/s')
@typechecked
def speed(name:str, l:Length, dt:Time) -> Velocity:
    name = f'{name} = \\frac{{{l.name}}}{{{dt.name}}}'
    return Velocity(name = name, quantity = (l/dt))

Density = quantity_maker('Density','kg/m^3')
@typechecked
def density(name:str, m:Mass, v:Volume) -> Density:
    name = f'{name} = \\frac{{{m.name}}}{{{v.name}}}'
    return Density(name = name, quantity = (m/v))

if __name__ == '__main__':
    pass