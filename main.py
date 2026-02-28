from pyscript import document

# Function that checks if student is eligible
def check_eligibility(event):

    registration = document.getElementById("registration").value
    medical = document.getElementById("medical").value
    grade = document.getElementById("grade").value
    result = document.getElementById("result")

    # Make sure all fields are selected
    if registration == "" or medical == "" or grade == "":
        result.innerHTML = "Please complete all fields."
        return

    grade = int(grade)

    # Check eligibility conditions
    if registration == "yes" and medical == "yes" and 7 <= grade <= 10:

        # Assign team based on grade
        if grade == 7:
            team = "Blue Bears 🐻"
            image = "blueb.png"
        elif grade == 8:
            team = "Red Bulldogs 🐶"
            image = "redb.png"
        elif grade == 9:
            team = "Yellow Tigers 🐯"
            image = "yellowt.png"
        else:
            team = "Green Hornets 🐝"
            image = "greenh.png"

        result.innerHTML = f"""
        🎉 Yay! Congratulations! You are eligible for Intramurals. <br>
        Your team is: <b>{team}</b><br><br>

        <img src="{image}" width="150">
        """

    else:
        if registration != "yes":
            result.innerHTML = "You must register online first."
        elif medical != "yes":
            result.innerHTML = "You must secure a medical clearance."
        else:
            result.innerHTML = "Only Grades 7-10 are allowed to join."