def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    mars_weight = weight * 0.38
    jupiter_weight = weight * 2.34
    print(
    """
On Mars you would weigh {0:.2f} pounds.
On Jupiter you would weigh {1:.2f} pounds.""".format(mars_weight, jupiter_weight))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
