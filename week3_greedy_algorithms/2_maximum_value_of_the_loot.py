# python3

def get_optimal_value(capacity, weights, values):
    value = 0.

    valuePerWeight = valuePerWeight = sorted([[v / w, w] for v,w in zip(values,weights)], reverse=True)
    print('valuePerWeight is',valuePerWeight,type(valuePerWeight))
    while capacity > 0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight): #find and select the largest value/weight
            print('i is:',i)
            print('item[1],item[0] are: ',item[1],item[0])
            if item [1] > 0 and maxi < item [0]:
                print('-------item [1] > 0 and maxi < item [0]')
                print('item[1],item[0] are: ',item[1],item[0])
                maxi = item [0]
                print('maxi is:',maxi)
                idx = i
        #case that capacity=0
        if idx is None:
            print('idx is None')
            return 0.
        #decide how much to selct and update the value and capacity
        v = valuePerWeight[idx][0]#value/weight
        w = valuePerWeight[idx][1]#weight
        print('v and w are:',v,w)
        if w <= capacity:
            print('w <= capacity')
            value += v*w
            capacity -= w
            print('capacity is:',capacity)
        else:
            if w > 0:
                print('w>0')
                value += capacity * v
                return value
        valuePerWeight.pop(idx)

    return value

if __name__ == "__main__":
    n = 3
    capacity = 50 #bag weight maximum
    values = [60, 100, 120]
    weights = [20, 50, 30]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value)) # print 180.0000000000