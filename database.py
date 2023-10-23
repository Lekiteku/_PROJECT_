import sqlite3

class DatabaseManager:
    DATABASE_FILE = 'test.db'  # Default database filename

    @classmethod
    def set_database_file(cls, new_filename):
        cls.DATABASE_FILE = new_filename

    @staticmethod
    def create_database():
        conn = sqlite3.connect(DatabaseManager.DATABASE_FILE)
        cursor = conn.cursor()
        # Create the "STUDENTS INFORMATION" table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS "STUDENTS INFORMATION" (
        "STUDENT ID" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        "FIRST NAME" TEXT NOT NULL,
        "LAST NAME" TEXT NOT NULL,
        "CHECKPOINT ID" INTEGER,
        "GUARDIAN ID" INTEGER,
        FOREIGN KEY ("CHECKPOINT ID") REFERENCES CHECKPOINT("CHECKPOINT ID"),
        FOREIGN KEY ("GUARDIAN ID") REFERENCES "GUARDIAN INFORMATION"("GUARDIAN ID")
        )''')

        # Create the "GUARDIAN INFORMATION" table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS "GUARDIAN INFORMATION" (
        "GUARDIAN ID" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        "FIRST NAME" TEXT NOT NULL,
        "LAST NAME" TEXT NOT NULL,
        "PHONE NUMBER" INTEGER,
        "ADMISSION NUMBER" INTEGER
        )''')

        # Create the "CHECKPOINT" table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS CHECKPOINT (
        "CHECKPOINT ID" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        "LONGITUDE" REAL NOT NULL,
        "LATITUDE" REAL NOT NULL,
        "LOCATION NAME" TEXT
        )''')
        # ... (add  other tables)

        conn.commit()
        conn.close()

    def insert_student(first_name, last_name, checkpoint_id, guardian_id):
        conn = sqlite3.connect(DatabaseManager.DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO "STUDENTS INFORMATION" ("FIRST NAME", "LAST NAME", "CHECKPOINT ID", "GUARDIAN ID")
                          VALUES (?, ?, ?, ?)''', (first_name, last_name, checkpoint_id, guardian_id))
        conn.commit()
        conn.close()

    @staticmethod
    def insert_guardian(first_name, last_name, phone_number, admission_number):
        conn = sqlite3.connect(DatabaseManager.DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO "GUARDIAN INFORMATION" ("FIRST NAME", "LAST NAME", "PHONE NUMBER", "ADMISSION NUMBER")
                          VALUES (?, ?, ?, ?)''', (first_name, last_name, phone_number, admission_number))
        conn.commit()
        conn.close()

    @staticmethod
    def insert_checkpoint(longitude, latitude, location_name):
        conn = sqlite3.connect(DatabaseManager.DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO CHECKPOINT ("LONGITUDE", "LATITUDE", "LOCATION NAME")
                          VALUES (?, ?, ?)''', (longitude, latitude, location_name))
        conn.commit()
        conn.close()

    @classmethod
    def execute_query(cls, query, params=()):
        try:
            conn = sqlite3.connect(cls.DATABASE_FILE)
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()

    @classmethod
    def remove_entry(cls, table_name, entry_id):
        query = f'DELETE FROM "{table_name}" WHERE "{table_name} ID" = ?'
        cls.execute_query(query, (entry_id,))

    @classmethod
    def get_last_checkpoint_id(cls):
        try:
            conn = sqlite3.connect(cls.DATABASE_FILE)
            cursor = conn.cursor()

            # Query for the most recent checkpoint
            cursor.execute('''
                SELECT "CHECKPOINT ID" 
                FROM CHECKPOINT
                ORDER BY "CHECKPOINT ID" DESC
                LIMIT 1
                ''')
            last_checkpoint = cursor.fetchone()
            return last_checkpoint[0] if last_checkpoint else None
        except sqlite3.Error as e:
            print(f"Error getting last checkpoint ID: {e}")
        finally:
            conn.close()

    @classmethod
    def get_last_guardian_id(cls):
        try:
            conn = sqlite3.connect(cls.DATABASE_FILE)
            cursor = conn.cursor()

            # Query for the maximum guardian ID
            cursor.execute('SELECT MAX("GUARDIAN ID") FROM "GUARDIAN INFORMATION"')
            last_guardian_id = cursor.fetchone()[0]
            return last_guardian_id if last_guardian_id is not None else None
        except sqlite3.Error as e:
            print(f"Error getting last guardian ID: {e}")
        finally:
            conn.close()

    @staticmethod
    def remove_guardian(guardian_id):
        conn = sqlite3.connect(DatabaseManager.DATABASE_FILE)
        cursor = conn.cursor()

        try:
            cursor.execute('DELETE FROM "GUARDIAN INFORMATION" WHERE "GUARDIAN ID" = ?', (guardian_id,))
            conn.commit()
            print(f"Guardian with ID {guardian_id} removed from 'GUARDIAN INFORMATION' table.")
        except sqlite3.Error as e:
            print(f"Error removing guardian: {e}")
        finally:
            conn.close()

    @staticmethod
    def remove_student(student_id):
        conn = sqlite3.connect(DatabaseManager.DATABASE_FILE)
        cursor = conn.cursor()

        try:
            cursor.execute('DELETE FROM "STUDENTS INFORMATION" WHERE "STUDENT ID" = ?', (student_id,))
            conn.commit()
            print(f"Student with ID {student_id} removed from 'STUDENTS INFORMATION' table.")
        except sqlite3.Error as e:
            print(f"Error removing student: {e}")
        finally:
            conn.close()

    @staticmethod
    def remove_checkpoint(checkpoint_id):
        conn = sqlite3.connect(DatabaseManager.DATABASE_FILE)
        cursor = conn.cursor()

        try:
            cursor.execute('DELETE FROM CHECKPOINT WHERE "CHECKPOINT ID" = ?', (checkpoint_id,))
            conn.commit()
            print(f"Checkpoint with ID {checkpoint_id} removed from 'CHECKPOINT' table.")
        except sqlite3.Error as e:
            print(f"Error removing checkpoint: {e}")
        finally:
            conn.close()

    import sqlite3
import numpy as np

class YourClassName:
    # ... other methods and class attributes ...

    @staticmethod
    def get_students_guardians_checkpoints(cls):
        try:
            conn = sqlite3.connect(cls.DATABASE_FILE)
            cursor = conn.cursor()

            # Query to retrieve student and guardian information along with checkpoint details
            cursor.execute('''
                SELECT
                    S."FIRST NAME" AS "STUDENT FIRST NAME",
                    S."LAST NAME" AS "STUDENT LAST NAME",
                    G."FIRST NAME" AS "GUARDIAN FIRST NAME",
                    G."LAST NAME" AS "GUARDIAN LAST NAME",
                    G."PHONE NUMBER" AS "GUARDIAN PHONE NUMBER",
                    C."LONGITUDE" AS "CHECKPOINT LONGITUDE",
                    C."LATITUDE" AS "CHECKPOINT LATITUDE"
                FROM "STUDENTS INFORMATION" S
                INNER JOIN "GUARDIAN INFORMATION" G ON S."GUARDIAN ID" = G."GUARDIAN ID"
                LEFT JOIN CHECKPOINT C ON S."CHECKPOINT ID" = C."CHECKPOINT ID"
                ''')

            result = cursor.fetchall()

            # Convert the result into a NumPy array for better data manipulation
            data_array = np.array(result, dtype=[('Student First Name', 'U50'),
                                                ('Student Last Name', 'U50'),
                                                ('Guardian First Name', 'U50'),
                                                ('Guardian Last Name', 'U50'),
                                                ('Guardian Phone Number', 'U50'),
                                                ('Checkpoint Longitude', float),
                                                ('Checkpoint Latitude', float)])

            return data_array

        except sqlite3.Error as e:
            print(f"Error getting student and guardian data: {e}")
        finally:
            conn.close()


if __name__ == '__main__':
    # Create the database and tables
    DatabaseManager.set_database_file('my_database.db')  # Set the database file name

    DatabaseManager.create_database()

    # Insert data into the tables
    DatabaseManager.insert_checkpoint(12.34, 56.78, 'Sample Location')

    # Insert a guardian
    DatabaseManager.insert_guardian('John', 'Doe', '123-456-7890', 'G12345')

    # Insert a student and link to a checkpoint and guardian
    DatabaseManager.insert_student('Alice', 'Smith', DatabaseManager.get_last_checkpoint_id(), 2)

    # Query data from the database
    conn = sqlite3.connect(DatabaseManager.DATABASE_FILE)
    cursor = conn.cursor()

    # Example: Retrieve all students with their guardian's phone number
    students_with_guardian_phone = cursor.fetchall()
    for student in students_with_guardian_phone:
        print(f'Student: {student[0]} {student[1]}, Guardian Phone: {student[2]}')

    conn.close()
