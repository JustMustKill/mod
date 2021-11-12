import random as rand


def event(probability):
    return rand.uniform(0, 1) <= probability

# initial parameters
pi1 = 0
pi2 = 0
iters_num = 0

# flags
p1_event = False
p2_event = False

request_from_pi1 = False
request_from_queue = False
request_from_source = False

while (1):
    pi1 = input('Enter pi1: ')
    try:
        pi1 = float(pi1)
        if pi1 >= 0.0 and pi1 <= 1.0:
            break
    except ValueError:
        pass
    print('Check your input!')

while (1):
    pi2 = input('Enter pi2: ')
    try:
        pi2 = float(pi2)
        if pi2 >= 0.0 and pi2 <= 1.0:
            break
    except ValueError:
        pass
    print('Check your input!')

while (1):
    iters_num = input('Enter amount of iterations: ')
    try:
        iters_num = int(iters_num)
        if iters_num >= 10 and iters_num <= 1000000:
            break
    except ValueError:
        pass
    print('Check your input!')
print('\n\n')

state0100 = '|0\t|1\t|0\t|0\t|'
state1100 = '|1\t|1\t|0\t|0\t|'
state1001 = '|1\t|0\t|0\t|1\t|'
state0101 = '|0\t|1\t|0\t|1\t|'
state1011 = '|1\t|0\t|1\t|1\t|'
state0111 = '|0\t|1\t|1\t|1\t|'
state1101 = '|1\t|1\t|0\t|1\t|'
state0011 = '|0\t|0\t|1\t|1\t|'
state1111 = '|1\t|1\t|1\t|1\t|'

state0100_counter = 0
state1100_counter = 0
state1001_counter = 0
state0101_counter = 0
state1011_counter = 0
state0111_counter = 0
state1101_counter = 0
state0011_counter = 0
state1111_counter = 0


processed_counter = 0
generated_counter = 0
req_in_queue_counter = 0
req_in_sys_counter = 0
totat_counter = 0
Kchannel1_counter = 0
Kchannel2_counter = 0

current_state = state0100
ev1 = False
ev2 = False
for i in range(iters_num):
    if current_state == state0100:

        req_in_sys_counter += 1
        req_in_queue_counter += 0
        Kchannel1_counter += 1
        Kchannel2_counter += 0
        generated_counter += 1

        state0100_counter += 1
        if event(pi1):
            current_state = state1001
        else:
            current_state = state1100


    elif current_state == state1100:

        req_in_sys_counter += 1
        req_in_queue_counter += 0
        Kchannel1_counter += 1
        Kchannel2_counter += 0
        generated_counter += 0

        state1100_counter += 1
        if event(pi1):
            current_state = state0101
        else:
            current_state = state0100


    elif current_state == state1001:

        req_in_sys_counter += 1
        req_in_queue_counter += 0
        Kchannel1_counter += 0
        Kchannel2_counter += 1
        generated_counter += 0

        state1001_counter += 1
        if event(pi2):
            current_state = state0100
            processed_counter += 1
        else:
            current_state = state0101


    elif current_state == state0101:

        req_in_sys_counter += 2
        req_in_queue_counter += 0
        Kchannel1_counter += 1
        Kchannel2_counter += 1
        generated_counter += 1

        state0101_counter += 1

        ev1 = event(pi1)
        ev2 = event(pi2)

        if not ev1 and not ev2:
            current_state = state1101
        elif ev1 and ev2:
            processed_counter += 1
            current_state = state1001
        elif ev1 and not ev2:
            current_state = state1011
        else:
            processed_counter += 1
            current_state = state1100


    elif current_state == state1011:

        req_in_sys_counter += 2
        req_in_queue_counter += 1
        Kchannel1_counter += 0
        Kchannel2_counter += 1
        generated_counter += 0

        state1011_counter += 1
        if event(pi2):
            processed_counter += 1
            current_state = state0101
        else:
            current_state = state0111
	    

    elif current_state == state0111:

        req_in_sys_counter += 3
        req_in_queue_counter += 1
        Kchannel1_counter += 1
        Kchannel2_counter += 1
        generated_counter += 1

        state0111_counter += 1

        ev1 = event(pi1)
        ev2 = event(pi2)

        if not ev1 and not ev2:
            current_state = state1111
        elif ev1 and ev2:
            processed_counter += 1
            current_state = state1011
        elif ev1 and not ev2:
            current_state = state1011
        else:
            processed_counter += 1
            current_state = state1101


    elif current_state == state1101:

        req_in_sys_counter += 2
        req_in_queue_counter += 0
        Kchannel1_counter += 1
        Kchannel2_counter += 1
        generated_counter += 0

        state1101_counter += 1

        ev1 = event(pi1)
        ev2 = event(pi2)

        if not ev1 and not ev2:
            current_state = state0101
        elif ev1 and ev2:
            processed_counter += 1
            current_state = state0101
        elif ev1 and not ev2:
            current_state = state0111
        else:
            processed_counter += 1
            current_state = state0100


    elif current_state == state1111:

        req_in_sys_counter += 3
        req_in_queue_counter += 1
        Kchannel1_counter += 1
        Kchannel2_counter += 1
        generated_counter += 0

        state1111_counter += 1

        ev1 = event(pi1)
        ev2 = event(pi2)

        if not ev1 and not ev2:
            current_state = state0111
        elif ev1 and ev2:
            processed_counter += 1
            current_state = state0111
        elif ev1 and not ev2:
            current_state = state0111
        else:
            processed_counter += 1
            current_state = state0101

totat_counter = state0100_counter + state1100_counter + state1001_counter + state0101_counter \
                + state1011_counter + state0111_counter + state1101_counter + state1111_counter

Q = processed_counter / generated_counter
Pdenied = 1 - Q
Lqueue = req_in_queue_counter / iters_num
Lsys = req_in_sys_counter / iters_num
A = processed_counter / iters_num
Wqueue = Lqueue / A
Wsys = Lsys / A
lambd = 0.5
Kchannel1 = Kchannel1_counter / totat_counter
Kchannel2 = Kchannel2_counter / totat_counter

print('\n\n')
print('Statistics:')

print(f'0100: {state0100_counter}\t|{state0100_counter / totat_counter}\t|')
print(f'1100: {state1100_counter}\t|{state1100_counter / totat_counter}\t|')
print(f'1001: {state1001_counter}\t|{state1001_counter / totat_counter}\t|')
print(f'0101: {state0101_counter}\t|{state0101_counter / totat_counter}\t|')
print(f'1011: {state1011_counter}\t|{state1011_counter / totat_counter}\t|')
print(f'0111: {state0111_counter}\t|{state0111_counter / totat_counter}\t|')
print(f'1101: {state1101_counter}\t|{state1101_counter / totat_counter}\t|')
print(f'1111: {state1111_counter}\t|{state1111_counter / totat_counter}\t|')


print('\n\n')
print(f'Processed counter: {processed_counter}')
print(f'Generated counter: {generated_counter}')
print(f'Requests in queue counter: {req_in_queue_counter}')
print(f'Requests in system counter: {req_in_sys_counter}')
print(f'Kchannel1 counter: {Kchannel1_counter}')
print(f'Kchannel1 counter: {Kchannel2_counter}')
print(f'A: {A}')
print(f'Kchannel1: {Kchannel1}')
print(f'Kchannel2: {Kchannel2}')
print(f'Q: {Q}')
print(f'Pdenied: {1 - Q}')
print(f'Lqueue: {Lqueue}')
print(f'Lsys: {Lsys}')
print(f'Wqueue: {Wqueue}')
print(f'Wsys: {Wsys}')
