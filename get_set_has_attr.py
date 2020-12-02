class employee:
    emp_name = "irfa"
    age = 30
    emp_id = "abcd"

    def default_age(self):
        print("this is default age 30")


emp1 = employee()

print(getattr(emp1, "age", 45))
print(setattr(emp1, "emp_name", "pasha"))
print(hasattr(emp1, "age"))

