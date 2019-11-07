
import chores
from math import gcd


COOLDOWN_STR = 'cooldown'
NO_CHORE_STR = ''


# if u > 1, not schedulable
def utilization():
    u = 0 
    for chore_name, deadline in chores.CHORE_D.items():
        u += 1 / deadline
    return u    

# returns smallest # of days before schedule will repeat itself
def shortest_repeating_cycle():
    a = list(chores.CHORE_D.values())
    
    lcm = a[0]
    for i in a[1:]:
      lcm = lcm * int(i/gcd(lcm, i))
    return lcm


def build_scheduled_chores_l(num_days):
    # returns the name of the chore with the shortest deadline, 
    # retruns false if all chores are in cooldown
    def find_min_deadline_chore_if_exists(i_chore_d):
        min_deadline_chore_name = False
        min_deadline = False
        
        for chore_name, deadline in i_chore_d.items():
            if deadline != COOLDOWN_STR:
                if min_deadline_chore_name == False or deadline < min_deadline:
                    min_deadline_chore_name = chore_name
                    min_deadline = deadline
        return min_deadline_chore_name 
    
    
    
    i_chore_d = dict(chores.CHORE_D)
    cooldown_chore_d = {}
    chore_l = []
    
    

    # for each day, pick next chore to schedule, by shortest deadline,
    # if non exist that are not in cool-down, do not schedule any chore for that day
    for day_num in range(num_days):
        
        # check if any chores are done cooling down, if so, set thier deadline back to normal
        # and removes the chore name from the cooldown dict
#         print('                                                                         about to enter loop') # d    ````````````````````````````````````````````
        cooldown_pop_l = []
        for chore_name, deadline in cooldown_chore_d.items():
#             print(                            deadline)#``````````````````````````````````````````````````````````````````````````````
            if deadline <= 0:
#                 print('                                                     deadline of ', chore_name , ' == 0, setting to ', chores.CHORE_D[chore_name] )#`````````````````````````````
                i_chore_d[chore_name] = chores.CHORE_D[chore_name]
                cooldown_pop_l.append(chore_name)
#                 cooldown_chore_d.pop(chore_name)
        for chore_name in cooldown_pop_l:
            cooldown_chore_d.pop(chore_name)
#         print('                                                                          out of loop')#````````````````````````````````````````````````
            
        
        shortest_deadline_chore_name = find_min_deadline_chore_if_exists(i_chore_d)
        print('day: ', day_num, '  shortest_deadline_chore_name: ', shortest_deadline_chore_name )#````````````````````````````````
        print(shortest_deadline_chore_name)
        

        if shortest_deadline_chore_name == False:
            chore_l.append(NO_CHORE_STR)
        else:
            chore_l.append(shortest_deadline_chore_name)
            i_chore_d[shortest_deadline_chore_name] = COOLDOWN_STR
            cooldown_chore_d[shortest_deadline_chore_name] = chores.CHORE_D[shortest_deadline_chore_name]
            
        # decrement counts by 1
        for chore_name, deadline in i_chore_d.items():
            if deadline != COOLDOWN_STR:
                i_chore_d[chore_name] = (deadline - 1)
        
        print('cooldown_chore_d', cooldown_chore_d)#`1```````````````````````````````````````````````````````
        print('i_chore_d', i_chore_d)#`1```````````````````````````````````````````````````````
        
        for chore_name, deadline in cooldown_chore_d.items():
                cooldown_chore_d[chore_name] = (deadline - 1)
                
    return chore_l








# print (shortest_repeating_cycle())
# 
# print(utilization())
# 
# num_days_until_repeat = shortest_repeating_cycle()
# 
# scheduled_chores_l = build_scheduled_chores_l(num_days_until_repeat)
# print(scheduled_chores_l)


def main():
    
    u = utilization()
    if u > 1:
        print('Utilization > 1, cannot schedule:  ', u)
    else:
        c = input(str('Utilization = ' + str(u) + ' \nContinue? (y / n):  '))
        if c == 'n':
            exit()
        else:
            print('here')










main()







# FREQ_INDEX       = 0
# DEIVIATION_INDEX = 1
# 
# 
# def build_chore_l(chore_d):
#     # makes tuple of chores ordered from most to least frequent
#     def build_chore_freq_t(chore_d):
#         
#         # make dict of just chores with thier freqs
#         pure_chore_freq_d = {}
#         for chore_name, freq_t in chore_d.items():
#             pure_chore_freq_d[chore_name] = freq_t[FREQ_INDEX]
#             
# #         print(sorted(pure_chore_freq_d.items(), key=lambda item: item[1]))
#         print(sorted(chore_d.items(), key=lambda item: item[1][0]))
#             
#         
#     build_chore_freq_t(chore_d)
#         
#         
# #         chore_freq_t = ("EMPTY") * len(chore_d)
# #          
# #         for chore_name, freq_t in chore_d.items():
# #             print()
#         
# build_chore_l(chores.CHORE_D)
#         
#         
# # for i in sorted(chores.CHORE_D):
# #     print(i)






