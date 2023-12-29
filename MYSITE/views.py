from django.http import HttpResponse
from django.shortcuts import render
from .utils.Polynomial import polynomial, polynomialnode, make_polynomial
from .utils.functions import counttheletters
from .utils.mathematics import calculate_mean,calculate_median,calculate_mode,calculate_gcf,calculate_lcm


def index(request):
    return render(request, 'index.html')

# Extra-tool
def calculator(request):
    return render(request,'calculator.html')


def about(request):
    return render(request, 'about.html')


# ------------------------- Mathematics ------------------------- #
def preAlgebra(request):
    #Using name from html to give it to data_mmm var.
    results = {}
    data_mmm = (request.POST.get('input-mmm','default'))
    data_lgcmf = (request.POST.get('input-lgcfm','default'))

    if data_mmm == 'default' and data_lgcmf == 'default':
        return render(request,'pre-algebra.html')
    
    elif data_mmm == 'default' and data_lgcmf != 'default':
        conv_data_mmm = list(map(int, data_lgcmf.split(',')))
        print(conv_data_mmm)
        
        return render(request,'pre-algebra.html',)
    
    else:
        conv_data_mmm = list(map(int, data_mmm.split(',')))
        print(conv_data_mmm)
    
        res_mean = calculate_mean(conv_data_mmm)
        res_median = calculate_median(conv_data_mmm)
        res_mode = calculate_mode(conv_data_mmm)
        res_lcm = calculate_lcm(conv_data_mmm)
        res_gcf = calculate_gcf(conv_data_mmm)

        # print(res_mean,res_median,res_mode)

        results = {'mean':res_mean,'median':res_median,'mode':res_mode,'gcf':res_gcf,'lcm':res_lcm}
        return render(request,'pre-algebra.html',results)

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
