import glob
from pathlib import Path

D = 'Duration of the simulation'
I = 'number of intersections'
S = 'number of Streets'
V = 'number of Cars'
F = "the bonus points for each car"
B = "Intersection at start"
E = "Intersection at end"
L = "Time to Travel Street"
P = "the number of streets"
street_name = "Name of Street"


def readinput(inputPath, input_file):
    street_count = 0
    car_count = 0
    file = open(inputPath, 'r')
    for (i, line) in enumerate(file):
        line = line.strip()  # remove new lines at the end for cleaner dictionary
        if (line == '\n'):
            break
        if(i == 0):
            split_lines = line.split(' ')
            input_file[D] = int(split_lines[0])
            input_file[I] = int(split_lines[1])
            input_file[S] = int(split_lines[2])
            input_file[V] = int(split_lines[3])
            input_file[F] = int(split_lines[4])

        elif (1 <= i <= input_file[S]):
            street_info = list(line.split(' '))
            input_file['Streets'][street_info[2]] = {
                B: street_info[0], E: street_info[1], L: int(street_info[3])}
            street_count += 1

        elif (i > input_file[S]):
            input_file['Cars'][car_count] = {P: int(line.split(' ')[0]),
                                             'Streets Needed': line.split(' ')[1:]}
            car_count += 1

    return input_file


def streetsAtIntersection(input_file):
    routesPerIntersection = {}
    for s in input_file["Streets"]:
        intersection_ID = input_parameters['Streets'][s][B]
        street_name = s
        if intersection_ID in routesPerIntersection:
            routesPerIntersection[intersection_ID]['name'].append(street_name)
        else:
            routesPerIntersection[intersection_ID] = {}
            routesPerIntersection[intersection_ID]['name'] = [street_name]

    return routesPerIntersection
# example return
# {'0': {'name': ['rue-de-londres']},
#  '1': {'name': ['rue-d-amsterdam', 'rue-d-athenes']},
#  '3': {'name': ['rue-de-rome']},
#  '2': {'name': ['rue-de-moscou']}}
# TODO add weights based on usage of street


def outPutFile(routesPerIntersection, outPutFile):
    # Create direcotry
    Path(outPutFile).parent.mkdir(parents=True, exist_ok=True)
    with open(outPutFile, 'w') as file:
        file.write(str(len(routesPerIntersection))+'\n')
        for s in routesPerIntersection:
            streets = routesPerIntersection[s]['name']
            numberOfStreets = len(streets)
            file.write(str(s)+'\n')
            file.write(str(numberOfStreets)+'\n')
            for street in streets:
                # Will find a way to addd weights to the dictionary
                file.write(street + " " + str(1)+'\n')


def getTimeToComplete(input_parameters):
    for key, car in input_parameters['Cars'].items():
        car_path = car['Streets Needed']
        sum=0
        for path in car_path:
            sum=sum +input_parameters['Streets'][path][L]
        print(sum)
        input_parameters['Cars'][key]['Time Needed']= sum
    return input_parameters

# TODO: add wieghts and remove unenccessary intersectrions to print


if __name__ == '__main__':
    input_files = glob.glob("Inputs/*.txt")
    # for file in input_files:
    file = input_files[0]
    input_parameters = {D: 0, I: 0, S: 0,
                        V: 0, F: 0, 'Streets': {}, 'Cars': {}}
    input_parameters = readinput(file, input_parameters)
    routesAtIntersection = streetsAtIntersection(input_parameters)
    # file_name = Path(file).name
    # outPutFile(routesAtIntersection, 'Outputs/output_'+file_name)
