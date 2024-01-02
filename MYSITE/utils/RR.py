from typing import List, Dict, Union
def get_times(process_list,factor):
        arrival_times = [process[factor] for process in process_list]
        return arrival_times

def calcAvg(num_processes,timefactor):
        sumTT = sum(timefactor)
        return round(sumTT / num_processes,2)

def RR(arrival_time: List[int], burst_time: List[int], time_quantum: int) -> Dict[str, Union[List[List[Union[str, int]]], List[str]]]:
    processes_info = [
        {'process': f"Process-{index}", 'arrival_time': arrival_time[index], 'burst_time': burst_time[index]}
        for index in range(len(arrival_time))
    ]

    processes_info.sort(key=lambda x: (x['arrival_time'], x['process']))

    solved_processes_info = []
    gantt_chart_info = []
    execution_state = []
    pplist = []  # New list to store process-name, arrival time, and burst time
    processed_processes = set()  # Keep track of processed processes
    ready_queue = []
    current_time = processes_info[0]['arrival_time']
    unfinished_processes = processes_info.copy()

    remaining_time = {process['process']: process['burst_time'] for process in processes_info}

    ready_queue.append(unfinished_processes[0])

    while any(remaining_time.values()) and unfinished_processes:
        if not ready_queue and unfinished_processes:
            # Previously idle
            ready_queue.append(unfinished_processes[0])
            current_time = ready_queue[0]['arrival_time']

        process_to_execute = ready_queue[0]

        start_time = current_time

        if remaining_time[process_to_execute['process']] <= time_quantum:
            # Burst time less than or equal to time quantum, execute until finished
            remaining_t = remaining_time[process_to_execute['process']]
            remaining_time[process_to_execute['process']] -= remaining_t
            current_time += remaining_t
        else:
            remaining_time[process_to_execute['process']] -= time_quantum
            current_time += time_quantum

        # Record Gantt Chart information
        gantt_chart_info.append([start_time, process_to_execute['process'], current_time])

        # Record Execution Start information
        execution_state.append(process_to_execute['process'])

        
        # Record process details with arrival time only if not already included
        if process_to_execute['process'] not in [details[0] for details in pplist]:
            pplist.append([process_to_execute['process'], process_to_execute['arrival_time'], process_to_execute['burst_time']])


        processes_to_arrive_in_this_cycle = [
            p for p in processes_info
            if p['arrival_time'] <= current_time and p != process_to_execute and p not in ready_queue and p in unfinished_processes
        ]

        # Push new processes to ready_queue
        ready_queue.extend(processes_to_arrive_in_this_cycle)

        # Requeuing (move head/first item to tail/last)
        ready_queue.append(ready_queue.pop(0))

        # When the process finished executing
        if remaining_time[process_to_execute['process']] == 0:
            unfinished_processes.remove(process_to_execute)
            ready_queue.remove(process_to_execute)

            solved_processes_info.append({
                **process_to_execute,
                'completion_time': current_time,
                'turnaround_time': current_time - process_to_execute['arrival_time'],
                'waiting_time': current_time - process_to_execute['arrival_time'] - process_to_execute['burst_time'],
            })

    # Sort the processes by arrival time and then by process name
    gantt_chart_info.sort(key=lambda x: (x[0], x[1]))
    execution_state.append("Finish")
    
    completion_times = get_times(solved_processes_info,'completion_time')
    # print("\n",completion_times)

    turnaroundtimes = get_times(solved_processes_info,'turnaround_time')
    # print('\n',turnaroundtimes)

    waitingtimes = get_times(solved_processes_info,'waiting_time')
    # print('\n',waitingtimes)

    avg_waitingtime = calcAvg(len(arrival_time),waitingtimes)
    avg_turnaroundtime = calcAvg(len(arrival_time),turnaroundtimes)

    
    result_dict = {'gantt-chart': gantt_chart_info, 'execution-state': execution_state,
                    'solved_processes_info': solved_processes_info, 'process_list': pplist,
                    'completion-times':completion_times,'turnaround-times':turnaroundtimes,
                    'waiting-times':waitingtimes,'avg_turnaround-time':avg_turnaroundtime,
                   'avg_waiting-time':avg_waitingtime}
    return result_dict

# arrival_time = [0, 2, 4]
# burst_time = [5, 3, 8]
# time_quantum = 3

# result = RR(arrival_time, burst_time, time_quantum)
# print(result)


