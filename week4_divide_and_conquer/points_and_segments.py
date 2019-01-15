# Uses python3
import sys
from itertools import chain
#chain() iterator terminating on the shortest input sequence: chain('ABC','DEF'--->A B C D E F)
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #pass iterables
    start_points = zip(starts, ['l'] * len(starts), range(len(starts)))
    end_points = zip(ends, ['r'] * len(ends), range(len(ends)))
    this_points = zip(points, ['t'] * len(points), range(len(points)))

    full_list = chain(start_points, end_points, this_points)
    sort_list = sorted(full_list, key=lambda a: (a[0], a[1]))
    segment = 0
    i = 0
    
    for num, letter, index in sort_list:
        if letter == 'l':
            segment += 1
        elif letter == 'r':
            segment -= 1
        else:
            cnt[index] = segment
            i += 1
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
