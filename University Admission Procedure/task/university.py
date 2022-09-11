N = int(input())  # the maximum number of students for each department

#           === Empty lists of departments ===
departments = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}


#           ===Getting a list with nested applicants lists and conversion some elements to int===
def get_applicants_list():
    applicants_list = []
    for line in applicants.readlines():
        applicants_list.append(line.split())
    return applicants_list


#           ===Choosing of applicants, three rounds===
def choosing(step):
    for department in departments:
        applicants_lst = sorted_lists(department)
        for applicant in applicants_lst:
            if applicant[step] == department:
                if len(departments[department]) == N:
                    break
                departments[department].append(applicant)
                sorted_list.remove(applicant)


#       ===The function returns the sorted lists===
def sorted_lists(dep):
    if dep == "Biotech":
        return sorted(sorted_list, key=lambda x: (-max((int(x[2]) + int(x[3])) / 2, float(x[6])), x[0], x[1]))
    elif dep == "Chemistry":
        return sorted(sorted_list, key=lambda x: (-max(int(x[3]), int(x[6])), x[0], x[1]))
    elif dep == "Engineering":
        return sorted(sorted_list, key=lambda x: (-max(((int(x[4]) + int(x[5])) / 2), float(x[6])), x[0], x[1]))
    elif dep == "Mathematics":
        return sorted(sorted_list, key=lambda x: (-max(int(x[4]), int(x[6])), x[0], x[1]))
    elif dep == "Physics":
        return sorted(sorted_list, key=lambda x: (-max(((int(x[2]) + int(x[4])) / 2), float(x[6])), x[0], x[1]))


#       ===Creating text files and recording data by department in them===
def create_txt():
    for i in departments:
        if i == "Biotech":
            student = sorted(departments[i], key=lambda x: (-max((int(x[2]) + int(x[3])) / 2, float(x[6])), x[0], x[1]))
            with open(f"{i.lower()}.txt", "w") as file:
                for s in student:
                    file.writelines(f"{s[0]} {s[1]} {max(((int(s[2]) + int(s[3])) / 2), float(s[6]))}\n")
        elif i == "Chemistry":
            student = sorted(departments[i], key=lambda x: (-max(int(x[3]), int(x[6])), x[0], x[1]))
            with open(f"{i.lower()}.txt", "w") as file:
                for s in student:
                    file.writelines(f"{s[0]} {s[1]} {max(int(s[3]), int(s[6]))}\n")
        elif i == "Engineering":
            student = sorted(departments[i], key=lambda x: (-max(((int(x[4]) + int(x[5])) / 2), float(x[6])), x[0], x[1]))
            with open(f"{i.lower()}.txt", "w") as file:
                for s in student:
                    file.writelines(f"{s[0]} {s[1]} {max(((int(s[4]) + int(s[5])) / 2), float(s[6]))}\n")
        elif i == "Mathematics":
            student = sorted(departments[i], key=lambda x: (-max(int(x[4]), int(x[6])), x[0], x[1]))
            with open(f"{i.lower()}.txt", "w") as file:
                for s in student:
                    file.writelines(f"{s[0]} {s[1]} {max(int(s[4]), int(s[6]))}\n")
        elif i == "Physics":
            student = sorted(departments[i], key=lambda x: (-max(((int(x[2]) + int(x[4])) / 2), float(x[6])), x[0], x[1]))
            with open(f"{i.lower()}.txt", "w") as file:
                for s in student:
                    file.writelines(f"{s[0]} {s[1]} {max(((int(s[2]) + int(s[4])) / 2), float(s[6]))}\n")


#       ===Getting a sorted list of applicants
with open("applicants.txt") as applicants:
    sorted_list = sorted(get_applicants_list())

for k in range(7, 10):
    choosing(k)

create_txt()
