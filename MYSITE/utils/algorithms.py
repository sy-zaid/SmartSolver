class process:
    """
    A class defined for running all types of algorithms. It defines all the attributes required by a process.
    
    Attributes:
        process_name (str): The process name or number (e.g. P1, P2, etc)
        arrival_time (int): The arrival time of the process.
        burst_time (int): The burst time of the process.
        priority (int): The priority of the process.
    
    Methods:
        
    
    """
    def __init__(self,process_name,arrival_time,burst_time,priority=0):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
    



def FCFS(arrival_times,burst_times):

    num_processes = len(arrival_times)
    process_list = []
    execution_state = []

    for i in range(num_processes):
        process_name = f"Process-{i}"
        process_arrival_time = arrival_times[i]
        process_burst_time = burst_times[i]
        process_list.append(process(process_name,process_arrival_time,process_burst_time))

    process_list = sorted(process_list,key=lambda x: x.arrival_time)
    job_que = []
    process_que = []
    curAT = 0
    
    current_process = None

    total_time = 0
    for ats in process_list:
        total_time+= ats.burst_time

    current_process = process_list.pop(0)
    curBT = 0
    prevBT = 0

    for i in range(0,total_time):
        if curBT-prevBT == current_process.burst_time:
            prevBT = curBT
            process_que.pop()
            current_process = process_list.pop(0)
        
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

# FCFS([1,2,3],[1,2,3])

    
     


