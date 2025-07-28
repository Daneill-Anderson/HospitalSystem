                     #Programming Techniques | Daneill Anderson

                                #Outline for program : 
#This is an Hospital Management System (HMS) which will be coded to 
# handle appointments, patients, and doctors in medical facility. 
# It creates and stores data with unique IDs using object-oriented programming; 
# appointments have 4-digit IDs, while patients and doctors have 7-digit IDs.
# Viewing patient information, scheduling appointments, adding patients and doctors,
# and monitoring doctor schedules are all made possible via the system menu.


#---------------- First I need to import Modules I am going to need
from datetime import datetime
import random
import re




#The Person class will serve as a base for both Patient and Doctor.
# It holds shared information like name, date of birth, and contact. 
# Patient and Doctor classes inherit from Person, adding unique IDs and specific properties,
# like a doctor's specialty or a patient's appointment list.

# Here I will start the parent class, Parent class called Person
class Person:
    def __init__(self, christian_name, surname, date_of_birth, gender, address, phone):
        self.christian_name = christian_name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone = phone

# I will then create Patient class
class Patient(Person):
    def __init__(self, christian_name, surname, date_of_birth, gender, address, phone, patient_id):
        super().__init__(christian_name, surname, date_of_birth, gender, address, phone)
        self.patient_id = patient_id

#  Doctor class
class Doctor(Person):
    def __init__(self, christian_name, surname, date_of_birth, gender, address, phone, doctor_id, specialty):
        super().__init__(christian_name, surname, date_of_birth, gender, address, phone)
        self.doctor_id = doctor_id
        self.specialty = specialty

#  Appointment class
class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

# Bill class
 # fixed consultation fee
class Bill:
    def __init__(self, appointment):
        self.appointment = appointment
        self.consultation_fee = 3000.00 
        self.additional_service_fees = 0.0

    def calculate_total_bill(self):
        return self.consultation_fee + self.additional_service_fees


#  Hospital Management System Class

#This class will be use to manage the functions of the program 

#The HospitalSystem class acts as the system’s control, maintaining dictionaries 
# to store all patients, doctors, and appointments. It will allow me to do fast lookup and 
# modification by  IDs. It also tracks appointment IDs with a counter,
# ensuring each appointment is uniquely identified


class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        self.patient_id_counter = 1000001   # 7-digit starting ID
        self.doctor_id_counter = 2000001   # 7-digit starting ID
        self.appointment_id_counter = 3001  # 4-digit starting ID
        
    #Method to add patient
    def add_patient(self):
        try:
            print("\n--- Add Patient ---")
            first_name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            gender = input("Enter gender (M/F): ")
            address = input("Enter address: ")
            phone = input("Enter phone number (876-000-0000): ")
            patient = Patient(first_name, last_name, dob, gender, address, phone, self.patient_id_counter)
            self.patients[self.patient_id_counter] = patient
            print("************************************")
            print(f"\n Successful - Patient added with ID: {self.patient_id_counter}")
            self.patient_id_counter += 1
            
        except Exception as e:
            print(f"Error adding patient: {e}")
   
   
   #Method to add_doctor
    def add_doctor(self):
        try:
            print("\n--- Add Doctor ---")
            first_name = input("Enter doctor's first name: ")
            last_name = input("Enter doctor's last name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            gender = input("Enter gender (M/F): ")
            
            
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            specialty = input("Enter specialty: ")
            doctor = Doctor(first_name, last_name, dob, gender, address, phone, self.doctor_id_counter, specialty)
            self.doctors[self.doctor_id_counter] = doctor
            print("************************************")
            print(f"\n successful - Doctor added with ID: {self.doctor_id_counter}")
            self.doctor_id_counter += 1
            
        except Exception as e:
            print(f"Error adding doctor: {e}")
            
            
   #Method to book_appointment

    def book_appointment(self):
        try:
            print("\n--- Book Appointment ---")
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            if patient_id in self.patients and doctor_id in self.doctors:
                date = input("Enter appointment date (YYYY-MM-DD): ")
                time_input = input("Enter appointment time (HH:MM): ")
                try:
                    time_obj = datetime.strptime(time_input, "%H:%M")
                    formatted_time = time_obj.strftime("%I:%M %p")
                except ValueError:
                    print("Invalid time format. Please use HH:MM (e.g., 14:30)")
                    return
                appointment = Appointment(self.appointment_id_counter, self.patients[patient_id], self.doctors[doctor_id], date, formatted_time)
                self.appointments[self.appointment_id_counter] = appointment
                print(f"Appointment booked with ID: {self.appointment_id_counter}")
                self.appointment_id_counter += 1
            else:
                print("Invalid patient or doctor ID.")
        except Exception as e:
            print(f"Error booking appointment: {e}")

# This method I will use to print out the bill 
    def print_bill(self):
        try:
            appointment_id = int(input("Enter appointment ID for billing: "))
            appointment = self.appointments.get(appointment_id)
            if appointment:
                bill = Bill(appointment)
                additional_service_fees = float(input("Enter additional service fees (test/medication/accommodation): JMD $"))
                bill.additional_service_fees = additional_service_fees
               
               
                print("\n*******************BEVERLEY MEMORIAL MEDICAL CENTRE*******************")
                print("  15 Mayberry Drive, Kingston, Jamaica ")
                print("  BeverlymemorialH@gmail.com ")
                print("  Tel: (876) 786- 3456 ")
                print(" =======================================================================")
                print(f" Patient:     {appointment.patient.christian_name} {appointment.patient.surname}")
                print(f" Doctor: Dr. {appointment.doctor.christian_name} {appointment.doctor.surname} ({appointment.doctor.specialty})")
                print(f" Date:       {appointment.date}")
                print(f" Time:         {appointment.time}")
                print(f" Consultation Fee: JMD ${bill.consultation_fee}")
                print(f" Additional Service Fees: JMD ${bill.additional_service_fees}")
                print(f" Total Bill: JMD ${bill.calculate_total_bill()}")
                print("========================================\n")
            else:
                print("Invalid appointment ID.")
                
        except Exception as e:
            print(f"Error generating bill: {e}")

    def cancel_appointment(self):
        try:
            print("\n--- Cancel Appointment ---")
            appointment_id = int(input("Enter appointment ID to cancel: "))
            if appointment_id in self.appointments:
                del self.appointments[appointment_id]
                print(f"Appointment ID {appointment_id} has been cancelled.")
            else:
                print("Invalid appointment ID.")
        except Exception as e:
            print(f"Error cancelling appointment: {e}")

    def view_patient(self):
        try:
            print("\n--- View Patient ---")
            patient_id = int(input("Enter patient ID to view: "))
            patient = self.patients.get(patient_id)
            if patient:
                print(f"\nPatient ID: {patient.patient_id}")
                print(f"Name: {patient.christian_name} {patient.surname}")
                print(f"DOB: {patient.date_of_birth}")
                print(f"Gender: {patient.gender}")
                print(f"Address: {patient.address}")
                print(f"Phone: {patient.phone}\n")
            else:
                print("Patient not found.")
        except Exception as e:
            print(f"Error viewing patient: {e}")

    def view_schedule(self):
        try:
            print("\n--- View Doctor Schedule ---")
            doctor_id = int(input("Enter doctor ID to view schedule: "))
            if doctor_id not in self.doctors:
                print("Invalid doctor ID.")
                return

            has_appointments = False
            for appt_id, appointment in self.appointments.items():
                if appointment.doctor.doctor_id == doctor_id:
                    has_appointments = True
                    print(f"\nAppointment ID: {appt_id}")
                    print(f"Patient: {appointment.patient.christian_name} {appointment.patient.surname}")
                    print(f"Date: {appointment.date}")
                    print(f"Time: {appointment.time}")

            if not has_appointments:
                print("No appointments found for this doctor.")
        except Exception as e:
            print(f"Error viewing schedule: {e}")

    def run(self):
        while True:
            print("************************************************************")
            print("\n=== Beverly's Memorial Hospital Management System ===")
            print("1. Add Patient")
            print("2. Add Doctor")
            print("3. Book Appointment")
            print("4. Cancel Appointment")
            print("5. View Patient")
            print("6. View Schedule")
            print("7. Print Bill")
            print("8. Exit")
            print("************************************************************")
            
            choice = input("Select an option: ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.add_doctor()
            elif choice == "3":
                self.book_appointment()
            elif choice == "4":
                self.cancel_appointment()
            elif choice == "5":
                self.view_patient()
            elif choice == "6":
                self.view_schedule()
            elif choice == "7":
                self.print_bill()
            elif choice == "8":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

#---------------- This is the line of code that will be used to run program
# this is very important to have to run 
if __name__ == "__main__":
    system = HospitalSystem()
    system.run()
