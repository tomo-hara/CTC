""" The Body Mass Index (BMI) calculated by dividing the weight (kg) 
of a person by the square value of his or her height (meters). 
A BMI of 25 or higher, is considered to be a sign of obesity.

Given 2 natural numbers showing the height and weight of a person, 
write a program that outputs the person's BMI on the first line, 
and the message Obesity if the BMI is greater than or equal to 25. """

sli = []
for i in range(15):
  sli.append("")

for i in range(5):
  t = input().strip()
  for j in range(len(t)):
    sli[j] = sli[j] + t[j]


for i in range(len(sli)):
  print(sli[i],end="")