ERROR = 1

def get_width_of_next(order, strips, cut):
    s_or = sorted(order)
    for i in xrange(len(s_or)):
        if s_or[i] > cut:
            #print order, s_or[i]
            return len(s_or[i:])

def calculate_area(strips, cut):
    area = 0
    #print strips, cut
    for key, value in strips.iteritems():
        area += max(0, key - cut)*value
        #print "hehe",  max(0, strip - cut)
    return area

def find(bottom, top, strips, target):
    cut = (top + bottom) / 2
    area_with_this_cut = calculate_area(strips, cut)
    #print area_with_this_cut / target, cut
    #print cut
    #print cut, area_with_this_cut
    #print "???", top, bottom, cut
    if top - bottom <= ERROR:
        if area_with_this_cut > target:
            return cut, area_with_this_cut
        else:
            return cut-1, calculate_area(strips, cut-1)
    elif area_with_this_cut >= target:
        return find(cut, top, strips, target)
    elif area_with_this_cut < target:
        return find(bottom, cut, strips, target)

def main():
    while True:
        strips = {}
        n, a = map(int, raw_input().split())
        order = []
        top = 0
        first_area = 0
        if n == 0 and a == 0:
            break
        for x in raw_input().split():
            try:
                strips[int(x)] += 1
            except Exception:
                strips[int(x)] = 1
            order.append(int(x))
            if int(x) > top:
                top = int(x)
            first_area += int(x)
        bottom = 0
        if first_area == a:
            print ":D"
        elif first_area < a:
            print "-.-"
        else:
            result, result_area = find(bottom, top, strips, a)
            if result_area == a:
                print "%.4f" % (result)
            else:
                width = get_width_of_next(order, strips, result)
                #print width, result_area, a
                print "%.4f" % (result + (result_area-a)/float(width))

main()