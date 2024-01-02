from typing import List, Dict

def rr(arrival_time: List[int], burst_time: List[int], time_quantum: int) -> Dict[str, List[Dict[str, int]]]:
    processes_info = [
        {'process': chr(index + 10 + 65), 'at': arrival_time[index], 'bt': burst_time[index]}
        for index in range(len(arrival_time))
    ]
    
    processes_info.sort(key=lambda x: (x['at'], x['process']))
    
    solved_processes_info = []
    gantt_chart_info = []

    ready_queue = []
    current_time = processes_info[0]['at']
    unfinished_processs = processes_info.copy()

    remaining_time = {process['process']: process['bt'] for process in processes_info}

    ready_queue.append(unfinished_processs[0])
    
    while any(remaining_time.values()) and unfinished_processs:
        if not ready_queue and unfinished_processs:
            # Previously idle
            ready_queue.append(unfinished_processs[0])
            current_time = ready_queue[0]['at']

        process_to_execute = ready_queue[0]

        if remaining_time[process_to_execute['process']] <= time_quantum:
            # Burst time less than or equal to time quantum, execute until finished
            remaining_t = remaining_time[process_to_execute['process']]
            remaining_time[process_to_execute['process']] -= remaining_t
            prev_current_time = current_time
            current_time += remaining_t

            gantt_chart_info.append({
                'process': process_to_execute['process'],
                'start': prev_current_time,
                'stop': current_time,
            })
        else:
            remaining_time[process_to_execute['process']] -= time_quantum
            prev_current_time = current_time
            current_time += time_quantum

            gantt_chart_info.append({
                'process': process_to_execute['process'],
                'start': prev_current_time,
                'stop': current_time,
            })

        processes_to_arrive_in_this_cycle = [
            p for p in processes_info
            if p['at'] <= current_time and p != process_to_execute and p not in ready_queue and p in unfinished_processs
        ]

        # Push new processes to ready_queue
        ready_queue.extend(processes_to_arrive_in_this_cycle)

        # Requeuing (move head/first item to tail/last)
        ready_queue.append(ready_queue.pop(0))

        # When the process finished executing
        if remaining_time[process_to_execute['process']] == 0:
            unfinished_processs.remove(process_to_execute)
            ready_queue.remove(process_to_execute)

            solved_processes_info.append({
                **process_to_execute,
                'ft': current_time,
                'tat': current_time - process_to_execute['at'],
                'wat': current_time - process_to_execute['at'] - process_to_execute['bt'],
            })

    # Sort the processes by arrival time and then by process name
    solved_processes_info.sort(key=lambda x: (x['at'], x['process']))

    return {'solved_processes_info': solved_processes_info, 'gantt_chart_info': gantt_chart_info}

# Example usage:
arrival_time = [0, 2, 4]
burst_time = [5, 3, 8]
time_quantum = 3

result = rr(arrival_time, burst_time, time_quantum)
# print(result['solved_processes_info'])
print(result['gantt_chart_info'])
