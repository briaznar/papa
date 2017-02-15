import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot(ginis,restaurants):
    # The y values. Cumulative percentage of incomes
    j = 0
    for restaurant in restaurants:
        y, y_pe = [], []
        i = 0
        restaurant = sorted(restaurant)
        for rest in restaurant:
            prob = rest*100/sum(restaurant)
            if i == 0:
                y.append(prob)
            else:
                y.append(prob + y[i-1])
            i += 1

        # The perfect equality y values. Cumulative percentage of incomes.
        y_pe = np.linspace(0.0, 100.0, len(y))

        plt.title("Gini " + str(round(ginis[j],2)))
        plt.plot(y, label='lorenz', color='r')
        plt.plot(y_pe, label='perfect_equality', color='b')
        plt.ylabel('Percentage of guests')
        plt.xlabel('No. of tables')
        x_legend = mpatches.Patch(color='red', label='observations')
        y_legend = mpatches.Patch(color='blue', label='perfect equality')
        plt.legend(handles=[x_legend, y_legend], loc=5)
        plt.show()
        j += 1

def gini(restaurant):
    ordered = sorted(restaurant)
    height, area_under_curve = 0, 0
    for value in ordered:
        height += value
        area_under_curve += height - value / float(2)
    area_under_equity = height * len(restaurant) / float(2)
    gini = (area_under_equity - area_under_curve) / area_under_equity
    return gini


def generateChineseRestaurant(customers):
    # First customer always sits at the first table
    tables = [1]
    #for all other customers do
    for cust in range(2, customers+1):
            # rand between 0 and 1
            rand = random.random()
            # Total probability to sit at a table
            prob = 0
            # No table found yet
            table_found = False
            # Iterate over tables
            for table, guests in enumerate(tables):
                # calc probability for actual table an add it to total probability
                prob += guests / (cust)
                # If rand is smaller than the current total prob., customer will sit down at current table
                if rand < prob:
                    # incr. #customers for that table
                    tables[table] += 1
                    # customer has found table
                    table_found = True
                    # no more tables need to be iterated, break out for loop
                    break
            # If table iteration is over and no table was found, open new table
            if not table_found:
                tables.append(1)
    return tables
 
restaurants = 1000
network, ginis = [], []
for iterations in range(1, 6):
    network.append(generateChineseRestaurant(restaurants))
for net in network:
    ginis.append(gini(net))

plot(ginis,network)