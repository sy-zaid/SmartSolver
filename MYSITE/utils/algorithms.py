class process:
    """
    A class defined for running all types of algorithms. It defines all the attributes required by a process.
    
    Attributes:
        process_name (str): The process name or number (e.g. P1, P2, etc)
        arrival_time (int): The arrival time of the process.
        burst_time (int): The burst time of the process.
        priority (int): The priority of the process.
    
    Methods:
    
    Output Requirements:
    
    - Execution Sequence
    - Turn Around Time (for each process)
    --- Formula: Turnaround Time (TAT)=Completion Time−Arrival Time (AT)
    
    - Finish Time (for each process)
    ---  Formula: Finish Time (FT)=Arrival Time (AT)+Turnaround Time (TAT)
    
    - Waiting Time (for each process)
    --- Formula: Waiting Time (WT)=Turnaround Time (TAT)−Burst Time
    
    - Average Turn Around Time
    --- Formula: Average Turnaround Time (AvgTAT)= 
                                                    Number of Processes/
                                            Sum of Turnaround Times of all processes
​

    - Average Waiting Time 
    --- Formula: Average Waiting Time (AvgWT)= 
                                                Number of Processes/
                                            Sum of Waiting Times of all processes
    
    """
    def __init__(self,process_name,arrival_time,burst_time,priority=0):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
    

def mapInputToIntList(lst):
    res = list(map(int,lst.split(",")))
    return res

def calcFinishTime(arrival_times,burst_times,priorities = "default",quantum_time = "default"):
    pass

def FCFS(arrival_times,burst_times):
    num_processes = len(arrival_times)
    process_list = []
    execution_state = []
    completion_time = []

    for i in range(num_processes):  
        process_name = f"Process-{i}"
        process_arrival_time = arrival_times[i]
        process_burst_time = burst_times[i]
        process_list.append(process(process_name,process_arrival_time,process_burst_time))

    # Sorting the processes based on arrivale times.
    sorted_process_list = sorted(process_list,key=lambda x: x.arrival_time)
    
    #Calculating completion time for each process.
    # print(sorted_process_list)
    
    job_que = []
    process_que = []
    # curAT = 0
    
    current_process = None

    total_time = 0
    temp = 0
    for pcs in sorted_process_list:
        total_time+= pcs.burst_time
        temp += pcs.burst_time
        completion_time.append(temp)
    
    print(completion_time)

    current_process = sorted_process_list.pop(0)
    curBT = 0
    prevBT = 0

    for i in range(0,total_time):
        if curBT-prevBT == current_process.burst_time:
            prevBT = curBT
            process_que.pop()
            current_process = sorted_process_list.pop(0)
        
        print('current_process:',current_process.process_name)
        
        if len(process_que) == 0:
            process_que.append(current_process)
            
            
        if len(process_que) > 0:
            job_que.append(current_process)
        
        curBT += 1
        print(curBT)
    

    for p in job_que:
        if p.process_name not in execution_state:
            execution_state.append(p.process_name)
    
    return execution_state



# Input examples from the Front-end.
arrival_times = [12, 1, 1]
burst_times = [1,1,2]       


priorities = [1, 2, 3] # High to Low
# OR
quantum_time = 2
print(FCFS(arrival_times,burst_times))

    
     


