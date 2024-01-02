from typing import List, Dict

def rr(arrival_time: List[int], burst_time: List[int], time_quantum: int) -> Dict[str, List[Dict[str, int]]]:
    processes_info = [
        {'job': chr(index + 10 + 65), 'at': arrival_time[index], 'bt': burst_time[index]}
        for index in range(len(arrival_time))
    ]
    
    processes_info.sort(key=lambda x: (x['at'], x['job']))
    
    solved_processes_info = []
    gantt_chart_info = []

    ready_queue = []
    current_time = processes_info[0]['at']
    unfinished_jobs = processes_info.copy()

    remaining_time = {process['job']: process['bt'] for process in processes_info}

    ready_queue.append(unfinished_jobs[0])
    
    while any(remaining_time.values()) and unfinished_jobs:
        if not ready_queue and unfinished_jobs:
            # Previously idle
            ready_queue.append(unfinished_jobs[0])
            current_time = ready_queue[0]['at']

        process_to_execute = ready_queue[0]

        if remaining_time[process_to_execute['job']] <= time_quantum:
            # Burst time less than or equal to time quantum, execute until finished
            remaining_t = remaining_time[process_to_execute['job']]
            remaining_time[process_to_execute['job']] -= remaining_t
            prev_current_time = current_time
            current_time += remaining_t

            gantt_chart_info.append({
                'job': process_to_execute['job'],
                'start': prev_current_time,
                'stop': current_time,
            })
        else:
            remaining_time[process_to_execute['job']] -= time_quantum
            prev_current_time = current_time
            current_time += time_quantum

            gantt_chart_info.append({
                'job': process_to_execute['job'],
                'start': prev_current_time,
                'stop': current_time,
            })

        processes_to_arrive_in_this_cycle = [
            p for p in processes_info
            if p['at'] <= current_time and p != process_to_execute and p not in ready_queue and p in unfinished_jobs
        ]

        # Push new processes to ready_queue
        ready_queue.extend(processes_to_arrive_in_this_cycle)

        # Requeuing (move head/first item to tail/last)
        ready_queue.append(ready_queue.pop(0))

        # When the process finished executing
        if remaining_time[process_to_execute['job']] == 0:
            unfinished_jobs.remove(process_to_execute)
            ready_queue.remove(process_to_execute)

            solved_processes_info.append({
                **process_to_execute,
                'ft': current_time,
                'tat': current_time - process_to_execute['at'],
                'wat': current_time - process_to_execute['at'] - process_to_execute['bt'],
            })

    # Sort the processes by arrival time and then by job name
    solved_processes_info.sort(key=lambda x: (x['at'], x['job']))

    return {'solved_processes_info': solved_processes_info, 'gantt_chart_info': gantt_chart_info}

# Example usage:
arrival_time = [0, 2, 4]
burst_time = [5, 3, 8]
time_quantum = 3

result = rr(arrival_time, burst_time, time_quantum)
print(result['solved_processes_info'])
print(result['gantt_chart_info'])
