drones='''The idea of remotely controlled unmanned vehicles flying
through the air either raises concerns over personal privacy, or leads
us to consider citizens who live in fear of drones used for military
purposes. NASA have successfully tested a prototype system that allows
unpiloted drones to detect and avoid other aircraft in their midst. The
agency’s drones are able to sense when something was in their flight
path and make adjustments on their own. In the UK, the Civil Aviation
Authority is warning that drones being flown as high up as 2,000ft are
putting passenger aircraft in danger. Drones can be used to monitor
pollution'''.lower()

print(drones)

print()

amount=len(drones)
print(amount)
print()
vowel_a=drones.count("a")
vowel_e=drones.count("e")
vowel_i=drones.count("i")
vowel_o=drones.count("o")
vowel_u=drones.count("u")
print('vowels')
print()
print('a',vowel_a)
print('e',vowel_e)
print('i',vowel_i)
print('o',vowel_o)
print('u',vowel_u)

added = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u

percentage=added/amount*100

precentage_main = round(percentage,2)

print("calculate percentage of vowels",precentage_main,'%')
