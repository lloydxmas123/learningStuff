#quick script to calculate annual EC2 cost

def annualCost():
    ec2 = float(input("Hourly EC2 Cost: "))
    lic = float(input("Hourly License Cost: "))
    cost = (ec2 * 8760) + (lic * 8760)
    print("Your EC2 instance will cost ${} per year. ")
