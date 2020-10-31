# My-Hacktoberfest

print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel after the examinations?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep smiling. Life is good!")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Find something fun to do")
      counter += 1
    if each_word == "tiring":
      feelings_list.append("tiring")
      encouragement_list.append("Get some sleep")
      counter += 1
    if each_word == "relieved":
      feelings_list.append("relieved")
      encouragement_list.append("Relax after the stressful examinations")
      counter += 1

    if each_word == "dead tired":
      feelings_list.append("dead tired")
      encouragement_list.append("Just find something fun to do")
      counter += 1
     if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("look on the brighter side or talk to your friends")
      counter += 1  
    
    
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("talk to your friends.Maybe you will feel better")
      counter += 1
     if each_word == "excited":
      feelings_list.append("excited")
      encouragement_list.append("Good for you!I bet you will be able to do well!")
      counter += 1  
    
    
    
    if counter == 0:

      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember to "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
