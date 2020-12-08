f = [value.split(",") for value in
     (open("day7", "r").read().split(".\n"))]
 
f.pop() #Pop trailing white space from list

bagrules = {}
    
def bagfinder(bag): 
    foundbag = False 
    for subbag in bagrules[bag]: 
        if subbag.strip() == 'other': 
            pass
        elif subbag.rstrip() == 'shiny gold': 
            foundbag = True
            return foundbag
        else: 
            foundbag = bagfinder(subbag)
            if foundbag == True: 
                return foundbag

totalbags = 0
def bagcalc(bag, bagcount):
    #print(bagcount)
    for subbag in bagrules[bag]: 
        numofsubbags = bagcount
        if subbag.strip() == 'other': 
            pass
        else: 
            global totalbags
            while numofsubbags > 0: 
                totalbags += (bagrules[bag][subbag])
                bagcalc(subbag, bagrules[bag][subbag])
                numofsubbags -= 1     
    
def part1(): 
    counter = 0 
    for i in bagrules.keys(): 
        result = bagfinder(i)
        if result == True: 
            counter += 1
    print(f'Shiny Gold bag can be found in {counter} different bags')

def part2(): 
    bagcalc('shiny gold', 1)
    print(f'You can have a total of {totalbags} bags within your bag')


# Structure dictionary based on bag rules
for i in f: 
    bagname = " ".join((i[0].split(" "))[0:2])
    bagdetails = (i[0].split("contain")[1:] + i[1:])
    bagdetailsdict = {}
    for j in bagdetails: 
        subbagname = (j[3:-4].rstrip())
        if j[1] != "n":
            numbbags = int(j[1])
        else: 
            numbbags = 0   
        bagdetailsdict.update({subbagname: (numbbags)})
    bagrules.update({bagname: bagdetailsdict})


part1()
part2()