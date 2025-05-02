queue_size = int(input("Enter the size of the queue: "))
number_of_requests = int(input("Enter the number of requests: "))
initial_head_position = int(input("Enter the initial head position: "))
number_of_cylinders = int(input('Enter the number of cylinders: '))
algorithm_to_be_used = input('Enter the algorithm to be used (F: FCFS | S: Scan | C: C-Scan): ').upper()
step_cylinder_time = float(input('Enter the time taken to move from one cylinder to another: '))

def fcfs(requests, head, step_time):
    order = [head]
    total_movement = 0

    for req in requests:
        movement = abs(req - head)
        total_movement += movement
        head = req
        order.append(req)

    total_seek_time = total_movement * step_time
    return order, total_movement, total_seek_time




def scan_algorithm(requests, head, direction, disk_size, step_time):
    requests.sort()
    total_head_movement = 0
    seek_sequence = []

    if direction == "left":
        left = [r for r in requests if r < head]
        right = [r for r in requests if r >= head]
        
        left.reverse()
        for r in left:
            total_head_movement += abs(head - r)
            head = r
            seek_sequence.append(r)

        if right:
            total_head_movement += head  # move to 0
            head = 0
            for r in right:
                total_head_movement += abs(head - r)
                head = r
                seek_sequence.append(r)

    elif direction == "right":
        left = [r for r in requests if r < head]
        right = [r for r in requests if r >= head]

        for r in right:
            total_head_movement += abs(head - r)
            head = r
            seek_sequence.append(r)

        if left:
            total_head_movement += abs((disk_size - 1) - head)
            head = disk_size - 1
            left.reverse()
            for r in left:
                total_head_movement += abs(head - r)
                head = r
                seek_sequence.append(r)

    total_seek_time = total_head_movement * step_time

    return seek_sequence, total_head_movement, total_seek_time


def cscan(requests, head, disk_size, step_time):
    requests.sort()
    seek_sequence = []
    total_head_movement = 0

    # Separate requests into those greater and less than head
    left = [req for req in requests if req < head]
    right = [req for req in requests if req >= head]

    # Service requests to the right of head
    for req in right:
        total_head_movement += abs(head - req)
        head = req
        seek_sequence.append(req)

    # Move head to the end of the disk (simulate circular jump to beginning)
    if right:
        total_head_movement += abs(head - (disk_size - 1))
        head = 0
        total_head_movement += abs((disk_size - 1) - head)

    # Service requests to the left
    for req in left:
        total_head_movement += abs(head - req)
        head = req
        seek_sequence.append(req)

    total_seek_time = total_head_movement * step_time

    return seek_sequence, total_head_movement, total_seek_time