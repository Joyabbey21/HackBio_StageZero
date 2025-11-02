#HackBio Internship - Stage 0 Python Task
#Team: Glycine

# Task: Write a simple Python script for printing the names, slack username, country, 1 hobby, affiliations of people on your team and the DNA sequence of the genes they love most.
# Author: Joy Abiodun
# Prints each team member's profile with their favorite gene's DNA sequence

team = [
    {
        "Name": "Vishnushiri",
        "Slack": "vishnu shiri",
        "Country": "India",
        "Hobby": "Reading",
        "Affiliations": "Bioinformatician",
        "DNA_Gene": "SOD1"
    },
    {
        "Name": "Joy",
        "Slack": "Abiodun Joy",
        "Country": "Nigeria",
        "Hobby": "Exploring",
        "Affiliations": "Statistician, ML Researcher",
        "DNA_Gene": "-"
    },
    {
        "Name": "Victor",
        "Slack": "ONAH",
        "Country": "Nigeria",
        "Hobby": "Footballing",
        "Affiliations": "Bioinformatician",
        "DNA_Gene": "-"
    },
    {
        "Name": "Aakash",
        "Slack": "Aakash Deva Thirukonda",
        "Country": "Sweden",
        "Hobby": "Cooking",
        "Affiliations": "-",
        "DNA_Gene": "TP53"
    },
    {
        "Name": "Mary",
        "Slack": "Alo Yetunde Mary",
        "Country": "Nigeria",
        "Hobby": "Reading",
        "Affiliations": "Bioinformatician",
        "DNA_Gene": "DNMT3A"
    },
    {
        "Name": "Opemidimeji",
        "Slack": "Opemidimeji Osatoyinbo",
        "Country": "Nigeria",
        "Hobby": "Exploring; DIYs",
        "Affiliations": "Researcher: Microbiologist; Molecular Biologist",
        "DNA_Gene": "-"
    },
    {
        "Name": "Amin",
        "Slack": "Amin",
        "Country": "Malaysia",
        "Hobby": "Reading",
        "Affiliations": "Molecular Biologist",
        "DNA_Gene": "TERT"
    },
    {
        "Name": "Oluwaseun",
        "Slack": "Oluwaseun Awosise",
        "Country": "Nigeria",
        "Hobby": "Watching Sitcoms",
        "Affiliations": "-",
        "DNA_Gene": "-"
    },
    {
        "Name": "Ishita",
        "Slack": "Ishita Chopra",
        "Country": "India",
        "Hobby": "Reading, Hiking",
        "Affiliations": "Bioinformatician",
        "DNA_Gene": "BCL2"
    },
    {
        "Name": "Opeoluwa",
        "Slack": "Eadencre8ives",
        "Country": "Nigeria",
        "Hobby": "Troubleshooting & Movies",
        "Affiliations": "Microbiology, Bioinformatics, Molecular Biology",
        "DNA_Gene": "BRCA1"
    },
    {
        "Name": "Olorunfemi",
        "Slack": "Femi",
        "Country": "Nigeria",
        "Hobby": "Watching Movies",
        "Affiliations": "Cell Biology and Genetics, Bioinformatics",
        "DNA_Gene": "Sonic Hedgehog"
    }
]

# Print details neatly
for member in team:
    print(f"Name: {member['Name']}")
    print(f"Slack Username: {member['Slack']}")
    print(f"Country: {member['Country']}")
    print(f"Hobby: {member['Hobby']}")
    print(f"Affiliations: {member['Affiliations']}")
    print(f"Favorite Gene: {member['DNA_Gene']}")
    print("-" * 60)