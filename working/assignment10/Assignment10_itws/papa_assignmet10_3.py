import numpy as np

def main():
    height, reason = [],[]
    fortresses = "240\t The lenght of the seilbahn don't seem that long so the mountain can't be that tall\n" \
               "300\t Taking into consideration that Koblenz is at a 74 m altitude, as the fortress stands on small hill it can't be taller than estimated.\n" \
               "375 \t Compared to Deutsches Eck the hill seems tall enough for me to reach about this height."

    towers = "400 \t I just assume the tower is in a much higher hill than the fortress. Therefore i think is this much higher" \
             "450 \t Based on my initial guess about the fortress. I believe that the tower is a copule of hundred meters taller than this hill altitude." \
             "450 \t I think this tower is located on a hill that is considerably much taller than the fortress."

    fortress = fortresses.split("\n")
    tower = towers.split("\n")
    for f in fortress:
        guess = f.split("\t")
        height.append(int(guess[0]))

    mean = np.mean(height)
    sd = np.std(height)
    var = np.square(sd)
    print("The mean height fot the fortres is  of {} m".format(mean))
    print("The standard deviation for the fortress is of {} m".format(round(sd,2)))
    print("The Variation for the fortress is of {} m".format(round(var,2)))

    print()
    print()

    for t in tower:
        guess = t.split("\t")
        height.append(int(guess[0]))

    mean = np.mean(height)
    sd = np.std(height)
    var = np.square(sd)
    print("The mean height fot the tower is  of {} m".format(mean))
    print("The standard deviation for the tower is of {} m".format(round(sd, 2)))
    print("The Variation for the tower is of {} m".format(round(var, 2)))
if __name__ == "__main__":
        main()