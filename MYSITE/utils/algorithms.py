from .FCFS import FCFS

def mapInputToIntList(lst):
    res = list(map(int,lst.split(",")))
    return res

def calcFinishTime(arrival_times,burst_times,priorities = "default",quantum_time = "default"):
    pass

def prepareResultFCFS(arrival_times,burst_times):
    return FCFS(arrival_times,burst_times)


def convertListtoDict(gantt_chart_list):
    converted_list = []

    for entry in gantt_chart_list:
        entry_dict = {'name': entry[1], 'start_time': entry[0]}
        entry_dict['end_time'] = entry[2]
        converted_list.append(entry_dict)

    return converted_list

# gantt_chart_list = [[0, 'Idle', 1], [1, 'Process-1', 3], [3, 'Process-2', 6], [6, 'Idle', 12], [12, 'Process-0', 13]]
# print(convertListtoDict(gantt_chart_list))


