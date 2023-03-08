from operator import indexOf
import sched


class Schedule:
    name: "a"
    st : 0
    ft : 0

    def __init__ (self,n,s,f):
        self.name = n
        self.st = s
        self.ft = f
    def Print(self):
        print(self.name + " " + str(self.st) + " " + str(self.ft))

schedule = []

schedule.append(Schedule("A",0,6))
schedule.append(Schedule("B",1,4))
schedule.append(Schedule("C",3,5))
schedule.append(Schedule("D",3,8))
schedule.append(Schedule("E",4,7))
schedule.append(Schedule("F",5,9))
schedule.append(Schedule("G",6,10))
schedule.append(Schedule("H",8,11))

# Sort by finish time
for i in range(0,len(schedule)):
    for j in range(0,len(schedule)):
        if (schedule[i].ft < schedule[j].ft):
            tmp = schedule[j]
            schedule[j] = schedule[i]
            schedule[i] = tmp

# sorted schedule
print("List of all Jobs")
for s in schedule:
    s.Print()

maxJob = []
allJobs = []

# check if job is compatible
def isCompatible(j, jnext):
    if (j.ft <= jnext.st):
        return True
    return False


for j in schedule:
    jobs = [j]
    jPos = schedule.index(j)
    while(jPos<len(schedule)):
        lastJob = jobs[len(jobs)-1]
        if (isCompatible(lastJob,schedule[jPos])):
           jobs.append(schedule[jPos])
        jPos += 1

    allJobs.append(jobs)

print()
print("List of all Jobs combination")
for js in allJobs:
    # if (len(js) > len(maxJob)):
    #     maxJob = js
    for j in js:
        j.Print()
    print()

# print("Maximum Jobs")
# for jobs in maxJob:
#     j.Print()

