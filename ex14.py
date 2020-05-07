from sys import argv

script, user_name=argv
prompt='>'

print("Hi {}, I'm the {} script.".format(script,user_name))
print("I'd like to ask a few questions")
print(f"Do you like me {user_name}?")
likes=input(prompt)

print("Where do you live {}".format(user_name))
lives=input(prompt)

print(f"What kind of computer do you have {user_name}")
computer=input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

#Notar que el argumento 0 siempre es el nombre del script