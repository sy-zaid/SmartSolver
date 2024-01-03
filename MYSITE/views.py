from django.http import HttpResponse
from django.shortcuts import render
from .utils.Polynomial import polynomial, polynomialnode, make_polynomial
from .utils.functions import counttheletters
from .utils.mathematics import calculate_mean,calculate_median,calculate_mode,calculate_gcf,calculate_lcm
from .utils.algorithms import prepareResultFCFS,mapInputToIntList,convertListtoDict,prepareResultRR
from .utils.physics import calcVelocity,calcAcceleration,calcFrequency


def index(request):
    return render(request, 'index.html')

# Extra-tool
def calculator(request):
    return render(request,'calculator.html')


def about(request):
    return render(request, 'about.html')


# ------------------------- Mathematics ------------------------- #
def preAlgebra(request):
    results = {}
    data_mmm = (request.POST.get('input-mmm','default'))
    data_lgcmf = (request.POST.get('input-lgcmf','default'))

    if data_mmm == 'default' and data_lgcmf == 'default':
        return render(request,'pre-algebra.html')
    
    elif data_mmm == 'default' and data_lgcmf != 'default':
        conv_data_mmm = list(map(int, data_lgcmf.split(',')))

        res_lcm = calculate_lcm(conv_data_mmm)
        res_gcf = calculate_gcf(conv_data_mmm)
        results = {'gcf':res_gcf,'lcm':res_lcm}
        # return render(request,'pre-algebra.html',results)
    
    else:
        conv_data_mmm = list(map(int, data_mmm.split(',')))
    
        res_mean = calculate_mean(conv_data_mmm)
        res_median = calculate_median(conv_data_mmm)
        res_mode = calculate_mode(conv_data_mmm)
        results = {'mean':res_mean,'median':res_median,'mode':res_mode}

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
    """
    <!-- IDS USED IN THE PHYSICAL-CALCULATIONS TEMPLATE -->
        <!--
        Velocity Section (PC-whole-div-2):
        Input:
            - Distance: input-distance
            Units (Dropdown): dropdown-units-distance
                - Meters (m)
                - Kilometers (km)
                - Feet (ft)

            - Time: input-time
            Units (Dropdown): dropdown-units-time
                - Seconds (s)
                - Hours (h)

        Buttons:
            - Clear Button: clearButton
            - Solve Button: solveButton

        Output:
            - Velocity: res-mean
        -->
        <!--
        Acceleration Section (PC-whole-div-3):
        Input:
            - Initial Velocity: input-initial-velocity
            - Final Velocity: input-final-velocity
            Units (Dropdown): dropdown-units-final-vel
                - Meters per second (m/s)
                - Kilometers per hour (km/h)
                - Feet per second (ft/s)
            - Time: input-time-acc
            Units (Dropdown): dropdown-units-time
                - Seconds (s)
                - Hours (h)
        Buttons:
            - Clear Button: clearButton
            - Solve Button: solveButton
        Output:
            - Acceleration: res-mean
        -->

        <!--
        Frequency Section (PC-whole-div-4):
        Input:
            - Time: input-time-acc
            Units (Dropdown): dropdown-units-time
                - Seconds (s)
                - Hours (h)
        Buttons:
            - Clear Button: clearButton
            - Solve Button: solveButton
        Output:
            - Frequency: res-mean
        -->

        <!--
        Pressure Section (PC-whole-div-5):
        Input:
            - Force: input-force
            Units (Dropdown): dropdown-units-force
                - Newton (N)
            - Area: input-area
            Units (Dropdown): dropdown-units-force
                - Square meter (m²)
        Buttons:
            - Clear Button: clearButton
            - Solve Button: solveButton
        Output:
            - Pressure: res-mean
        -->

        <!--
        Force Section (PC-whole-div-6):
        Input:
            - Mass: input-mass
            Units (Dropdown): dropdown-units-mass
                - Grams (g)
                - Kilograms (kg)
                - Milligrams (mg)
            - Acceleration: input-acceleration
            Units (Dropdown): dropdown-units-acceleration
                - Meters per second squared (m/s²)
                - Meters per second (m/s)
        Buttons:
            - Clear Button: clearButton
            - Solve Button: solveButton
        Output:
            - Force: res-mean
        -->

    """
    results = {}
    # VELOCITY INPUTS
    inp_distance = (request.POST.get('input-distance',None))
    inp_time = (request.POST.get('input-time',None))
    # ACCELERATION INPUTS
    inp_initial_velocity = (request.POST.get('input-initial-velocity', None))
    inp_final_velocity = (request.POST.get('input-final-velocity', None))
    inp_time_acc = (request.POST.get('input-time-acc', None))
    # FREQUENCY INPUTS
    inp_time_freq = request.POST.get('input-time-freq', None)
    

    # FOR VELOCITY
    if inp_distance and inp_time:
        dddistance = (request.POST.get('dropdown-units-distance','meters'))
        ddtime = (request.POST.get('dropdown-units-time','seconds'))
        lst_velocity = calcVelocity(inp_distance,inp_time,dddistance,ddtime)
        velocity = lst_velocity
        siu_velocity = 'm/s'
        results = {'velocity':velocity,'siu_velocity':siu_velocity}
        return render(request,'physical-calculation.html',results)
    
    # FOR ACCELERATION
    if inp_initial_velocity and inp_final_velocity and inp_time_acc:
        ddtime_acc = request.POST.get('dropdown-units-time', 'seconds')
        ddvelocity = request.POST.get('dropdown-units-final-vel', 'meters-per-second-squared')
        acceleration = calcAcceleration(inp_final_velocity,inp_initial_velocity,inp_time_acc,ddvelocity,ddtime_acc)
        siu_acceleration = 'm/s²'
        results = {'acceleration':acceleration,'siu_acceleration':siu_acceleration}
        return render(request,'physical-calculation.html',results)

    # FOR FREQUENCY
    if inp_time_freq:
        ddtime_freq = request.POST.get('dropdown-units-time', 'seconds')
        frequency = calcFrequency(inp_time_freq,ddtime_freq)
        siu_freq = 'Hertz (Hz)'
        results = {'frequency':frequency,'siu_freq':siu_freq}
        return render(request,'physical-calculation.html',results)
    
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
    """
    Types of Algorithms used:
    - FCFS 
    - SJF Preemptive
    - SJF Non-Preemptive
    - Round-Robin 
    - Priority Preemptive 
    - Priority Non-Preemptive 
    """
    # if request.method == "POST":
    results = {}
    algorithm_name = (request.POST.get('algos-dropdown','default'))
    arrival_times = (request.POST.get('arrival-time','default'))
    burst_times = (request.POST.get('burst-time','default'))
    priorities = (request.POST.get('priority','default'))
    
    quantum_time = (request.POST.get('quantum-time','default'))
    
    # print(algorithm_name,arrival_times,burst_times, priorities,quantum_time)
    # Example outputs of the above strings (FCFS is selected in dropdown): 
    # FCFS 0,1,2,3 9,2,1,7 default default
    # FCFS 0,1,2,3 9,2,1,7 default default
    if request.method == "POST":
        arrival_times = list(map(int, arrival_times.split(',')))
        burst_times = list(map(int, burst_times.split(',')))
        
        # print(algorithm_name,arrival_times,burst_times, priorities,quantum_time)
   
    if algorithm_name == "FCFS":
        results = prepareResultFCFS(arrival_times,burst_times)
        return render(request,"os-algorithms.html",results)
    
    # ------------------------- IF THE ALGO IS SJF ------------------------- #
    elif algorithm_name == "SJF":
        pass
    
    elif algorithm_name == "SJF-nonpr":
        pass
    
    elif algorithm_name == "RR":
        quantum_time = int(quantum_time)
        results = prepareResultRR(arrival_times,burst_times,quantum_time)
        return render(request,"os-algorithms.html",results)
            
    elif algorithm_name == "Priority-nonpr":
        priorities = list(map(int,priorities.split(',')))
        
    elif algorithm_name == "Priority":
        priorities = list(map(int,priorities.split(',')))
    
    else:    
        return render(request,'os-algorithms.html')
