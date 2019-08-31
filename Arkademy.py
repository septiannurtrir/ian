import json

biodata = {
    "name": "Septian Nur Tri Rachmadi",
    "age": 25,
    "address": "Sagan GK V/904, RT/RW, 039/08, Terban, Gondokusuman, Yogyakarta",
    "hobbies": ("Reading a book", "Exercise", "Travelling"),
    "is_married": False,
    "list_school": 
    [
        {"name": "Universitas Airlangga", "year_in": 2015, "year_out": 2017, "major": "English Literature, Linguistic"},
        {"name": "Universitas Gadjah Mada", "year_in": 2012, "year_out": 2015, "major": "English Language"},
        {"name": "SMA Berbudi Yogyakarta", "year_in": 2009, "year_out": 2012, "major": "Social"}
    ],
    "Skills": 
    [
        {"skill_name": "Python", "level": "beginner"},
        {"skill_name": "English Translation", "level": "expert"},
        {"skill_name": "English Transcription", "level": "expert"},
        {"skill_name": "English Proofreading", "level": "advanced"},
        {"skill_name": "Content Writing", "level": "advanced"},
        {"skill_name": "Microsoft Office", "level": "expert"}
    ],
    "interest_in_coding": True,
}

profile = json.dumps(biodata)

print(profile)