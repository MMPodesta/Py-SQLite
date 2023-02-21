from openpyxl import Workbook, load_workbook

book = load_workbook('Test - Form(1-2).xlsx')
sheet = book.active


# Details
company_name = sheet['F2'].value
owner = sheet['E2'].value

# Scope1
kilometers_driven_monthly = int(sheet['H2'].value) * int(sheet['I2'].value)
yearly_vehicle_emission = kilometers_driven_monthly * 115 * 12  # in gCO2

# Scope2
yearly_electricity_emission = int(sheet['J2'].value) * 389 * 12  # in gCO2

# Scope3
employee_drivers_amount = round(int(sheet['K2'].value) * int(sheet['L2'].value) / 100)
weekly_commute_distance = 100
yearly_commute_emission = employee_drivers_amount * weekly_commute_distance * 4 * 115 * 12  # in gC02

total = yearly_vehicle_emission + yearly_electricity_emission + yearly_commute_emission

# print out
print("********************************************************")
print("company: " + company_name)
print("Owner: " + owner)
print("Yearly vehicle emission:", yearly_vehicle_emission, "gC02")
print("Yearly electricity emission:", yearly_electricity_emission, "gC02")
print("Yearly commute emission:", yearly_commute_emission, "gC02")
print("Total emission per year:", total, "gC02")
print("********************************************************")

