print('Approximate calculations using the differential of a function of one variable')

ind_sqrt = int(input('Enter the sqrt\'s exponent: '))
under_sqrt = int(input('Enter the num under sqrt: '))
degree = int(input('Enter the degree of this number: '))

def x_zero(n):
    if round(n**(degree/ind_sqrt)) != 1:
        return round(n**(degree/ind_sqrt))**ind_sqrt
    else:
        return round(n**(degree/ind_sqrt),20)**ind_sqrt

def delta(n):
    return under_sqrt**degree - x_zero(n)

def derivat(n):
    index = degree/ind_sqrt
    delta_index = index - 1
    if delta_index > 0:
        return ind_sqrt*(n**delta_index)
    elif delta_index < 0:
        delta_index *= -1
        return 1/(ind_sqrt*(n**delta_index))
    elif delta_index == 0:
        return 1

def main_func(n):
    return n**(1/ind_sqrt)
print('Xₒ - the nearest number to the sqrt from which we can calculate the sqrt {} degree'.format(under_sqrt))
print('---------------------------------------------------------------------------------------------------')
print('ΔХ - increment argument to Xₒ')
print('---------------------------------------------------------------------------------------------------')
print('ΔХ = X - Xₒ')
print('---------------------------------------------------------------------------------------------------')
print('Xₒ: {}, ΔХ: {}'.format(x_zero(under_sqrt),delta(under_sqrt)))
print('---------------------------------------------------------------------------------------------------')
x_null = x_zero(under_sqrt)
x_delta = delta(under_sqrt)
print('---------------------------------------------------------------------------------------------------')
print('We are looking for an approximate value using the formula for calculation using the differential:')
print('---------------------------------------------------------------------------------------------------')
print('f( Xₒ + ΔX ) ~ f(Xₒ) + d[f(Xₒ)]')
print('---------------------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------------------')
print('We have a function look like f(x) = ⁿ√x')
print('---------------------------------------------------------------------------------------------------')
print('Hence follows f(Xₒ) = {}'.format(round(main_func(x_null))))
print('---------------------------------------------------------------------------------------------------')
f_x0 = round(main_func(x_null))
print('---------------------------------------------------------------------------------------------------')
print('The differentia formula: d[f(Xₒ)] = f`(Xₒ)*ΔX')
print('---------------------------------------------------------------------------------------------------')
print('The derivative of our function will be equal to n*x^ⁿ⁻¹, when n - the indicator of the fractional degree')
print('---------------------------------------------------------------------------------------------------')
print('Round to the eighth number after the decimal point')
print('---------------------------------------------------------------------------------------------------')
print('Then f`(Xₒ) = {}'.format(round(derivat(x_null),8)))
f_der_x0 = round(derivat(x_null),8)
print('Hence follows d[f(Xₒ)] = {}*{} <=> {}'.format(f_der_x0, x_delta, round(f_der_x0*x_delta,8)))
print('---------------------------------------------------------------------------------------------------')
deff = round(f_der_x0*x_delta,8)
print('---------------------------------------------------------------------------------------------------')
print('Put all in the formula f( Xₒ + ΔX ) ~ f(Xₒ) + d[f(X0)]')
print('---------------------------------------------------------------------------------------------------')
print('f({} + {}) ~ {} + {}'.format(x_null,x_delta,f_x0,deff))
print('---------------------------------------------------------------------------------------------------')
result = f_x0 + deff
print('Our answer: {}'.format(result))
result_math = (under_sqrt**degree)**(1/ind_sqrt)
print('Answer from calculate: {}'.format(result_math))

