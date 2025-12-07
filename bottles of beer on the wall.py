bottles = 3

while bottles > 0:
    current_bottles = bottles -1
    print (f"{bottles} bottles of beer on the wall, {bottles} bottles of beer")
    print (f"Take one down and pass it around, {current_bottles} + bottles of beer on the wall. \n")
    bottles -= 1
    
if bottles == 0:
    print ("0 bottle of beer on the wall, 0 bottles of beer.")
    print ("Need to get more beer bottles")