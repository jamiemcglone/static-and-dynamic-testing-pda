### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # This if statement needs double equals ==
      return True
    else # This else is missing a colon :
      return False
   

  dif highest_card(self, card1 card2): # This function definition needs to begin with def, the parameters are also missing a comma , between card1 and card2
  if card1.value > card2.value: # Python functions need all the code within to be indented
    return card # This should be returning card1 or card2, card does not exist
  else:
    return card2
  


def cards_total(self, cards): # This function needs to be indented to be inside the class
  total # Total needs to be assigned to something beforehand, total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total # This return statement needs to be outside of the for loop, python will stop the function on the first iteration currently as it will hit the return statement. Total also needs to be changed to a str otherwise it will not be able to concatenate
  
```
