# Default Arguments
# example 1
def empinfo(designation, name="ABC"):
    print("Name : ", name)
    print("Designation : ", designation)
    return

empinfo(designation="Dev")

# example 2
def empinfo(designation, name="XYZ"):
    print("Name : ", name)
    print("Designation : ", designation)
    return

empinfo(designation="Dev", name="ABC")
empinfo(designation="Dev")
