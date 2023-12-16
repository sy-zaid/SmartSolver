from django.http import HttpResponse
from django.shortcuts import render
from .utils.Polynomial import polynomial, polynomialnode, make_polynomial
from .utils.functions import counttheletters


def index(request):
    return render(request, 'index.html')

# Extra-tool
def calculator(request):
    return render(request,'calculator.html')


def about(request):
    return render(request, 'about.html')


# ------------------------- Mathematics ------------------------- #
def preAlgebra(request):
    return render(request,'pre-algebra.html')

def algebra(request):
    poly_input_1 = (request.POST.get('Polynomial1', 'default'))
    operator_poly = (request.POST.get('Operator_Poly'))
    poly_input_2 = (request.POST.get('Polynomial2', 'default'))
    analyzed = ' . . . . . '

    P1 = make_polynomial(str(poly_input_1))
    P2 = make_polynomial(str(poly_input_2))

    if P1 != None and P2 != None:
        if operator_poly == '0':
            analyzed = str(P1.addtwopolys(P2).display())
        elif operator_poly == '1':
            analyzed = str(P1.subtracttwopolys(P2).display())
        elif operator_poly == '2':
            analyzed = str(P1.multiplypolys(P2).display())
        else:
            pass

    params = {'result_count': analyzed}

    return render(request, "algebra.html", params)


# ------------------------- Physics ------------------------- #
def physicalCalculation(request):
    return render(request, "physical-calculation.html")

def physicalValueConverter(request):
    return render(request,'physical-value-converter.html')

# ------------------------- Programming ------------------------- #
def binary(request):
    return render(request, "binary.html")

def sorting(request):
    return render(request,'sorting.html')

# ------------------------- Algorithms ------------------------- #
def osAlgorithms(request):
    return render(request,'os-algorithms.html')
