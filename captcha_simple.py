import random
def captcha():
  captcha = ""
  r1 = random.randint(0, 10)
  if r1 < 10:
    lenn = r1
  for i in range(0, lenn):  
    r2 = random.randint(0, 10)
    # r2 = 7
    if r2 < 6:
      r3 = random.randint(0, 10)
      # if r3 < 10:
      captcha += str(r3)
    else:
      r3 = random.randint(0, 25)
      captcha += chr(r3 + 97)
  return captcha
print(captcha())