from .Process_classes import process_list

def FCFS(inp_arrival_times, inp_burst_times):

    """
    Function for the FCFS algorithm.
    
    VARIABLES:
    - inp_arrival_time: A list of all the arrival times given by the user.
    - inp_burst_time: A list of all the burst times given by the user.
    
    OUTPUT REQUIREMENTS:
    
    1- Gantt Chart (Nested List).

    2- Execution Sequence (List).
    
    3- Completion/ Finish Time - for each process (List)
    --- Formula: Completion Time (CT) = calculated by the FCFS function itself and outputs as a list.

    4- Turn Around Time (for each process)
    --- Formula: Turnaround Time (TAT) = Completion Time - Arrival Time (AT)
    
    5- Waiting Time (for each process)
    --- Formula: Waiting Time (WT) = Turnaround Time (TAT) - Burst Time
    
    6- Average Turn Around Time
    --- Formula: Average Turnaround Time (AvgTAT) = 
                    Number of Processes / Sum of Turnaround Times of all processes

    7- Average Waiting Time 
    --- Formula: Average Waiting Time (AvgWT) = 
                    Number of Processes / Sum of Waiting Times of all processes
    """

    result_dict = {}
    inp_process_list = process_list(inp_arrival_times, inp_burst_times)

    inp_process_list.createprocessList()
    # print("Unsorted Process List:", inp_process_list.__getlist__(), '\n\n')

    # Sorting the input process list.
    inp_process_list.sortListByArrivalTime()
    # print("Sorted Process List:", inp_process_list.__getlist__(), '\n\n')

    # Var for storing the process list with name,arrival,burst times.
    pplist = inp_process_list.__getlist__()

    # Current Burst Time, Previous Burst Time
    curBT, prevBT = 0, 0
    # Current Process. (Will get updated in the loop as one process is picked from the list.)
    curProcess = 0
    # Stores current process's arrival time.
    processAT= 0
    # Time pointer for updating the Gantt Chart.
    time_pointer = 0

    # Vars used for storing Idle Time and Total Idle Time.
    idleTime, total_idle_time = 0, 0

    gantt_chart = []  # [[Process_name,Start_Time, Completion_Time]]
    execution_state = []
    completion_times = []

    for process_num in range(0,inp_process_list.length()):
        curProcess = inp_process_list.__getprocess__(process_num)
        processAT = curProcess.arrival_time

        if processAT > time_pointer: # FOR IDLE TIME
            idleTime = processAT - time_pointer
            time_pointer += total_idle_time
            total_idle_time += idleTime
            gantt_chart.append([processAT-idleTime, 'Idle', processAT])
        
        if processAT < time_pointer:
            processAT = time_pointer

        time_pointer = processAT + curProcess.burst_time
        
        completion_times.append(time_pointer)
        # print("Completion Time",completion_times)
        
        gantt_chart.append([processAT, curProcess.process_name,time_pointer])
        curBT = curProcess.burst_time + prevBT
        prevBT += curBT
        
    
    # print("Completion Time",completion_times)
        
    execution_state = [entry[1] for entry in gantt_chart if entry[1] != "Idle"]

    # print(inp_process_list.__getarrivaltimes__())
    turnaroundtimes = inp_process_list.calcTurnAroundTime(completion_times)
    # print(turnaroundtimes)
    
    avg_turnaroundtime = inp_process_list.calcAvgTurnAroundTime(turnaroundtimes)
    # print("AVGTT",inp_process_list.calcAvgTurnAroundTime(turnaroundtimes))
    
    waitingtimes = inp_process_list.calcWaitingTime(turnaroundtimes)
    # print(inp_process_list.calcWaitingTime(turnaroundtimes))
    
    avg_waitingtime = inp_process_list.calcAvgWaitingTime(waitingtimes)
    # print(inp_process_list.__getlist__())
    print('GC',gantt_chart)

    result_dict = {'gantt-chart':gantt_chart,'execution-state':execution_state,
                   'completion-times':completion_times,'turnaround-times':turnaroundtimes,
                   'waiting-times':waitingtimes,'avg_turnaround-time':avg_turnaroundtime,
                   'avg_waiting-time':avg_waitingtime,'process_list': pplist
                   }
    
    return result_dict


# arrival_times = [0,10,2,2]
# burst_times = [2,3,3,1]
# input1 = FCFS(arrival_times, burst_times)


# arrival_times = [6,5,4,1]
# burst_times = [2,3,2,1]
# print(FCFS(arrival_times, burst_times))