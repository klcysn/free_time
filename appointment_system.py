class hospital() :
    
    def __init__(self) :
        self.__name = ""
        self.__address = ""
        self.__division = {"Divisions"}
        self.__doctor = []
        self.__appointment = []
        self.__patient = []

    def start(self) :
        answ = 0
        while answ not in range(1, 12) :
            try :
                answ = int(input(f"""
                Welcome {self.get_name()} Hospital

                [1] Change Hospital Name
                [2] Change Hospital Address
                [3] Add Division
                [4] Add Doctor
                [5] Add Appointment
                [6] Add Patient
                [7] List Divisions
                [8] List Doctors
                [9] List Appointments
                [10] List Patients
                [11] Quit
                """))

                if answ == 1 : 
                    return self.__set_name()
                elif answ == 2 : 
                    return self.__set_address()
                elif answ == 3 : 
                    return self.__set_division()
                elif answ == 4 : 
                    return self.__set_doctor()
                elif answ == 5 : 
                    return self.__set_appointment()
                elif answ == 6 : 
                    return self.__set_patient()
                elif answ == 7 :
                    return self.get_division()
                elif answ == 8 :
                    return self.get_doctor()
                elif answ == 9 :
                    return self.get_appointment()
                elif answ == 10 :
                    return self.get_patient()
                elif answ == 11 :
                    break
                else : raise ValueError("Invalid Value!")
            except ValueError :
                print("Invalid Value!")
    
    def get_name(self) :
        return self.__name
       
   
    def __set_name(self) :
        self.__name = input("Please enter hospital name : ").title().strip()
        print("Hospital name was changed")
        input("Please to continue press enter")
        
    
    def get_address(self) :
        return self.__address
    
    def __set_address(self) :
        self.__address = input("Please enter hospital address : ").title().strip()
        print("Hospital address was changed")
        input("Please to continue press enter")
        
   
    def get_division(self) :
        print("Divisions".center(60, "="))
        for i in self.__division :
            print("Division :", i)
            print("=" * 60)
        input("Please to continue press enter")
        
    
    def __set_division(self) :
        a = True
        while a :
            x = input("Would you like to add division (Y/N) : ").title().strip()
            if x == "Y" :
                self.__division.add(input("Please enter division : ").title().strip())
                print("Division was added")
            elif x == "N" :
                a = False
        input("Please to continue press enter")
        

    def get_doctor(self) :
        print("Doctors".center(60, "="))
        for i in self.__doctor :
            print("""
            Name      : {f_name}
            Last Name : {l_name}
            Tel       : {tel}
            Division  : {div}""".format(f_name = i.get_name(), l_name = i.get_l_name(), tel = i.get_tel(), div = i.get_div()))
            print("=" * 60)
        input("Please to continue press enter")
        

    def __set_doctor(self) :
        while True :
            x = input("Would you like to add doctor (Y/N) : ").title().strip()
            if x == "Y" :
                f_name = input("Please enter doctor name : ").title().strip()
                l_name = input("Please enter doctor last name : ").title().strip()
                tel = input("Please enter doctor telephone number : ")
                div = input("Please enter doctor division : ").title().strip()
                ful_name = f_name + "_" + l_name
                ful_name = doctor(f_name, l_name, tel, div)
                self.__doctor.append(ful_name)
                print("Doctor was added")
            elif x == "N" :
                input("Please to continue press enter")
                
        
    def __set_appointment(self) :
        sitiuation = True
        dctr = input("Please enter doctor full name : ").title().strip()
        ptnt = input("Please enter patient full name : ").title().strip()
        dt = input("Please enter appointment date (YYYY-MM-DD-HH:MM) : ")
        code = dctr + "||" + dt
        for i in self.__appointment :
            lst = i.split("||")
            if dctr == lst[0] and dt == lst[1] :
                print(f"Doctor is not suitable in {dt}")
                sitiuation = False
        if sitiuation :
            appoint = code + "||" + ptnt
            self.__appointment.append(appoint)
            print("Appointment was completed")
        input("Please to continue press enter")
        
    
    def get_appointment(self) :
        print("=" * 60)
        print("Appointments".center(60, "="))
        app_num = 0
        for i in self.__appointment :
            lst = i.split("||")
            patient = lst[2]
            doctor = lst[0]
            date = lst[1]
            print(f"{patient} has appointment on {date} with {doctor}")
            print("=" * 60)
            app_num += 1
        if app_num == 0 :
            print("There is no appointment")
        input("Please to continue press enter")
        
    
    def __set_patient(self) :
        name = input("Please enter name : ").title().strip()
        l_name = input("Please enter last name : ").title().strip()
        tel = input("Please enter telephone number : ")
        ful_name = name + "_" + l_name
        ful_name = patient(name, l_name, tel)
        self.__patient.append(ful_name)
        print("Patient was added!")
        input("Please to continue press enter")
        
    
    def get_patient(self) :
        print("Patients".center(60, "="))
        for i in self.__patient :
            print(f"""

            Name      : {i.get_name()}
            Last Name : {i.get_l_name()}
            Tel       : {i.get_tel()}
            """)
            print("=" * 60)
        input("Please to continue press enter")
        

class person() :
    def __init__(self, name, l_name, tel) :
        self.__name = name
        self.__l_name = l_name
        self.__tel = tel
        
    def get_name(self) :
        return self.__name
   
    def get_l_name(self) :
        return self.__l_name
   
    def get_tel(self) :
        return self.__tel
class doctor(person) :
    __doc_num = 0
   
    def __init__(self, name, l_name, tel, div) :
        super().__init__(name, l_name, tel)
        doctor.doc_num_raise()
        self.__div = div 
   
    def get_div(self) :
        return self.__div
   
    @classmethod
    def doc_num_raise(cls) :
        cls.__doc_num +=1
class patient(person) :
    pass
