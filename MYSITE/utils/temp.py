from typing import List, Dict, Union

def rr(arrival_time: List[int], burst_time: List[int], time_quantum: int) -> Dict[str, Union[List[List[Union[str, int]]], List[str]]]:
    processes_info = [
        {'process': f"Process-{index}", 'arrival_time': arrival_time[index], 'burst_time': burst_time[index]}
        for index in range(len(arrival_time))
    ]

    processes_info.sort(key=lambda x: (x['arrival_time'], x['process']))

    solved_processes_info = []
    gantt_chart_info = []
    execution_state = []
    process_details = []  # New list to store process-name, arrival time, and burst time
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

        # Record Gantt Chart informarrival_timeion
        gantt_chart_info.append([start_time, process_to_execute['process'], current_time])

        # Record Execution Starrival_timee informarrival_timeion
        execution_state.append(process_to_execute['process'])

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
    
    def get_arrival_times(process_list):
        arrival_times = [process['arrival_time'] for process in process_list]
        return arrival_times

    pplist = get_arrival_times(solved_processes_info)
    print("\nPPLIST",pplist)
    result_dict = {'gantt_chart': gantt_chart_info, 'execution_state': execution_state,'solved_processes_info':solved_processes_info}
    return result_dict

# Example usage:
arrival_time = [0, 2, 4]
burst_time = [5, 3, 8]
time_quantum = 3

result = rr(arrival_time, burst_time, time_quantum)
print(result)



