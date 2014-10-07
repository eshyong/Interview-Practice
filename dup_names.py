def parse_names():
    global namedict
    count = int(raw_input())
    i = 0
    while i < count:
        line = raw_input()
        array = line.split(':')
        ssn = array[1]
        ssn.strip()
        name = array[0]
        # check what format name is in, eg '<FIRST> <LAST>', '<LAST>, <FIRST>', etc
        first, last = '', None
        middle = None
        if ',' in name:
            # <LAST>, <FIRST> (<MIDDLE>)
            namearr = name.split(',')
            last = namearr[0]
            # Check if there's a middle name
            compound = namearr[1]
            compound = compound.lstrip()
            compound = compound.rstrip()
            if ' ' in compound:
                compound = compound.split(' ')
                if len(compound) > 1:
                    first = compound[0]
                    middle = compound[1]
            else:
                first = compound
        else:
            # <FIRST> (<MIDDLE> <LAST>)
            namearr = name.split(' ')
            first = namearr[0]
            if len(namearr) == 2:
                last = namearr[1]
            elif len(namearr) == 3:
                middle = namearr[1]
                last = namearr[2]
                
        namekey = first
        if namekey in namedict:
            del namedict[namekey]
        if middle != None:
            namekey += ' ' + middle
            if namekey in namedict:
                del namedict[namekey]
        if last != None:
            namekey += ' ' + last
            if namekey in namedict:
                del namedict[namekey]
            temp = first + ' ' + last
            if temp in namedict:
                del namedict[temp]
        namedict[namekey] = ssn
        i += 1

    print '\nList:'
    for key, value in namedict.iteritems():
        print key + ':' + value

namedict = {}
parse_names()
