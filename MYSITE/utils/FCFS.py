from Process_classes import process_list

def FCFS(inp_arrival_times, inp_burst_times):
    inp_process_list = process_list(inp_arrival_times, inp_burst_times)

    inp_process_list.createprocessList()
    # print("Unsorted Process List:", inp_process_list.__getlist__(), '\n\n')

    # Sorting the input process list.
    inp_process_list.sortListByArrivalTime()
    # print("Sorted Process List:", inp_process_list.__getlist__(), '\n\n')

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

    for process_num in range(0,inp_process_list.length()):
        curProcess = inp_process_list.__getprocess__(process_num)
        processAT = curProcess.arrival_time
        

        print("Current Process", curProcess.process_name)
        print("ProcessAT, curBT, prevBT", processAT, curBT, prevBT,time_pointer)
        print("Timepointer:",time_pointer)

        if processAT > time_pointer:
            idleTime = processAT - time_pointer
            
            time_pointer += total_idle_time
            total_idle_time += idleTime
            gantt_chart.append([processAT-idleTime, 'Idle',idleTime, time_pointer,total_idle_time])
        
        if processAT < time_pointer:
            processAT = time_pointer

        time_pointer = processAT + curProcess.burst_time # 3,
        
        gantt_chart.append([processAT, curProcess.process_name,time_pointer])
        curBT = curProcess.burst_time + prevBT
        prevBT += curBT
        

    print("Gantt Chart:", gantt_chart)
    print("Execution Sequence:", [entry[1] for entry in gantt_chart])


arrival_times = [0,2,2,2]
burst_times = [2,3,3,10]
input1 = FCFS(arrival_times, burst_times)