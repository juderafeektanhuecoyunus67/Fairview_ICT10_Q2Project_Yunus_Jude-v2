from pyscript import document, display, HTML

# ==============================================================================
# 1. START OF HOMEPAGE.HTML (SEATWORK 1)
# ==============================================================================

# Official list of ICT club members, stored lowercase for case-insensitive matching - gemini helped with this part since i couldnt ffigure out why it returns false when i typed the name correctly
club_members = [
    "anthony araneta",
    "audrey lucman",
    "cruz espia",
    "basilio taguiga",
    "brian bocalig",
    "edu hernandez",
    "kevin xin iii",
    "marco zambales",
]

def verify_candidate(event):
    """
    Retrieves first and last name from the DOM, verifies membership against list,
    and displays result in the top banner using a dictionary mapping
    without using any conditional statements or loops.
    """
    # Step 1 -> Retrieve and combine the candidate's first and last names
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate_name = f"{first_name} {last_name}".strip()

    # Step 2 -> Testing the membership in club list (returns True or False)
    is_member = candidate_name.casefold() in club_members

    # Step 3 -> Map boolean outcome directly to required output strings
    status_messages = {
        True: f"✅ Success! Congratulations {candidate_name}! You are officially part of the ICT club.",
        False: f"❌ Sorry {candidate_name}, your name is not on the list."
    }

    # Step 4 -> Extract corresponding status message via boolean key lookup
    result_text = status_messages[is_member]

    # Step 5 -> Update the DOM banner element with the result text
    output_element = document.getElementById("output1")
    output_element.innerText = ""
    display(result_text, target="output1")

# END OF 1. HOMEPAGE.HTML


# ==============================================================================
# 2. START OF ELEMENTCHECKER.HTML (SKILLS TEST)
# ==============================================================================

# Dictionary that contains strict non-metal elements mapped into (Name, Atomic Number, Atomic Mass)
non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "At": ("Astatine", 85, 210),
    "Rn": ("Radon", 86, 222),
    "Ts": ("Tennessine", 117, 294),
    "Og": ("Oganesson", 118, 294)
}


def check_element(event):
    """
    Retrieves element symbol input, looks up non-metal details via .get()
    with a default fallback tuple, and renders formatted HTML output
    without using any conditional statements.
    """
    # Step 1 -> Retrieve user input and normalize capitalization
    symbol = document.getElementById("symbol_input").value.strip().capitalize()

    # Step 2 -> Retrieve tuple (Name, Number, Mass) using .get() with default fallback
    elem_name, elem_number, elem_mass = non_metals.get(symbol, ("Element not found", "-", "-"))

    # Step 3 -> Join detailed output lines using HTML line breaks (<br>)
    result_html = "<br>".join([
        f"Symbol: {symbol or '-'}",
        f"Element: <i>{elem_name}</i>",
        f"Atomic Number: {elem_number}",
        f"Atomic Mass: {elem_mass}"
    ])

    # Step 4 -> Render HTML output inside the green results box
    display(HTML(result_html), target="element-output", append=False)

# END OF 2. ELEMENTCHECKER.HTML


# ==============================================================================
# 3. START OF SCHOOLCLUBMEMBERS.HTML (DRILL 2)
# ==============================================================================

# Predefined sets of club members per grade level
grade_7 = {"Anthony Araneta", "Audrey Lucman"}
grade_8 = {"Cruz Espia", "Basilio Taguiga"}
grade_9 = {"Brian Bocalig", "Edu Hernandez"}
grade_10 = {"Marco Zambales", "Kevin Xin III"}


def add_club_member(event):
    """
    Retrieves first and last name inputs, combines them with the four
    grade-level sets using the set union (|) operator, sorts the master set,
    and renders each member separated by HTML <br> tags without if statements.
    """
    # Step 1 -> Retrieve and format the new member's full name
    first = document.getElementById("club_first_name").value.strip().title()
    last = document.getElementById("club_last_name").value.strip().title()
    full_name = f"{first} {last}".strip()

    # Step 2 -> Filter out empty string without using an if statement
    new_member_set = set(filter(None, [full_name]))

    # Step 3 -> Combine all 4 grade-level sets and the new member set via union (|)
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member_set

    # Step 4 -> Sort the master set alphabetically and join with HTML line breaks (<br>)
    sorted_members_html = "<br>".join(sorted(master_set))

    # Step 5 -> Display the formatted list inside the green box
    output_html = f"<b>ICT Club Members: ({len(master_set)} members):</b><br>{sorted_members_html}"
    display(HTML(output_html), target="club-output", append=False)

# END OF 3. SCHOOLCLUBMEMBERS.HTML


# ==============================================================================
# 4. START OF MEETTHECREATOR.HTML (PROJECT)
# ==============================================================================

# Dictionary about the meet the creator's personal info
creator_info = {
    "name": "Jude T. Yunus",
    "age": "15",
    "interests": "Arm Wrestling, Badminton,<br>Literature, Physics, much more...",
    "hobbies": "Running, Watching, Sleeping,<br>Eating A Lot, & Working Out.",
    "dreams": "To become more smarter,<br>stronger, & to become a future pilot.",
    "idiom": "<i>It is what it is</i>"
}


def load_creator_profile():
    """
    Populates the Meet the Creator page using dictionary values and HTML formatting
    automatically on page load without using any conditional statements.
    """
    # Step 1 -> Check that the creator-profile container exists on the active page
    target_box = document.getElementById("creator-profile")

    # Step 2 -> Build HTML profile layout from dictionary keys
    profile_html = "".join([
        f"<h2 class='creator-name'>{creator_info['name']}</h2>",
        f"<p class='creator-detail'><strong>Age:</strong> {creator_info['age']}</p>",
        f"<p class='creator-detail'><strong>Interests:</strong> {creator_info['interests']}</p>",
        f"<p class='creator-detail'><strong>Hobbies:</strong> {creator_info['hobbies']}</p>",
        f"<p class='creator-detail'><strong>Dreams:</strong> {creator_info['dreams']}</p>",
        f"<p class='creator-detail'><strong>Favorite idiom:</strong> {creator_info['idiom']}</p>"
    ])

    # Step 3 -> Rendering profile inside #creator-profile when present on the page
    target_box and display(HTML(profile_html), target="creator-profile", append=False)


# Automatically populate profile when meetthecreator.html loads
load_creator_profile()

# END OF 4. MEETTHECREATOR.HTML