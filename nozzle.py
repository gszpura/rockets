# TODO: visualisation
import math

# CONSTS
# diamater of throat
dt = 5
rt = dt / 2.0
# diamater of combustion chamber
dc = 18
rc = dc / 2.0
# expansion ratio
exp = 4.84
# div angle
div = 30
conv_deg = 60
print("Init conditions  ", "throat: ", dt, "expansion: ", exp, "divergence angle:", div, "conv angle:", conv_deg)


# COMMON CALC
# area of throat
at = math.pi*(rt)**2


print("-----------------------DIVERGENCE---------------------------------")
# calc for exit values
ae = at*exp
re = math.sqrt(ae/math.pi)
print("Exit radius:", re)
print("Exit diameter:", re*2)

# calc for div angles
div_half = div / 2
div_rad = div_half / 180.0 * math.pi
div_tan = math.tan(div_rad)
# calculations for divergance trapezoid
div_len = (re - rt) / div_tan
print("Divergence length:", div_len)


print("-----------------------DIVERGENCE FORM----------------------------")
div_cone_missing_h =  rt*div_len / (re - rt)
div_cone_h = div_cone_missing_h + div_len
print("DIV CONE H:", div_cone_h)
print("DIV CONE D:", re*2)


print("-----------------------CONVERGENCE--------------------------------")
# calc for conv angles
conv_deg_half = conv_deg / 2
conv_rad = conv_deg_half/180.0 * math.pi
tan_conv = math.tan(conv_rad)

# calc for convergence trapezoid
chamber_r_trapezoid = rc - rt
conv_len = chamber_r_trapezoid / tan_conv
print("Convergence length:", conv_len)


print("-----------------------CONVERGENCE FORM----------------------------")
conv_cone_missing_h = rt*conv_len/(rc - rt)
conv_cone_h = conv_cone_missing_h + conv_len
print("CONV CONE H:", conv_cone_h)
print("CONV CONE D:", dc)


# ----- expansion ratio calc -----
# http://www.nakka-rocketry.net/articles/noz_example3.pdf
# KNSU: https://www.nakka-rocketry.net/succhem.html
print("-----------------------TODO EXPANSION RATIO--------------------------")
k = 1.044
pe = 1.0
p0 = 21.43 # how this is calculated???
print("Convergence", "k:", k, "p0:", p0)

fst = ((k + 1)/2.0)**(1.0/(k-1))
print("First term:", fst)
sec = (pe / p0)**(1.0/k)
print("Sec term:", sec)
third = (k + 1)/(k - 1.0)*(1.0 - (pe / p0)**((k-1)/k))
print("Third term: ", third)
expX = fst*sec*math.sqrt(third)
ratio = 1.0 / expX
print("Expansion ratio: ", ratio)

aX = at*ratio
rX = math.sqrt(aX/math.pi)
print("Radius X: ", rX)
print("Diameter X:", rX*2)
