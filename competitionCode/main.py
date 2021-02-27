import numpy as np
street = []
path = []


def readinput(file):
    file1 = open(file, 'r')
    lines = file1.readlines()
    count = 0
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


def getrouteforint(street):
    routesPerIntersection = {}
    for s in street:
        if s[1] in routesPerIntersection:
            routesPerIntersection[s[1]].append(s[2])
        else:
            routesPerIntersection[s[1]]=[s[2]]

    # print(routesPerIntersection)
    # print(routesPerIntersection['0'])
    return routesPerIntersection

def roadstatistics(path):
    stats = {}
    for p in path:
        for r in p[1:]:
           if r in stats:
               stats[r] += 1
           else:
               stats[r] = 1
    return stats


if __name__ == '__main__':
    readinput('Inputs\d.txt')
    print("Streets:", street)
    print("Car Paths:", path)
    # getlightperintersec(street)
    print(roadstatistics(path))
    # getrouteforint(street)
