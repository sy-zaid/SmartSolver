from typing import List, Tuple

solved_processes_info_type = List[dict]
gantt_chart_info_type = List[dict]


def pp(arrival_time: List[int], burst_time: List[int], priorities: List[int]) -> Tuple[solved_processes_info_type, gantt_chart_info_type]:
    processes_info = [
        {'job': f"process-{index}", 'at': at, 'bt': bt, 'priority': priority}
        for index, (at, bt, priority) in enumerate(zip(arrival_time, burst_time, priorities))
    ]

    processes_info.sort(key=lambda x: (x['at'], x['priority']))

    solved_processes_info = []
    gantt_chart_info = []

    ready_queue = []
    current_time = processes_info[0]['at']
    unfinished_jobs = processes_info[:]

    remaining_time = {process['job']: process['bt'] for process in processes_info}

    ready_queue.append(unfinished_jobs[0])

    while sum(remaining_time.values()) > 0 and unfinished_jobs:
        prev_idle = False

        if not ready_queue and unfinished_jobs:
            prev_idle = True
            ready_queue.append(unfinished_jobs[0])

        ready_queue.sort(key=lambda x: x['priority'])

        process_to_execute = ready_queue[0]

        process_at_less_than_bt = [
            p for p in processes_info
            if p['at'] <= remaining_time[process_to_execute['job']] + current_time
            and p != process_to_execute
            and p not in ready_queue
            and p in unfinished_jobs
        ]

        got_interruption = False

        for p in process_at_less_than_bt:
            if prev_idle:
                current_time = process_to_execute['at']

            amount = p['at'] - current_time

            if current_time >= p['at']:
                ready_queue.append(p)

            if p['priority'] < process_to_execute['priority']:
                remaining_time[process_to_execute['job']] -= amount
                ready_queue.append(p)
                prev_current_time = current_time
                current_time += amount
                gantt_chart_info.append({
                    'job': process_to_execute['job'],
                    'start': prev_current_time,
                    'stop': current_time,
                })
                got_interruption = True
                break

        process_to_arrive = [
            p for p in processes_info
            if p['at'] <= current_time
            and p != process_to_execute
            and p not in ready_queue
            and p in unfinished_jobs
        ]

        ready_queue.extend(process_to_arrive)

        if not got_interruption:
            if prev_idle:
                remaining_t = remaining_time[process_to_execute['job']]
                remaining_time[process_to_execute['job']] -= remaining_t
                current_time = process_to_execute['at'] + remaining_t

                for p in process_at_less_than_bt:
                    if current_time >= p['at']:
                        ready_queue.append(p)

                gantt_chart_info.append({
                    'job': process_to_execute['job'],
                    'start': process_to_execute['at'],
                    'stop': current_time,
                })
            else:
                remaining_t = remaining_time[process_to_execute['job']]
                remaining_time[process_to_execute['job']] -= remaining_t
                prev_current_time = current_time
                current_time += remaining_t

                for p in process_at_less_than_bt:
                    if current_time >= p['at'] and p not in ready_queue:
                        ready_queue.append(p)

                gantt_chart_info.append({
                    'job': process_to_execute['job'],
                    'start': prev_current_time,
                    'stop': current_time,
                })

        ready_queue.append(ready_queue.pop(0))

        if remaining_time[process_to_execute['job']] == 0:
            unfinished_jobs.remove(process_to_execute)
            ready_queue.remove(process_to_execute)

            solved_processes_info.append({
                **process_to_execute,
                'ft': current_time,
                'tat': current_time - process_to_execute['at'],
                'wat': current_time - process_to_execute['at'] - process_to_execute['bt'],
            })

    solved_processes_info.sort(key=lambda x: (x['at'], x['job']))

    return solved_processes_info, gantt_chart_info


# # Example usage:
# arrival_time = [0, 1, 2]
# burst_time = [4, 3, 2]
# priorities = [2, 1, 3]

# result = pp(arrival_time, burst_time, priorities)
# print(result)



arrival_time = [6,5,4,1]
burst_time = [2,3,2,1]
priorities = [1,2,3,2]

result = pp(arrival_time, burst_time, priorities)
print("\n\n", result)