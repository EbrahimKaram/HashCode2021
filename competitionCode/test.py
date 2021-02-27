import numpy as np

street = []
path = []
sim_time, n_intersec, n_streets, n_cars, score_by_car = 0, 0, 0, 0, 0


def getpathperlength(length):
    out = []
    for p in path:
        if int(p[0]) == length:
            out.append(p)
    return out


def readinput(file):
    file1 = open(file, 'r')
    lines = file1.readlines()
    count = 0

    global sim_time, n_intersec, n_streets, n_cars, score_by_car
    n_streets = 0
    for line in lines:
        count += 1
        if count == 1:
            sim_time, n_intersec, n_streets, n_cars, score_by_car = line.split()
            n_streets = int(n_streets)
            sim_time = int(sim_time)
            n_intersec = int(n_intersec)
            n_cars = int(n_cars)
            score_by_car = int(score_by_car)
            print("simulation time = ", sim_time)
            print("number of intersections:", n_intersec)
            print("n streets:", n_streets)
            print("n cars", n_cars)
            print("score_by_car", score_by_car)
        elif count <= 1 + n_streets:
            # inter1, inter2, stname, sttime
            street.append(line.split())
        else:
            # number of total streets in path , path street names in sequence
            path.append(line.split())
        # print("Line{}: {}".format(count, line.strip()))


# output
# 1st line number of int with schedule
def getlightperintersec(streets):
    streetlights = []
    for st in streets:
        streetlights.append(int(st[1]))
    unique, counts = np.unique(np.array(streetlights), return_counts=True)
    return dict(zip(unique, counts))


def getrouteforint():
    routesPerIntersection = {}
    for s in street:
        #print(s)
        # print(s[1])
        if s[1] in routesPerIntersection:
            routesPerIntersection[s[1]].append(s[2])
        else:
            routesPerIntersection[s[1]]=[s[2]]

    # print(routesPerIntersection)
    # return list(routesPerIntersection.values())[internumber]
    return routesPerIntersection


def roadstatistics():
    # stnames =[]
    stats = {}
    '''for st in street:
        stnames.append(st[2])'''
    for p in path:
        for r in p[1:]:
           if r in stats:
               stats[r] += 1
           else:
               stats[r] = 1
    return stats


if __name__ == '__main__':
    output = ''
    filelist = ['a.txt','b.txt','c.txt','d.txt','e.txt','f.txt']
    for f in filelist:
        print("Working on file:", f)
        readinput(f)
        # print("Streets:", street)
        # print("Car Paths:", path)
        lightsperintersec = getlightperintersec(street)
        # print('routes in 1', getrouteforint('1'))
        output += str(len(lightsperintersec)) + '\n'  # total number of intersections with lights
        routesPerIntersection = getrouteforint()
        stats = roadstatistics()
        print("Road statistics:", stats)
        for i, el in enumerate(lightsperintersec.values()):
            intersectionnumber = list(lightsperintersec.keys())[i]
            # print('intersectionnumber: ', intersectionnumber)
            output += str(intersectionnumber) + '\n'  # add intersection number

            if el == 1:  # check number of lights in the intersection if 1 always green
                output += '1\n'  # number of routes to turn greenlight for
                routeininter = routesPerIntersection[str(intersectionnumber)]  # get road names
                output += routeininter[0] + ' ' + str(sim_time) + '\n'  # first road name, all simulation time
            else:


                routeininter = routesPerIntersection[str(intersectionnumber)]  # get road names
                cycle = 0
                fractions = []
                total = 0
                for r in routeininter:
                    if r in stats:
                        fractions.append(stats[r])
                        cycle += stats[r]
                        total += 1
                    else:
                        fractions.append(0)
                gcd = np.gcd.reduce(fractions)
                if gcd !=0:
                    fractions = fractions/gcd
                    cycle = int(cycle/gcd)
                output += str(total)+'\n'  # number of routes to turn greenlight for
                for i, fr in enumerate(fractions):
                    output += routeininter[i] + ' ' + str(int(fr)) + '\n'
        # print('output=', output)
        outname = f.split(".")[0]
        text_file = open("output_" + outname + ".txt", "w")

        text_file.write(output)

        text_file.close()
    # first key list(lightsperintersec.keys())[0]
