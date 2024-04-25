import sqlite3
from tabulate import tabulate


def get_db(db_path):
    """
    This method is responsible for accessing the db file.
        :param db_path: the path of the db file
    """

    db = sqlite3.connect(db_path)
    create_table(db)
    return db


def create_table(db):
    """
    This method is responsible for creating tables in the database file.
        :param db: the name of the db file
    """

    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS habits
                    (habit_name varchar(250) NOT NULL, habit_category TEXT, habit_frequency TEXT, habit_duration varchar(250) NOT NULL, start_date varchar(250) NOT NULL, check_off INTEGER, last_check_off varchar(250) NOT NULL, streak INTEGER, longest_streak INTEGER)''')

    db.commit()


def create_habit(db, habit_name, habit_category, habit_frequency, habit_duration, start_date, check_off, last_check_off, streak, longest_streak):
    """
    This methdod is responsible for storing information about the habits in the database file.
        :param db: the name of the db file
        :param habit_name: the name of the habit
        :param habit_category: the category of the habit
        :param habit_frequency: the frequency of the habit
        :param habit_duration: how long the habit lasts
        :param start_date: the date when this habit was created
        :param check_off: how many times the habit was performed
        :param last_check_off: the day when the habit was marked as completed
        :param streak: the number of days habits were completed without being broken
        :param longest_streak: the number of the longest streak 
    """

    cursor = db.cursor()
    cursor.execute('''INSERT INTO habits (habit_name, habit_category, habit_frequency, habit_duration, start_date, check_off, last_check_off, streak, longest_streak)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (habit_name, habit_category, habit_frequency, habit_duration, start_date, check_off, last_check_off, streak, longest_streak))

    db.commit()


def get_table(db, condition, value):
    """
    This function is responsible for visualizing data about habits in a table.
        :param db: the name of the db file
        :param condition: the name of the column in the table
        :param value: the value of the column
    """

    cursor = db.cursor()

    if condition is None and value is None:
        rows = cursor.execute("SELECT * FROM habits")
    else:
        rows = cursor.execute(
            f"SELECT * FROM habits WHERE {condition} = '{value}'")
        db.commit()

    def table(lrows):
        """
        This method is responsible for creating a table with the data from the database and formatting a list of rows (lrows) into a table with headers for the tabulate module.

            :param lrows: the list of rows
        """

        first_row = ['Habit Name', 'Habit Category', 'Habit Frequency', 'Habit Duration',
                     'Start Date', 'Check Off', 'Last Check Off', 'Streak', 'Longest Streak']
        rows_list = [list(row) for row in lrows]
        rows_list.insert(0, first_row)
        return tabulate(rows_list, headers='firstrow', tablefmt='fancy_grid')

    table = table(lrows=rows)
    return table
