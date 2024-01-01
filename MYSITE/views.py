from django.http import HttpResponse
from django.shortcuts import render
from .utils.Polynomial import polynomial, polynomialnode, make_polynomial
from .utils.functions import counttheletters
from .utils.mathematics import calculate_mean,calculate_median,calculate_mode,calculate_gcf,calculate_lcm
from .utils.algorithms import prepareResultFCFS,mapInputToIntList,convertListtoDict
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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
        
        complete_result_dict = prepareResultFCFS(arrival_times,burst_times)
        # print(complete_result_dict)

        # Execution State
        execution_state = complete_result_dict["execution-state"]

        # Gantt Chart
        gantt_chart_list = complete_result_dict['gantt-chart']
        gantt_chart_dict = convertListtoDict(gantt_chart_list)
        print(gantt_chart_dict)

        # Separate lists for start and end times
        start_times = [process["start_time"] for process in gantt_chart_dict]
        end_times = [process["end_time"] for process in gantt_chart_dict]
        process_names = [process["name"] for process in gantt_chart_dict]

        # Create a subplot with shared x-axis
        fig = make_subplots(
            rows=1, cols=1,
            subplot_titles=[""],
            shared_xaxes=True,
            vertical_spacing=0.1,
        )

        # Add horizontal bars to the chart
        fig.add_trace(go.Bar(
            x=[start_times, end_times],
            y=process_names,
            orientation='h',
        ))

        # Update layout of the chart
        fig.update_layout(
            title_text='',
            xaxis_title='Time',
            yaxis_title='Processes',
        )

        # Convert the figure to HTML
        chart_div = fig.to_html(full_html=False)

        results = {'execution_state':execution_state,'chartdiv':chart_div}

        return render(request,"os-algorithms.html",results)
    
    # ------------------------- IF THE ALGO IS SJF ------------------------- #
    elif algorithm_name == "SJF":
        pass
    
    elif algorithm_name == "SJF-nonpr":
        pass
    
    elif algorithm_name == "RR":
        quantum_time = int(quantum_time)
            
    elif algorithm_name == "Priority-nonpr":
        priorities = list(map(int,priorities.split(',')))
        
    elif algorithm_name == "Priority":
        priorities = list(map(int,priorities.split(',')))
    
    else:    
        return render(request,'os-algorithms.html')
