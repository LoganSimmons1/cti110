# CTI-110
# P4HW1 - Score List
# Logan Simmons
# 4/19/2023

# asking score count
# printing new line
# assigning mylist
# infinite while loop
# check if user score count is length of the list mylist
# break statement 
# print score number
# score input
# checking if score in range
# printing message
# printing message
# else condition
# append to mylist
# increment
# sort list
# get lowest score
# remove lowest score from list
# calculate the average
# checking score_avg
# assign grade
# check score_avg inside range
# assign grade
# check score_avg inside range
# assign grade
# else condition
# assign grade
## print results
# print lowest score
# print modified list
# print score_avg
# print grade
# print line

count=int(input("How many scores do you want to enter? "))
print("\n")
i,mylist=1,[]
while(True):
    if(len(mylist)==count):
        break
    print("Enter score #"+str(i)+": ",end="")
    score=int(input())
    if(score<0 or score>100):
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
    else:
        mylist.append(float(score))
        i+=1
mylist.sort()
lowest_score = mylist[0]
mylist.remove(lowest_score)
score_avg=sum(mylist)/len(mylist)
if(score_avg>90):
    grade="A"
elif(score_avg>=80 and score_avg<90):
    grade="B"
elif(score_avg>=70 and score_avg<80):
    grade="C"
else:
    grade="F"

print("\n\n-----------------Results------------")
print("Lowest Score       :",lowest_score)
print("Modified List      :",mylist)
print("Scores Average     :",score_avg)
print("Grade              :",grade)
print("\n\n---------------------------------------")
