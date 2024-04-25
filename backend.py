import datetime as dt
from db import *
import sqlite3
import questionary
from datetime import date


def extract_habit_name(db_path):
    """This function is responsible for extracting habit names from the SQLite database.
        :param db_path: the name of the db file
     """

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    rows = c.execute("SELECT habit_name FROM habits")

    listed_rows = [row[0] for row in rows]

    return listed_rows


# Add habit class

class AddHabit:
    """
        This class creates a habit and stores it in "habit_tracker.db"

            Method:
                add_habit(self, habit_name, habit_category, habit_frequency, habit_duration, db_path)
                    Adds a new habit and stores it in the database
    """

    def add_habit(self, habit_name: str, habit_category: str, habit_frequency: str, habit_duration: str, db_path):
        """
        :param habit_name: the name of the habit
        :param habit_category: the category of the habit
        :param habit_frequency: the frequency of the habit
        :param habit_duration: how long the habit lasts
        :param db_path: the name of the db file
        """

        start_date = dt.datetime.now().strftime("%Y-%m-%d")

        db = get_db(db_path)
        create_habit(db=db, habit_name=habit_name, habit_category=habit_category,
                     habit_frequency=habit_frequency, habit_duration=habit_duration, start_date=start_date, check_off=0, last_check_off="-", streak=0, longest_streak=0)


class edit_habit:

    """
        This class allows the users to edit the name/category/duration of the given habit.

            Arguments:
                habit_name: the name of the habit that needs to be edited
                choice: the user's choice of what should be edited in habit (name/category/duration)
                edited_value: the new value that the users edits

            Methods:
                edit(self, db_path):
                    Updates the name/category/duration of the specified habit in the database

    """

    def __init__(self, habit_name, choice, edited_value):
        """
        Init Function

        :param habit_name: the name of the habit that needs to be edited
        :param choice: the user's choice of what should be edited in habit (name/category/duration)
        :param edited_value: the new value that the user edited
        """

        column_names = {
            'Habit Name': 'habit_name',
            'Habit Category': 'habit_category',
            'Habit Duration': 'habit_duration'
        }

        self.habit_name = habit_name
        self.choice = column_names[choice]
        self.edited_value = edited_value

    def edit_habit(self, db_path):
        """ Changes the name/category/duration of the specified habit in the database. 

            :param db_path: the name of the database file
        """

        db = get_db(db_path)

        db.execute(
            f"UPDATE habits SET {self.choice} = '{self.edited_value}'"
            f"WHERE habit_name = '{self.habit_name}'")
        db.commit()


class habit_analysis:

    """
    This class allows users to check or analyze all habits or a single habit.

        Methods:
            check_off(self, habit_name, db_path):
                This function is responsible for checking off the habit after its completion.

            streak(self, habit_name, habit_frequency, db_path):
                Counts the streak and updates the streak by calculating the difference between the check-off

            streak_analysis(self, choice, db_path):
                Gives analytics on the habits such as longest streak of among all habits, given habit, dailt habits or a weekly habits.

            report(self, choce, db_path):
                Displays the details of the habits in a table.
    """

    def check_off(self, habit_name, db_path):

        db = sqlite3.connect(db_path)
        c = db.cursor()

        c.execute(
            f"SELECT check_off FROM habits WHERE habit_name = '{habit_name}';")
        check_off = list(c.fetchone())[0]

        c.execute(
            f"SELECT check_off FROM habits WHERE habit_name = '{habit_name}';")
        habit_frequency = list(c.fetchone())[0]

        self.streak(habit_name, habit_frequency, db_path)

        now = dt.datetime.now().strftime("%Y-%m-%d")
        c.execute(f"UPDATE habits SET check_off = '{check_off + 1}', last_check_off = '{now}'"
                  f"WHERE habit_name = '{habit_name}';")

        db.commit()

    def streak(self, habit_name, habit_frequency, db_path):

        db = sqlite3.connect(db_path)
        c = db.cursor()
        dif = ''

        if habit_frequency == 'daily':
            dif = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y-%m-%d")

        elif habit_frequency == 'weekly':
            dif = (dt.datetime.now() - dt.timedelta(weeks=1)
                   ).strftime("%Y-%m-%d")

        c.execute(
            f"SELECT last_check_off FROM habits WHERE habit_name = '{habit_name}';")

        last_check_off = list(c.fetchone())[0]

        c.execute(
            f"SELECT streak FROM habits WHERE habit_name = '{habit_name}';")

        longest_streak = list(c.fetchone())[0]

        if last_check_off == dif:
            c.execute(f"UPDATE habits SET streak = '{streak + 1}'"
                      f"WHERE habit_name = '{habit_name}';")
            db.commit()

            if longest_streak <= streak+1:
                longest_streak += 1
                c.execute(f"UPDATE habits SET longest_streak = '{longest_streak}'"
                          f"WHERE habit_name = '{habit_name}';")
                db.commit()

        else:
            streak = 1
            c.execute(f"UPDATE habits SET streak = '{streak}'"
                      f"WHERE habit_name = '{habit_name}';")
            db.commit()

            if longest_streak == 0:
                c.execute(f"UPDATE habits SET longest_streak = '{longest_streak + 1}'"
                          f"WHERE habit_name = '{habit_name}';")
                db.commit()

    def report(self, choice, db_path):
        table = ''
        db = get_db(db_path)

        if choice == 'all habits':
            table = get_table(db, condition=None, value=None)

        elif choice == 'all daily habits':
            table = get_table(db, condition='habit_frequency', value='daily')

        elif choice == 'all weekly habits':
            table = get_table(db, condition='habit_frequency', value='weekly')

        elif choice == 'one habit':
            name = questionary.select(
                'Select habit you want the report for', choices=extract_habit_name(db_path)).ask()
            table = get_table(db, condition='habit_name', value=f'{name}')

        print(table)

    def streak_analysis(self, choice, db_path):
        """
                Method that 
                i) returns a list of all habits with the same periodicity,
                ii) return the longest run streak of all defined habits,
                iii) return the longest run streak for a given habit,
                iv) returns the longest streak among all weekly or daily habits

        """

        db = get_db(db_path)
        c = db.cursor()

        if choice == 'all habits':
            c.execute("SELECT longest_streak FROM habits")
            longest_streak = [row[0] for row in c.fetchall()]
            print(f'The longest streak among all habits is: {
                  max(longest_streak)}')

        elif choice == 'one habit':
            name = questionary.select(
                'Select habit you want the report for', choices=extract_habit_name(db_path)).ask()
            c.execute(
                f"SELECT longest_streak FROM habits WHERE habit_name = '{name}'")
            longest_streak = list(c.fetchone())[0]
            print(f'The longest streak for {name} is: {longest_streak}')

        elif choice == 'all weekly habits':
            c.execute(
                "SELECT longest_streak FROM habits WHERE habit_frequency = 'weekly'")
            longest_streak = [row[0] for row in c.fetchall()]
            print(
                f'The longest streak among all weekly habits is: {max(longest_streak)}')

        elif choice == 'all daily habits':
            c.execute(
                "SELECT longest_streak FROM habits WHERE habit_frequency = 'daily'")
            longest_streak = [row[0] for row in c.fetchall()]
            print(
                f'The longest streak among all daily habits is: {max(longest_streak)}')


class Pre_Defined_Habits:

    """
    Class that Creates and reports the predefined habits for unit-test

    Method:
            add_predefined_habits(self, db_path):
                responsible for creating the predefined habits

            report_predefined_habits(self,db_path):
                gets the predefined habits from the database and displays it in a table

    """

    def add_pre_defined_habits(self, db_path):
        db = get_db(db_path)
        create_habit(db=db, habit_name='Run', habit_category='Health',
                     habit_frequency='daily', habit_duration='100 days', start_date='2024-04-05', check_off=5, last_check_off="2024-04-10", streak=5, longest_streak=5)
        create_habit(db=db, habit_name='Read', habit_category='Personal',
                     habit_frequency='daily', habit_duration='50 days', start_date='2024-03-05', check_off=30, last_check_off="2024-04-05", streak=30, longest_streak=30)
        create_habit(db=db, habit_name='Meditate', habit_category='Health',
                     habit_frequency='weekly', habit_duration='3 weeks', start_date='2024-02-01', check_off=3, last_check_off="2024-02-03", streak=3, longest_streak=3)
        create_habit(db=db, habit_name='Drink Water', habit_category='Health',
                     habit_frequency='daily', habit_duration='365 days', start_date='2024-01-01', check_off=50, last_check_off="2024-03-01", streak=10, longest_streak=15)
        create_habit(db=db, habit_name='Write', habit_category='Personal',
                     habit_frequency='daily', habit_duration='20 days', start_date='2024-01-10', check_off=20, last_check_off="2024-02-20", streak=5, longest_streak=11)

    def report_pre_defined_habits(self, db_path):

        db = get_db(db_path)
        table = get_table(db, condition=None, value=None)
        print(table)


class Delete_Habit:

    """
    This class allows users to delete any habit from the database

        Method:
            delete_the_habit(self, name, db_path):
                This function is responsible for deleting the habit by its name.

    """

    def delete_habit(self, habit_name, db_path):

        db = sqlite3.connect(db_path)
        c = db.cursor()

        c.execute(f"DELETE FROM habits "
                  f"WHERE habit_name = '{habit_name}'")

        db.commit()
