from typing import List, Dict

def npp(arrival_time: List[int], burst_time: List[int], priorities: List[int]) -> Dict[str, List[Dict[str, int]]]:
    processes_info = [
        {
            'job': f"process-{index}",
            'at': arrival_time[index],
            'bt': burst_time[index],
            'priority': priorities[index]
        }
        for index in range(len(arrival_time))
    ]

    processes_info.sort(key=lambda x: (x['at'], x['priority']))

    finish_time = []
    gantt_chart_info = []

    solved_processes_info = []
    ready_queue = []
    finished_jobs = []

    for i in range(len(processes_info)):
        if i == 0:
            ready_queue.append(processes_info[0])
            finish_time.append(processes_info[0]['at'] + processes_info[0]['bt'])
            solved_processes_info.append({
                **processes_info[0],
                'ft': finish_time[0],
                'tat': finish_time[0] - processes_info[0]['at'],
                'wat': finish_time[0] - processes_info[0]['at'] - processes_info[0]['bt']
            })

            for p in processes_info:
                if p['at'] <= finish_time[0] and p not in ready_queue:
                    ready_queue.append(p)

            ready_queue.pop(0)
            finished_jobs.append(processes_info[0])

            gantt_chart_info.append({
                'job': processes_info[0]['job'],
                'start': processes_info[0]['at'],
                'stop': finish_time[0]
            })
        else:
            if not ready_queue and len(finished_jobs) != len(processes_info):
                unfinished_jobs = [
                    p for p in processes_info if p not in finished_jobs
                ]
                unfinished_jobs.sort(key=lambda x: (x['at'], x['priority']))
                ready_queue.append(unfinished_jobs[0])

            rq_sorted_by_priority = sorted(ready_queue, key=lambda x: (x['priority'], x['at']))

            process_to_execute = rq_sorted_by_priority[0]
            previous_finish_time = finish_time[-1]

            if process_to_execute['at'] > previous_finish_time:
                finish_time.append(process_to_execute['at'] + process_to_execute['bt'])
                newest_finish_time = finish_time[-1]
                gantt_chart_info.append({
                    'job': process_to_execute['job'],
                    'start': process_to_execute['at'],
                    'stop': newest_finish_time
                })
            else:
                finish_time.append(previous_finish_time + process_to_execute['bt'])
                newest_finish_time = finish_time[-1]
                gantt_chart_info.append({
                    'job': process_to_execute['job'],
                    'start': previous_finish_time,
                    'stop': newest_finish_time
                })

            solved_processes_info.append({
                **process_to_execute,
                'ft': newest_finish_time,
                'tat': newest_finish_time - process_to_execute['at'],
                'wat': newest_finish_time - process_to_execute['at'] - process_to_execute['bt']
            })

            for p in processes_info:
                if p['at'] <= newest_finish_time and p not in ready_queue and p not in finished_jobs:
                    ready_queue.append(p)

            index_to_remove = ready_queue.index(process_to_execute)
            if index_to_remove > -1:
                ready_queue.pop(index_to_remove)

            finished_jobs.append(process_to_execute)

    solved_processes_info.sort(key=lambda x: (x['at'], x['job']))

    return {'solved_processes_info': solved_processes_info, 'gantt_chart_info': gantt_chart_info}


# Example usage:
arrival_time = [1,4,5,6]
burst_time = [1,2,3,2]
priorities = [2,3,2,1]

result = npp(arrival_time, burst_time, priorities)
print(result)
