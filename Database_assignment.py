import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Students (
    Student_ID TEXT PRIMARY KEY,
    Department TEXT,
    Level INTEGER,
    Attendance_Percentage REAL,
    Avg_Exam_Score REAL
)
""")

cur.executemany(
    "INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?, ?)",
    [
        ("CSC001", "Computer Science", 300, 92, 74.5),
        ("CSC002", "Computer Science", 300, 85, 68.0),
        ("CSC003", "Computer Science", 200, 78, 61.5),
        ("CSC004", "Computer Science", 400, 95, 81.0),
        ("CSC005", "Computer Science", 100, 70, 55.0),
    ],
)
conn.commit()

for row in cur.execute("SELECT * FROM Students"):
    print(row)

conn.close()