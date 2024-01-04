from .FCFS import FCFS
from .RR import RR
from .SJF import SJF
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def mapInputToIntList(lst):
    res = list(map(int,lst.split(",")))
    return res

def calcFinishTime(arrival_times,burst_times,priorities = "default",quantum_time = "default"):
    pass

def calcAvg(num_processes,timefactor):
        sumTT = sum(timefactor)
        return round(sumTT / num_processes,2)

def get_times(process_list,factor):
        arrival_times = [process[factor] for process in process_list]
        return arrival_times

def prepareResultFCFS(arrival_times,burst_times):
    """
    var complete_result_dict = {'gantt-chart':gantt_chart,'execution-state':execution_state,
                   'completion-times':completion_times,'turnaround-times':turnaroundtimes,
                   'waiting-times':waitingtimes,'avg_turnaround-time':avg_turnaroundtime,
                   'avg_waiting-time':avg_waitingtime,'process_list': pplist
                   }
    """

    results = {}
    complete_result_dict = FCFS(arrival_times,burst_times)
        # print(complete_result_dict)

    # Execution State
    execution_state = complete_result_dict["execution-state"]
    
    # Turn around & Average Turnaround Times.
    turnaroundtimes, avg_turnaroundtime = complete_result_dict["turnaround-times"],complete_result_dict["avg_turnaround-time"]
    # print("\nTurnAround Times:",turnaroundtimes)
    # Waiting time & Average Waiting Times.
    waitingtimes, avg_waitingtime = complete_result_dict["waiting-times"],complete_result_dict["avg_waiting-time"]
    # print("\nWaiting Times:",waitingtimes)
    process_list = complete_result_dict["process_list"]
    completiontimes = complete_result_dict["completion-times"]
    # print("\nProcess List:",process_list)

    # Gantt Chart
    gantt_chart_list = complete_result_dict['gantt-chart']
    gantt_chart_dict = convertListtoDict(gantt_chart_list)
    print(gantt_chart_dict)

    # Separate lists for start and end times
    start_times = [process["start_time"] for process in gantt_chart_dict]
    end_times = [process["end_time"] for process in gantt_chart_dict]
    process_names = [process["name"] for process in gantt_chart_dict]

    # Created a subplot with shared x-axis
    fig = make_subplots(
        rows=1, cols=1,
        subplot_titles=[""],
        shared_xaxes=True,
        vertical_spacing=0.1,
    )

    # Added horizontal bars to the chart
    fig.add_trace(go.Bar(
        x=[start_times, end_times],
        y=process_names,
        orientation='h',
        marker=dict(color='#0b67f1'),
    ))

    # Updated layout of the chart
    fig.update_layout(
        title_text='',
        xaxis_title='Time',
        yaxis_title='Processes',
    )

    # Converted the figure to HTML
    chart_div = fig.to_html(full_html=False)

    # Created a results dictionary.
    results = {"chartdiv":chart_div,'execution_state':execution_state,'completiontimes':completiontimes,
               'turnaroundtimes':turnaroundtimes,'waitingtimes':waitingtimes,
               'avg_turnaroundtime':avg_turnaroundtime,'avg_waitingtime':avg_waitingtime,
               'process_list': process_list}
    return results


def convertListtoDict(gantt_chart_list):
    converted_list = []

    for entry in gantt_chart_list:
        entry_dict = {'name': entry[1], 'start_time': entry[0]}
        entry_dict['end_time'] = entry[2]
        converted_list.append(entry_dict)

    return converted_list

# gantt_chart_list = [[0, 'Idle', 1], [1, 'Process-1', 3], [3, 'Process-2', 6], [6, 'Idle', 12], [12, 'Process-0', 13]]
# print(convertListtoDict(gantt_chart_list))


def prepareResultRR(arrival_times,burst_times,quantum_time):
    """
    var result_dict = {'gantt-chart': gantt_chart_info, 'execution-state': execution_state,
                    'solved_processes_info': solved_processes_info, 'process_list': pplist,
                    'completion-times':completion_times,'turnaround-times':turnaroundtimes,
                    'waiting-times':waitingtimes,'avg_turnaround-time':avg_turnaroundtime,
                   'avg_waiting-time':avg_waitingtime}
    """

    results = {}
    complete_result_dict = RR(arrival_times,burst_times,quantum_time)
        # print(complete_result_dict)

    # Execution State
    execution_state = complete_result_dict["execution-state"]
    
    # Turn around & Average Turnaround Times.
    turnaroundtimes, avg_turnaroundtime = complete_result_dict["turnaround-times"],complete_result_dict["avg_turnaround-time"]
    # print("\nTurnAround Times:",turnaroundtimes)
    # Waiting time & Average Waiting Times.
    waitingtimes, avg_waitingtime = complete_result_dict["waiting-times"],complete_result_dict["avg_waiting-time"]
    # print("\nWaiting Times:",waitingtimes)
    process_list = complete_result_dict["process_list"]
    completiontimes = complete_result_dict["completion-times"]
    # print("\nProcess List:",process_list)

    # Gantt Chart
    gantt_chart_list = complete_result_dict['gantt-chart']
    gantt_chart_dict = convertListtoDict(gantt_chart_list)
    print(gantt_chart_dict)

    # Separate lists for start and end times
    start_times = [process["start_time"] for process in gantt_chart_dict]
    end_times = [process["end_time"] for process in gantt_chart_dict]
    process_names = [process["name"] for process in gantt_chart_dict]

    # Created a subplot with shared x-axis
    fig = make_subplots(
        rows=1, cols=1,
        subplot_titles=[""],
        shared_xaxes=True,
        vertical_spacing=0.1,
    )

    # Added horizontal bars to the chart
    fig.add_trace(go.Bar(
        x=[start_times, end_times],
        y=process_names,
        orientation='h',
        marker=dict(color='#0b67f1'),
    ))

    # Updated layout of the chart
    fig.update_layout(
        title_text='',
        xaxis_title='Time',
        yaxis_title='Processes',
    )

    # Converted the figure to HTML
    chart_div = fig.to_html(full_html=False)

    # Created a results dictionary.
    results = {"chartdiv":chart_div,'execution_state':execution_state,'completiontimes':completiontimes,
               'turnaroundtimes':turnaroundtimes,'waitingtimes':waitingtimes,
               'avg_turnaroundtime':avg_turnaroundtime,'avg_waitingtime':avg_waitingtime,
               'process_list': process_list}
    
    return results


def prepareResultSJF(arrival_times,burst_times):
    """
    var result_dict = {'gantt-chart': gantt_chart_info, 'execution-state': execution_state,
                    'solved_processes_info': solved_processes_info, 'process_list': pplist,
                    'completion-times':completion_times,'turnaround-times':turnaroundtimes,
                    'waiting-times':waitingtimes,'avg_turnaround-time':avg_turnaroundtime,
                   'avg_waiting-time':avg_waitingtime}
    """

    results = {}
    complete_result_dict = SJF(arrival_times,burst_times)
        # print(complete_result_dict)

    # Execution State
    execution_state = complete_result_dict["execution-state"]
    
    # Turn around & Average Turnaround Times.
    turnaroundtimes, avg_turnaroundtime = complete_result_dict["turnaround-times"],complete_result_dict["avg_turnaround-time"]
    # print("\nTurnAround Times:",turnaroundtimes)
    # Waiting time & Average Waiting Times.
    waitingtimes, avg_waitingtime = complete_result_dict["waiting-times"],complete_result_dict["avg_waiting-time"]
    # print("\nWaiting Times:",waitingtimes)
    process_list = complete_result_dict["process_list"]
    completiontimes = complete_result_dict["completion-times"]
    # print("\nProcess List:",process_list)

    # Gantt Chart
    gantt_chart_list = complete_result_dict['gantt-chart']
    gantt_chart_dict = convertListtoDict(gantt_chart_list)
    print(gantt_chart_dict)

    # Separate lists for start and end times
    start_times = [process["start_time"] for process in gantt_chart_dict]
    end_times = [process["end_time"] for process in gantt_chart_dict]
    process_names = [process["name"] for process in gantt_chart_dict]

    # Created a subplot with shared x-axis
    fig = make_subplots(
        rows=1, cols=1,
        subplot_titles=[""],
        shared_xaxes=True,
        vertical_spacing=0.1,
    )

    # Added horizontal bars to the chart
    fig.add_trace(go.Bar(
        x=[start_times, end_times],
        y=process_names,
        orientation='h',
        marker=dict(color='#0b67f1'),
    ))

    # Updated layout of the chart
    fig.update_layout(
        title_text='',
        xaxis_title='Time',
        yaxis_title='Processes',
    )

    # Converted the figure to HTML
    chart_div = fig.to_html(full_html=False)

    # Created a results dictionary.
    results = {"chartdiv":chart_div,'execution_state':execution_state,'completiontimes':completiontimes,
               'turnaroundtimes':turnaroundtimes,'waitingtimes':waitingtimes,
               'avg_turnaroundtime':avg_turnaroundtime,'avg_waitingtime':avg_waitingtime,
               'process_list': process_list}
    
    return results


