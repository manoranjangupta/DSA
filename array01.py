#find out largest element in array

givenArray=[2,14,6,8,10]
maxNumber=2
for num in range(len(givenArray)):
    if  maxNumber<givenArray[num]:
     maxNumber=givenArray[num]
    print("MAX Number is : ",maxNumber)