queue_size = input("Enter the size of the queue: ")
number_of_requests = int(input("Enter the number of requests: "))
initial_head_posizison = input("Enter the initial head position: ")
number_of_ylinders = input('Enter the number of cylinders: ')
algorithm_to_be_used = input('Enter the algorithm to be used(F:FCFD | S:Scan| C:CScan): ')
step_cylinder_time = input('Enter the time taken to move from one cylinder to another: ')


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
