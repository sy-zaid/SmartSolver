from .Process_classes import process_list

def SJF(inp_arrival_times, inp_burst_times):

    result_dict = {}
    inp_process_list = process_list(inp_arrival_times, inp_burst_times)

    inp_process_list.createprocessList()
    inp_process_list.sortListByBurstTime()

    pplist = inp_process_list.__getlist__()

    curBT, prevBT = 0, 0
    curProcess = 0
    processAT = 0
    time_pointer = 0
    idleTime, total_idle_time = 0, 0

    gantt_chart = []  # [[Process_name, Start_Time, Completion_Time]]
    execution_state = []
    completion_times = []

    for process_num in range(0, inp_process_list.length()):
        curProcess = inp_process_list.__getprocess__(process_num)
        processAT = curProcess.burst_time

        if processAT > time_pointer:  # FOR IDLE TIME
            idleTime = processAT - time_pointer
            time_pointer += total_idle_time
            total_idle_time += idleTime
            gantt_chart.append([processAT - idleTime, 'Idle', processAT])

        if processAT < time_pointer:
            processAT = time_pointer

        time_pointer = processAT + curProcess.burst_time

        completion_times.append(time_pointer)
        gantt_chart.append([processAT, curProcess.process_name, time_pointer])
        curBT = curProcess.burst_time + prevBT
        prevBT += curBT

    execution_state = [entry[1] for entry in gantt_chart if entry[1] != "Idle"]

    turnaroundtimes = inp_process_list.calcTurnAroundTime(completion_times)
    avg_turnaroundtime = inp_process_list.calcAvgTurnAroundTime(turnaroundtimes)

    waitingtimes = inp_process_list.calcWaitingTime(turnaroundtimes)
    avg_waitingtime = inp_process_list.calcAvgWaitingTime(waitingtimes)

    result_dict = {'gantt-chart': gantt_chart, 'execution-state': execution_state,
                   'completion-times': completion_times, 'turnaround-times': turnaroundtimes,
                   'waiting-times': waitingtimes, 'avg_turnaround-time': avg_turnaroundtime,
                   'avg_waiting-time': avg_waitingtime, 'process_list': pplist
                   }

    return result_dict

# arrival_times = [0,10,2,2]
# burst_times = [2,3,3,1]
# input1 = SJF(arrival_times, burst_times)
# print(input1)
