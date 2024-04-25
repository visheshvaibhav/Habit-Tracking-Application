from backend import *
import questionary
import sqlite3


print('Welcome to Habit Tracker!')


def cli():

    i = True
    while i:

        choice = questionary.select(
            'What would you like to do?', choices=['Create a new habit', 'Edit a habit', 'Analyze Habit/Check-off', 'Pre-Defined Habits', 'Delete a Habit', 'Exit']).ask()

        if choice == 'Create a new habit':

            name = questionary.text('Enter the habit name:').ask().lower()
            category = questionary.select('Enter the habit category:', choices=[
                'Health', 'Work', 'Personal', 'Social', 'Other']).ask().lower()

            frequency = questionary.select('Enter the habit frequency:', choices=[
                                           'daily', 'weekly']).ask()

            duration = questionary.text(
                'Enter the habit duration: In days or weeks').ask().lower()

            create_habit = AddHabit()
            create_habit.add_habit(
                name, category, frequency, duration, db_path="database/habit_tracker.db")
            print("\nHabit created successfully!\n")

        elif choice == 'Edit a habit':
            try:
                habit_name = questionary.select(
                    'Select habit you want to edit', choices=extract_habit_name("database/habit_tracker.db")).ask()
                choice = questionary.select(
                    'What would you like to edit?', choices=['Habit Name', 'Habit Category', 'Habit Duration']).ask()

                edited_value = questionary.text(
                    f"Enter the new {choice}").ask().lower()

                manage_habit = edit_habit(habit_name, choice, edited_value)
                manage_habit.edit_habit(db_path="database/habit_tracker.db")
                print("\nHabit edited successfully!\n")

            except sqlite3.OperationalError and ValueError:
                print("\nPlease create a habit first\n")
                pass
        elif choice == 'Analyze Habit/Check-off':
            try:

                analyze_habit = habit_analysis()
                choice = questionary.select(
                    'What would you like to do?', choices=['Check-off', 'Analyze', 'Streak Analysis']).ask()

                if choice == 'Check-off':
                    name = questionary.select(
                        'Select habit you want to check-off', choices=extract_habit_name("database/habit_tracker.db")).ask().lower()
                    analyze_habit.check_off(
                        habit_name=name, db_path="database/habit_tracker.db")
                    print("\nHabit checked off successfully!\n")

                elif choice == 'Analyze':
                    choice = questionary.select(
                        'What would you like to see?', choices=['All habits', 'All daily habits', 'All weekly habits', 'One habit']).ask().lower()
                    analyze_habit.report(
                        choice, db_path="database/habit_tracker.db")

                elif choice == 'Streak Analysis':
                    choice = questionary.select(
                        'For which habit would you like to see the longest streak for?', choices=['All habits', 'All daily habits', 'All weekly habits', 'One habit']).ask().lower()
                    analyze_habit.streak_analysis(
                        choice, db_path="database/habit_tracker.db")

            except sqlite3.OperationalError and ValueError:
                print("\nPlease create a habit first\n")
                pass

        elif choice == 'Pre-Defined Habits':
            pre_defined_habits = Pre_Defined_Habits()
            pre_defined_habits.add_pre_defined_habits(
                db_path="database/pre-defined.db")
            pre_defined_habits.report_pre_defined_habits(
                db_path="database/pre-defined.db")

        elif choice == 'Delete a Habit':
            try:
                habit_name = questionary.select(
                    'Select habit you want to delete', choices=extract_habit_name("database/habit_tracker.db")).ask()
                delete_habit = Delete_Habit()

                delete_habit.delete_habit(
                    habit_name, db_path="database/habit_tracker.db")
                print("\nHabit deleted successfully!\n")

            except sqlite3.OperationalError and ValueError:
                print("\nPlease create a habit first\n")
                pass

        elif choice == 'Exit':
            print('Goodbye!')
            i = False

        else:
            pass


if __name__ == "__main__":
    cli()
