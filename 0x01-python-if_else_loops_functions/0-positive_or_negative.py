<<<<<<< HEAD
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
=======
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format((number)))
elif number == 0:
    print("{} is zero".format((number)))
else:
    print("{} is negative".format((number)))
>>>>>>> 2dd6f4d388043d390bc8f6c6381da430f2a00fb9
