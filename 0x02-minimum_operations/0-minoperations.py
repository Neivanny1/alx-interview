#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            '''
            print('-(11)->{}'.format('H' * done), end='')
            '''
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            '''
            print('-(11)->{}'.format('H' * done), end='')
            '''
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            '''
            print('-(01)->{}'.format('H' * done), end='')
            '''
            done += clipboard
            ops_count += 1
    return ops_count