
def placeNumbers( sign , number ):
 minIndex, maxIndex = 0, len(number) - 1
 placed = []
 for i in range(len(sign)):
    if sign[i] == '<'
    placed.append(number[minIndex])
    minIndex += 1
    else:
        placed.append(number[maxIndex])
        maxIndex -= 1
    placed.append(number[maxIndex])
    return placed



if __name__ == '__main__':
    sign = input()
    number = []
    val = int(input())
    # Input 0 to break out of the loop
    while val:
        number.append(val)
        val = int(input())
    
    placed = placeNumbers( sign , number )
    for i in range(0, len(number)-1):
        if not(placed[i]):	
            valid = False
        if sign[i] == '<' and placed[i] >= placed[i+1]:
            valid = False
        if sign[i] == '>' and placed[i] <= placed[i+1]:
            valid = False
      
    valid = valid and placed[len(placed)-1] > 0;
    if valid:
      print("The placement is valid.")
    else:
      print("The placement is not valid.")
    
    for i in range(0, len(sign)):
       str1 = str(placed[i])+" "+sign[i]+" "
       print(str1, end = '')
   
    print(placed[len(placed)-1])
 

        