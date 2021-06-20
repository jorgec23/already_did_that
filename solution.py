# Hey, I already did that!
# inputs are a nonnegative integer n, and a base
# steps
#       x = sorted digits in descending order
#       y = sorted digits in ascending order
#       z = x - y
#       n = z, repeat the process
#
#
# This process will give a list of numbers, the goal

def already_did_that(n, b):

    # create a dictionary that will track the appearance of digits with a list of indeces
    # for each digit created, check to see if a list exists
    # if a list does exist, append the index(there should be two now), then return their difference
    repeating = False
    index_counter = 0
    ind_dict = {n: [0]}

    # calculate the number of digits the original ID has, propagate to each new ID
    k = len(str(n))

    while not repeating:
        # calculate the new worker id
        z = new_id(n, k, b)

        # reset the worker id
        n = z

        # update the index of the current id, then check to see if it is in the index dictionary
        # if it is, then return the difference of the initial index for z, and the current one
        # else, just add an entry to the dictionary
        index_counter += 1
        if z in ind_dict:
            print(ind_dict)
            print('current z =', z)
            print('original z index =', ind_dict[z])
            return  index_counter - ind_dict[z][0]
            repeating = True
        else:
            ind_dict[z] = [index_counter]



def new_id(current_id, num_digits, base):
    # take in the current ID and the number of digits, "k"
    x_n = sorted(str(current_id), reverse = True)
    y_n = sorted(str(current_id))

    # add trailing zeros to the string version of 'x', 'y' is left alone since leading zeros
    # will not affect the value of the subtraction 'x - y'
    if len(x_n)<num_digits:
        x_n.append('0'*(num_digits - len(x_n)))

    # find the new worker id "z"
    x = int(''.join(x_n), base)
    y = int(''.join(y_n), base)
    return convert_to_base(x-y, base)

def convert_to_base(n, base):
    # we were told the highest base would be 10, so no need to worry about letters
    num_left = n
    n_str = ''
    if n < base:
        return n
    else:
        while num_left > 0:
            remainder = num_left%base
            num_left = num_left//base
            n_str = str(remainder)+n_str
    return int(n_str)
