from typing import List, Tuple
def calcAvg(num_processes,timefactor):
        sumTT = sum(timefactor)
        return round(sumTT / num_processes,2)
def get_times(process_list,factor):
        arrival_times = [process[factor] for process in process_list]
        return arrival_times

def PRIORITY(arrival_time: List[int], burst_time: List[int], priorities: List[int]) -> Tuple[List[dict], List[dict]]:
    processes_info = [
        {"process": f"Process-{index}", "arrival_time": at, "burst_time": bt, "priority": priority}
        for index, (at, bt, priority) in enumerate(zip(arrival_time, burst_time, priorities))
    ]

    execution_state = []
    pplist = []
    processes_info.sort(key=lambda x: (x["arrival_time"], x["priority"]))

    solved_processes_info = []
    gantt_chart_info = []

    ready_queue = []
    current_time = processes_info[0]["arrival_time"]
    unfinished_jobs = list(processes_info)

    remaining_time = {process["process"]: process["burst_time"] for process in processes_info}

    ready_queue.append(unfinished_jobs[0])

    while sum(remaining_time.values()) > 0 and unfinished_jobs:
        prev_idle = False

        if len(ready_queue) == 0 and unfinished_jobs:
            prev_idle = True
            ready_queue.append(unfinished_jobs[0])

        ready_queue.sort(key=lambda x: (x["priority"]))

        process_to_execute = ready_queue[0]

        process_at_less_than_bt = [
            p for p in processes_info
            if p["arrival_time"] <= remaining_time[process_to_execute["process"]] + current_time
            and p != process_to_execute
            and p not in ready_queue
            and p in unfinished_jobs
        ]

        got_interruption = False

        for p in process_at_less_than_bt:
            if prev_idle:
                current_time = process_to_execute["arrival_time"]

            amount = p["arrival_time"] - current_time

            if current_time >= p["arrival_time"]:
                ready_queue.append(p)

            if p["priority"] < process_to_execute["priority"]:
                remaining_time[process_to_execute["process"]] -= amount
                ready_queue.append(p)
                prev_current_time = current_time
                current_time += amount
                gantt_chart_info.append({
                    "process": process_to_execute["process"],
                    "start": prev_current_time,
                    "stop": current_time,
                })
                got_interruption = True
                break

        process_to_arrive = [
            p for p in processes_info
            if p["arrival_time"] <= current_time
            and p != process_to_execute
            and p not in ready_queue
            and p in unfinished_jobs
        ]

        ready_queue.extend(process_to_arrive)

        if not got_interruption:
            if prev_idle:
                remaining_t = remaining_time[process_to_execute["process"]]
                remaining_time[process_to_execute["process"]] -= remaining_t
                current_time = process_to_execute["arrival_time"] + remaining_t

                for p in process_at_less_than_bt:
                    if current_time >= p["arrival_time"]:
                        ready_queue.append(p)

                gantt_chart_info.append({
                    "process": process_to_execute["process"],
                    "start": process_to_execute["arrival_time"],
                    "stop": current_time,
                })
            else:
                remaining_t = remaining_time[process_to_execute["process"]]
                remaining_time[process_to_execute["process"]] -= remaining_t
                prev_current_time = current_time
                current_time += remaining_t

                for p in process_at_less_than_bt:
                    if current_time >= p["arrival_time"] and p not in ready_queue:
                        ready_queue.append(p)

                gantt_chart_info.append({
                    "process": process_to_execute["process"],
                    "start": prev_current_time,
                    "stop": current_time,
                })

        # Requeueing (move head/first item to tail/last)
        ready_queue.append(ready_queue.pop(0))
        # Record Execution Start information
        execution_state.append(process_to_execute['process'])
        # Record process details with arrival time only if not already included
        if process_to_execute['process'] not in [details[0] for details in pplist]:
            pplist.append([process_to_execute['process'], process_to_execute['arrival_time'], process_to_execute['burst_time']])

        # When the process finished executing
        if remaining_time[process_to_execute["process"]] == 0:
            unfinished_jobs.remove(process_to_execute)
            ready_queue.remove(process_to_execute)

            solved_processes_info.append({
                **process_to_execute,
                'completion_time': current_time,
                'turnaround_time': current_time - process_to_execute['arrival_time'],
                'waiting_time': current_time - process_to_execute['arrival_time'] - process_to_execute['burst_time'],
            })

    # Sort the processes by job name within arrival time
    solved_processes_info.sort(key=lambda x: (x["arrival_time"], x["process"]))
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

from typing import List

def PRIORITYW(arrival_time: List[int], burst_time: List[int], priorities: List[int]) -> Tuple[List[dict], List[dict]]:
    processes_info = [
        {"process": f"Process-{index}", "arrival_time": at, "burst_time": bt, "priority": priority}
        for index, (at, bt, priority) in enumerate(zip(arrival_time, burst_time, priorities))
    ]

    processes_info.sort(key=lambda x: (x["arrival_time"], x["burst_time"]))

    solved_processes_info = []
    gantt_chart_info = []
    execution_state = []
    pplist = []  # List to store process-name, arrival time, and burst time
    ready_queue = []
    current_time = processes_info[0]["arrival_time"]
    unfinished_process = processes_info.copy()

    remaining_time = {process["process"]: process["burst_time"] for process in processes_info}

    ready_queue.append(unfinished_process[0])

    while sum(remaining_time.values()) > 0 and len(unfinished_process) > 0:
        prev_idle = False
        if len(ready_queue) == 0 and len(unfinished_process) > 0:
            prev_idle = True
            ready_queue.append(unfinished_process[0])

        ready_queue.sort(key=lambda x: remaining_time[x["process"]])

        process_to_execute = ready_queue[0]

        process_at_less_than_bt = [
            p for p in processes_info
            if p["arrival_time"] <= remaining_time[process_to_execute["process"]] + current_time
            and p != process_to_execute
            and p not in ready_queue
            and p in unfinished_process
        ]

        got_interruption = False

        for p in process_at_less_than_bt:
            if prev_idle:
                current_time = process_to_execute["arrival_time"]

            amount = p["arrival_time"] - current_time

            if current_time >= p["arrival_time"]:
                ready_queue.append(p)

            if p["burst_time"] < remaining_time[process_to_execute["process"]] - amount:
                remaining_time[process_to_execute["process"]] -= amount
                ready_queue.append(p)
                prev_current_time = current_time
                current_time += amount

                # Record Gantt Chart information
                gantt_chart_info.append([prev_current_time, process_to_execute['process'], current_time])
                got_interruption = True
                break

        process_to_arrive = [
            p for p in processes_info
            if p["arrival_time"] <= current_time
            and p != process_to_execute
            and p not in ready_queue
            and p in unfinished_process
        ]

        ready_queue.extend(process_to_arrive)

        if not got_interruption:
            if prev_idle:
                remaining_t = remaining_time[process_to_execute["process"]]
                remaining_time[process_to_execute["process"]] -= remaining_t
                current_time = process_to_execute["arrival_time"] + remaining_t

                for p in process_at_less_than_bt:
                    if current_time >= p["arrival_time"]:
                        ready_queue.append(p)

                gantt_chart_info.append([process_to_execute["arrival_time"], process_to_execute['process'], current_time])
            else:
                remaining_t = remaining_time[process_to_execute["process"]]
                remaining_time[process_to_execute["process"]] -= remaining_t
                prev_current_time = current_time
                current_time += remaining_t

                for p in process_at_less_than_bt:
                    if current_time >= p["arrival_time"] and p not in ready_queue:
                        ready_queue.append(p)

                gantt_chart_info.append([prev_current_time, process_to_execute['process'], current_time])

        # Requeueing (move head/first item to tail/last)
        ready_queue.append(ready_queue.pop(0))

        # Record Execution Start information
        execution_state.append(process_to_execute['process'])
        # Record process details with arrival time only if not already included
        if process_to_execute['process'] not in [details[0] for details in pplist]:
            pplist.append([process_to_execute['process'], process_to_execute['arrival_time'], process_to_execute['burst_time']])

        # When the process finished executing
        if remaining_time[process_to_execute["process"]] == 0:
            index_to_remove_uj = unfinished_process.index(process_to_execute)
            if index_to_remove_uj > -1:
                unfinished_process.pop(index_to_remove_uj)
            index_to_remove_rq = next(
                (i for i, p in enumerate(ready_queue) if p["process"] == process_to_execute["process"]),
                None
            )
            if index_to_remove_rq is not None:
                ready_queue.pop(index_to_remove_rq)

            solved_processes_info.append({
                **process_to_execute,
                'completion_time': current_time,
                'turnaround_time': current_time - process_to_execute['arrival_time'],
                'waiting_time': current_time - process_to_execute['arrival_time'] - process_to_execute['burst_time'],
            })

    # Sort the processes by process name within arrival time
    solved_processes_info.sort(key=lambda x: (x["arrival_time"], x["process"]))

    completion_times = get_times(solved_processes_info, 'completion_time')
    turnaround_times = get_times(solved_processes_info, 'turnaround_time')
    waiting_times = get_times(solved_processes_info, 'waiting_time')

    avg_waiting_time = calcAvg(len(arrival_time), waiting_times)
    avg_turnaround_time = calcAvg(len(arrival_time), turnaround_times)

    result_dict = {'gantt-chart': gantt_chart_info, 'execution-state': execution_state,
                   'solved_processes_info': solved_processes_info, 'process_list': pplist,
                   'completion-times': completion_times, 'turnaround-times': turnaround_times,
                   'waiting-times': waiting_times, 'avg_turnaround-time': avg_turnaround_time,
                   'avg_waiting-time': avg_waiting_time}
    return result_dict

# Example usage:
arrival_time = [0, 2, 4]
burst_time = [5, 3, 1]
priorities = [3, 2, 1]

result = PRIORITY(arrival_time, burst_time, priorities)
print("Solved Processes Info:", result)
# print("Gantt Chart Info:", result[1])
