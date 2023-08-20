import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred) 
db=firestore.client()

def link(tech_needed,id,deadline,work):
    employee_data = {}
    #emp_id,expertise,work_status,workload,experience,avail
    #emp1
    data=db.collection("WORKERS").document("1").get()
    dataset=data.to_dict()

    list=["ID","TECH","STATUS","EFFICIENCY","COUNT","avail"]
    emp1=[]
    for i in list:
        emp1.append(dataset[i])
    print(emp1)
    #emp2
    data=db.collection("WORKERS").document("2").get()
    dataset=data.to_dict()

    list=["ID","TECH","STATUS","EFFICIENCY","COUNT","avail"]
    emp2=[]
    for i in list:
        emp2.append(dataset[i])
    print(emp2)
    #emp3
    data=db.collection("WORKERS").document("3").get()
    dataset=data.to_dict()

    list=["ID","TECH","STATUS","EFFICIENCY","COUNT","avail"]
    emp3=[]
    for i in list:
        emp3.append(dataset[i])
    print(emp3)
    #emp4
    data=db.collection("WORKERS").document("4").get()
    dataset=data.to_dict()

    list=["ID","TECH","STATUS","EFFICIENCY","COUNT","avail"]
    emp4=[]
    for i in list:
        emp4.append(dataset[i])
    print(emp4)

    employee_data["emp1"] = emp1
    employee_data["emp2"] = emp2
    employee_data["emp3"] = emp3
    employee_data["emp4"] = emp4
    task_emp={}
    task1=[]
    task2=[]
    task3=[]
    task4=[]

    task_emp["task1"]=task1
    task_emp["task2"]=task2
    task_emp["task3"]=task3
    task_emp["task4"]=task4

    task_emp_f={}
    task1_f=[]
    task2_f=[]
    task3_f=[]
    task4_f=[]

    task_emp_f["task1"]=task1_f
    task_emp_f["task2"]=task2_f
    task_emp_f["task3"]=task3_f
    task_emp_f["task4"]=task4_f

    tech_employee_map_f={tech: [] for tech in tech_needed}
    tech_employee_map = {tech: [] for tech in tech_needed}


    def check_availability():
        
        for tech in tech_needed:
            for emp in [emp1, emp2, emp3, emp4]:
                if tech.lower() in emp[1].lower():
                    tech_employee_map[tech].append(emp[0])
                    # print(f"Technology '{tech}' found in employee {emp[0]}")


                
        # print(tech_employee_map)


        for i in range(0,len(tech_needed)):
            # print(f"----------------------stack no {i}----------------------")
            # print(tech_employee_map[tech_needed[i]])
            # print(f"no.of people knowing the tech {i} is {len(tech_employee_map[tech_needed[i]])}")
            if len(tech_employee_map[tech_needed[i]])!=0:
                for j in range(0,len(tech_employee_map[tech_needed[i]])):
                    people=tech_employee_map[tech_needed[i]][j]
                    varname="emp"+people
                    # print(f"{varname} is  availability for {i}th task is {employee_data[varname][2]}")
                    if employee_data[varname][2]==True:
                        task_emp["task"+str(i+1)].append(employee_data[varname][0])
                        
        return(task_emp)    
    # print("---------------------------------------------------------")
    for i in range(0,len(tech_needed)):
        check_availability()
        max=0
        max_emp=''
        for j in range(0,len(task_emp["task"+str(i+1)])):
            # print(type(task_emp["task"+str(i+1)][j]))
            var="emp" + task_emp["task"+str(i+1)][j]
            # print(employee_data[var])
            
            if (int(employee_data[var][3])>=int(max)):
                max=employee_data[var][3]
                max_emp=employee_data[var][0]
                # print(f"max is {max}")
                # print(f"max_emp is {max_emp}")
                employee_data[var][2]=False
                # print(employee_data[var])
                
        # print(f"the best employee for {i}th task is {max_emp}")
            

        tech_employee_map_f[tech_needed[i]].append(max_emp)


    data=tech_employee_map_f

    for value_list in data.values():
        for value in value_list:
            db.collection("WORKERS").document(value).update({"STATUS":False,"TASKID":work,"DEADLINE":deadline,"Task":id})
    return "done"
