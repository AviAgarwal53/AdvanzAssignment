class ComplaintTracker:
    #Class to store all the ComplaintTracker Info
    
    def __init__(self, customer_name,service_number,complaint_desc,complaint_date,unique_complaint_id):
        self.customer_name = customer_name
        self.service_number = service_number
        self.complaint_desc = complaint_desc
        self.unique_complaint_id = unique_complaint_id 
        self.complaint_date = complaint_date
        self.next_ComplaintTracker = None

class Complaint:
    def __init__(self):
        self.head = None
        self.unique_complaint_id = 0
        self.count = 0 

    #Function to add complaits in the List
    def addComplaintTracker(self, customer_name,service_number,complaint_desc,complaint_date):
        self.unique_complaint_id +=1
        self.count +=1
        print(f"Complaint ID assigned to the ComplaintTracker name - {customer_name} is {self.unique_complaint_id}")
        new_ComplaintTracker = ComplaintTracker(customer_name,service_number,complaint_desc,complaint_date,self.unique_complaint_id)
        if self.head is None:
            self.head = new_ComplaintTracker
            return
        last_ComplaintTracker = self.head
        while last_ComplaintTracker.next_ComplaintTracker:
            last_ComplaintTracker = last_ComplaintTracker.next_ComplaintTracker
        last_ComplaintTracker.next_ComplaintTracker = new_ComplaintTracker
        if self.count >5:
            print("Alert: Complaints are reaching more than the value of 5. Please look into the matter")

    # function is to delete the ComplaintTracker using Unique id 
    def closeComplaint(self, unique_complaint_id):
        current_ComplaintTracker = self.head
        

        if current_ComplaintTracker and current_ComplaintTracker.unique_complaint_id == unique_complaint_id:
            self.head = current_ComplaintTracker.next_ComplaintTracker
            self.count-=1
            current_ComplaintTracker = None
            return

        prev_ComplaintTracker = None
        while current_ComplaintTracker and current_ComplaintTracker.unique_complaint_id != unique_complaint_id:
            prev_ComplaintTracker = current_ComplaintTracker
            current_ComplaintTracker = current_ComplaintTracker.next_ComplaintTracker

        if current_ComplaintTracker is None:
            return
        self.count-=1
        prev_ComplaintTracker.next_ComplaintTracker = current_ComplaintTracker.next_ComplaintTracker
        current_ComplaintTracker = None

    # function is to Display all the Complaints
    def displayAll(self):
        current_ComplaintTracker = self.head
        while current_ComplaintTracker:
            print(current_ComplaintTracker.unique_complaint_id,current_ComplaintTracker.customer_name,current_ComplaintTracker.service_number,current_ComplaintTracker.complaint_desc,current_ComplaintTracker.complaint_date)
            current_ComplaintTracker = current_ComplaintTracker.next_ComplaintTracker


    # function is to Display the Complaints using unique complaint id
        
    def display(self,unique_complaint_id):
        current_ComplaintTracker = self.head
        while current_ComplaintTracker:
            if(current_ComplaintTracker.unique_complaint_id == unique_complaint_id):
                print(current_ComplaintTracker.unique_complaint_id,current_ComplaintTracker.customer_name,current_ComplaintTracker.service_number,current_ComplaintTracker.complaint_desc,current_ComplaintTracker.complaint_date)

            current_ComplaintTracker = current_ComplaintTracker.next_ComplaintTracker
    

# Example usage:
complainttracker = Complaint()

print('''Enter the function you want to perform: 
Choose between add complaint(AC),
DisplayAll(DA),
Display using complaint id(DCI),
close a complaint(CC),
(use 'stop' keyword to stop the program)''')
while True:
    function = input()
    if function.lower() == "stop":
        break
    if function.lower() == "ac":
        customer_name = input("Enter the Customer name : ")
        service_number = int(input("Enter the Service Number: "))
        complaint_desc = input("Enter the Complaint description : ")
        complaint_date = input("Enter the Complaint Date : ")
        complainttracker.addComplaintTracker(customer_name,service_number,complaint_desc,complaint_date)

    elif function.lower() == "da":
        complainttracker.displayAll()

    elif function.lower() == "dci":
        complaint_id = int(input("Enter the Complaint id : "))
        complainttracker.display(complaint_id)
    elif function.lower() == "cc":
        complaint_id = int(input("Enter the Complaint id : "))
        complainttracker.closeComplaint(complaint_id)


