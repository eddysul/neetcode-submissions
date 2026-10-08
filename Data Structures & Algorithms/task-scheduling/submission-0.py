class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # hashmap to hold freqs of tasks, then start with task with highest freq
        # have hashmap store counts
        # Use heap to obtain most frequent task
        # Use queue to hold waiting tasks

        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0
        # Intuition
        # Max heap always holds current tasks that can be run (tasks that are out of cooldown period)
        # Queue holds the tasks that are in the current cooldown period
        while max_heap or q:
            time += 1

            if not max_heap: # Saying all tasks are in cooldown period, so (this counts for idles) skip to next time where task can be executed
                time = q[0][1]
            else: # Saying there is a task to be executed currently 
                cnt = heapq.heappop(max_heap)+1 # +1 b/c max heap is minus so closer to 0
                if cnt: # there is still another task after we process this one
                    q.append([cnt, time+n]) # we processed current task so we add back to cooldown queue
            if q and q[0][1] == time: # this means cooldown is over, so we take out of queue and its ready to be picked from maxHeap
                heapq.heappush(max_heap, q.popleft()[0])

        return time
        
        