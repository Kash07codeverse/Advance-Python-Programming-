# Hospital Patient Management System
# A simple OOP project for managing patient records

class Patient:
    """Base class for all patients"""
    
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
    
    def display_info(self):
        """Display patient information"""
        print(f"ID: {self.patient_id} | Name: {self.name} | Cost: ₹{self.treatment_cost}")


class GeneralPatient(Patient):
    """General ward patients"""
    
    def __init__(self, patient_id, name, treatment_cost):
        super().__init__(patient_id, name, treatment_cost)
        self.category = "General Ward"
    
    def display_info(self):
        print(f"[GENERAL] ID: {self.patient_id} | Name: {self.name} | Cost: ₹{self.treatment_cost}")


class SpecialPatient(Patient):
    """Special/ICU patients with additional priority"""
    
    def __init__(self, patient_id, name, treatment_cost):
        super().__init__(patient_id, name, treatment_cost)
        self.category = "Special/ICU"
    
    def display_info(self):
        print(f"[SPECIAL] ID: {self.patient_id} | Name: {self.name} | Cost: ₹{self.treatment_cost}")


class Hospital:
    """Hospital class to manage all patients"""
    
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = []  # List to store all patients
    
    def add_patient(self, patient):
        """Add a new patient to the hospital"""
        self.patients.append(patient)
        print(f"✓ Patient {patient.name} added successfully!\n")
    
    def display_all_patients(self):
        """Display all patient records"""
        if len(self.patients) == 0:
            print("No patients in the system.\n")
            return
        
        print("=" * 60)
        print(f"  {self.hospital_name} - Patient Records")
        print("=" * 60)
        
        for patient in self.patients:
            patient.display_info()
        
        print("=" * 60)
        print(f"Total Patients: {len(self.patients)}\n")
    
    def calculate_total_cost(self):
        """Calculate total treatment cost for all patients"""
        total = sum(patient.treatment_cost for patient in self.patients)
        return total
    
    def search_patient(self, patient_id):
        """Search for a patient by ID"""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print(f"\nPatient Found!")
                patient.display_info()
                return patient
        
        print(f"\nPatient with ID {patient_id} not found.\n")
        return None


# ============ MAIN PROGRAM ============

if __name__ == "__main__":
    # Create a hospital
    hospital = Hospital("City Medical Hospital")
    
    # Add some general patients
    p1 = GeneralPatient(101, "Rajesh Kumar", 5000)
    p2 = GeneralPatient(102, "Priya Singh", 4500)
    
    # Add some special patients
    p3 = SpecialPatient(201, "Amit Patel", 15000)
    p4 = SpecialPatient(202, "Neha Gupta", 18000)
    
    # Add patients to hospital
    hospital.add_patient(p1)
    hospital.add_patient(p2)
    hospital.add_patient(p3)
    hospital.add_patient(p4)
    
    # Display all records
    hospital.display_all_patients()
    
    # Show total cost
    total_cost = hospital.calculate_total_cost()
    print(f"Total Treatment Cost: ₹{total_cost}\n")
    
    # Search for a specific patient
    print("Searching for Patient ID 201...")
    hospital.search_patient(201)
    
    print("\nSearching for Patient ID 999...")
    hospital.search_patient(999)