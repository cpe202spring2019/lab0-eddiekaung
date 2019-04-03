def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh {0:.2f} pounds.".format(weight * 0.38) + \
    "\nOn Jupiter you would weigh {0:.2f} pounds.".format(weight * 2.34))
   
   
if __name__ == '__main__':
   weight_on_planets()
