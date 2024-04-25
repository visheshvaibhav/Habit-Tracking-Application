from backend import *


class Test_Habit_tracker:

    def test_add_habit(self):
        create_habit = AddHabit()
        create_habit.add_habit(name='Run', category='Health', frequency='daily',
                               duration='10 days', db_path='database/pre-defined.db')

    def test_edit_habit(self):
        manage_habit = edit_habit(
            habit_name='Run', choice='Habit Name', edited_value='Football')
        manage_habit.edit_habit('database/pre-defined.db')

    def test_analysis(self):
        analyze_habit = habit_analysis()
        analyze_habit.check_off('Football', 'database/pre-defined.db')
        analyze_habit.report('All habits', 'database/pre-defined.db')
