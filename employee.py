class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return 0  # Default implementation, overridden in subclasses

    def __str__(self):
        return self.name


#salary contract worker 
class SalaryContractEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    #overriding get_pay method to calculate pay based on monthly salary
    def get_pay(self):
        return self.monthly_salary

    #overriding str method to make a custom message when printing worker
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."



#hourly contract worker
class HourlyContractEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_wage * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."



#salary contract worker with added bonus
class SalaryContractWithBonus(Employee):
    def __init__(self, name, monthly_salary, bonus):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def get_pay(self):
        return self.monthly_salary + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."



#hourly contract worker with added bonus
class HourlyContractWithBonus(Employee):
    def __init__(self, name, hourly_wage, hours_worked, bonus):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus

    def get_pay(self):
        return (self.hourly_wage * self.hours_worked) + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."



#salary contract worker with commissions per contract
class SalaryContractWithContractCommission(Employee):
    def __init__(self, name, monthly_salary, num_contracts, commission_per_contract):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return self.monthly_salary + (self.num_contracts * self.commission_per_contract)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."



#hourly contract worker with added commission per contract
class HourlyContractWithContractCommission(Employee):
    def __init__(self, name, hourly_wage, hours_worked, num_contracts, commission_per_contract):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return (self.hourly_wage * self.hours_worked) + (self.num_contracts * self.commission_per_contract)

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."





# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = SalaryContractEmployee('Billie', 4000)
print(billie)

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = HourlyContractEmployee('Charlie', 25, 100)
print(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = SalaryContractWithContractCommission('Renee', 3000, 4, 200)
print(renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = HourlyContractWithContractCommission('Jan', 25, 150, 3, 220)
print(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = SalaryContractWithBonus('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = HourlyContractWithBonus('Ariel', 30, 120, 600)
