# if the finish time array already sorted .
def selectMaxActivities(s, f):
    n = len(f)
    print("The selected activities are:\n")
    i = 0
    print(s[i], end=" ")
    for j in range(1, n):
        if s[j] >= f[i]:
            print(s[j], end=" ")
            i = j


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
selectMaxActivities(s, f)


# If the finish array is not sorted.
def printMaxActivities(Activity):
    selected = []
    n = len(Activity)
    # sort the array acc to finish time
    Activity.sort(key=lambda x: x[1])
    # after sorted we have to take the first activity always
    i = 0
    selected.append(Activity[i])
    # for the remaining activity follow the below approach
    for j in range(1, n):
        # select the activity if it's start time is greater than or equal to finish time of previously selected item.
        if Activity[j][0] >= Activity[i][1]:
            selected.append(Activity[j])
            i = j
    # return the selected list
    return selected


Activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
selected = printMaxActivities(Activity)
print("\nThe maximum selected activities are:")
for i in selected:
    print(i, end=" ")



