
# Given weight on earth and string representing planet, return weight on planet
# If string does not match a planet, raise ValueError
def weight_on_planets(earth_weight, planet):
   # add code here - based on input planet string, return appropriate value
   # if planet is not matched, raise ValueError exception
      if planet == 'Mars' :
         return earth_weight * .38 
      elif planet == 'Jupiter' :
         return earth_weight * 2.34
      elif planet == 'Venus' :
         return earth_weight * .91
      else :
         raise ValueError

if __name__ == '__main__':
    pounds = float(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
          "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.\n" +
          "On Venus you would weigh", weight_on_planets(pounds, 'Venus' ), "pounds." )
