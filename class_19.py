# Dictionary of students (id -> details)
students_data = {
    "id1": {"name": "Alice", "age": 20, "subject integration": "Science, Mathematics, English" },
    "id2": {"name": "Bob", "age": 22, "subject integration": "English , science, Mathematics" }, 
    "id3": {"name": "Alice", "age": 20, "subject integration": "Science, Mathematics, English" },#duplicate of id1
    "id4": {"name": "Charlie", "age": 21, "subject integration": "Mathematics, Science, English" }
}

results={}
seen_keys =[]

#using list instead of a set
for student_id, details in students_data.items():
    unique_key = (details["name"], details["age"], details["subject integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        results[student_id] = details

       # print output line by line
for k,v in results.items():
    print(k,":",v)