
noOfActivities = int(input("Enter number of activities: "))
activity = []
start = []
end = []
sol = [0]*noOfActivities

for i in range (noOfActivities):
    activity.append(i+1)
    st = int(input("Enter start time: "))
    et = int(input("Enter end time: "))
    start.append(st)
    end.append(et)

print(activity, start, end)
for i in range(noOfActivities):
    for j in range(noOfActivities-1-i):
        if(end[j]>end[j+1]):
            end[j], end[j+1] = end[j+1], end[j]
            start[j], start[j+1] = start[j+1], start[j]
            activity[j], activity[j+1] = activity[j+1], activity[j]

selectedActivity = activity[0]
selectedPos = 0
sol[activity[0]-1] = 1
print(selectedActivity,end=" ")

for i in range(noOfActivities):
    if(start[i]>=end[selectedPos]):
        selectedActivity = activity[i]
        selectedPos = i
        sol[activity[selectedPos]-1] = 1
        print(selectedActivity,end=" ")

print()
print("Solution vector {}".format(sol))


