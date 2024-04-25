# Habit Tracker App
By Vishesh Vaibhav

## Overview
The Habit Tracker App is a command-line-based application designed to help users track and manage their habits. It allows users to create new habits, edit existing habits, check off completed habits, analyze habit data, and delete habits.

## Common Challenges in Habit Tracking
- **Lack of Consistency**: It can be hard to stick to habits without regular reminders or accountability.
- **Difficulty in Monitoring Progress**: Without a proper tracking system, it's challenging to measure progress and identify patterns.
- **Limited Insights**: Understanding habit trends and streaks can be valuable for personal growth, but these insights are often difficult to glean from simple notes or memory.

## How This App Addresses These Challenges
- **Organized Habit Tracking**: This app allows you to create, edit, and delete habits easily, providing a structured way to manage your routine.
- **Automatic Streak Analysis**: The app includes a streak analysis feature that helps identify your longest streaks, offering motivation to maintain consistency.
- **Customization and Flexibility**: Users can categorize habits by frequency, duration, and other criteria, allowing for a personalized experience.
- **Simplified Habit Check-Off**: The app's check-off feature makes it easy to mark habits as completed, reinforcing a sense of achievement.

## The Benefits of Habit Tracking
- **Improved Accountability**: Having a system to track habits helps increase accountability and encourages you to stick with your commitments.
- **Enhanced Productivity**: With consistent habits, you can achieve more in your personal and professional life.
- **Greater Self-Awareness**: Tracking habits provides insights into your behavior and allows you to make informed decisions about your routines.
- **Goal Achievement**: Whether it's health, work, or personal development, consistent habit tracking helps you reach your goals.


## Features
- **Create New Habits**: Define new habits with specific categories, frequencies (daily/weekly), and durations.
- **Edit Habits**: Modify existing habit details such as name, category, and duration.
- **Analyze Habits**: Analyze habits, including streak analysis and habit reporting.
- **Delete Habits**: Remove habits that are no longer needed.
- **Pre-Defined Habits**: Add and report on a set of pre-defined habits.

## Installation
To run the Habit Tracker App, you'll need Python and the required dependencies installed on your system.

### Dependencies
- Python 3.x
- SQLite
- [Questionary](https://github.com/tmbo/questionary) (for interactive CLI prompts)
- [Tabulate](https://github.com/astanin/python-tabulate) (for table formatting)

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/visheshvaibhav/Habit-Tracking-Application
   #Change directory to Habit-Tracking-Application
2. **Install Dependencies from requirements.txt file**:
   ```bash
   pip install -r requirements.txt
3. **Run the Application**:
   ```bash
   python main.py
# Usage

Upon running the application, you'll be greeted with a welcome message and a menu with various options. Select an option using the keyboard and follow the on-screen prompts.

## Menu Options
- **Create a New Habit**: Add a new habit by providing the habit name, category, frequency, and duration.

<img width="918" alt="Screenshot 2024-04-26 at 2 32 16 AM" src="https://github.com/visheshvaibhav/Habit-Tracking-Application/assets/60804493/75f63632-bead-4034-8b97-81bdbbd18d05">

- **Edit a Habit**: Edit an existing habit by selecting from the list of habits and modifying the desired attributes.

<img width="918" alt="Screenshot 2024-04-26 at 2 33 15 AM" src="https://github.com/visheshvaibhav/Habit-Tracking-Application/assets/60804493/9c5e2dce-f55c-4973-9b7d-023b34dacb88">

- **Analyze Habit/Check-off**: Check off completed habits or analyze habit data. This includes streak analysis and habit reports.

<img width="1075" alt="Screenshot 2024-04-26 at 2 33 49 AM" src="https://github.com/visheshvaibhav/Habit-Tracking-Application/assets/60804493/898b204e-8143-434a-a41c-993b924dce95">

- **Pre-Defined Habits**: Look at the different predefined habits.

<img width="1075" alt="Screenshot 2024-04-26 at 2 34 36 AM" src="https://github.com/visheshvaibhav/Habit-Tracking-Application/assets/60804493/7d0e19ae-64f2-44c2-9e22-e4b037e136e3">

- **Delete a Habit**: Delete an existing habit by selecting from the list of habits.

<img width="1075" alt="Screenshot 2024-04-26 at 2 35 05 AM" src="https://github.com/visheshvaibhav/Habit-Tracking-Application/assets/60804493/1596afd3-b0d5-421c-9393-1abb887cfd8e">

- **Exit**: Exit the application.

<img width="1077" alt="Screenshot 2024-04-26 at 2 35 31 AM" src="https://github.com/visheshvaibhav/Habit-Tracking-Application/assets/60804493/a7d43934-4690-4f25-9e1e-b6fab0bfb609">

## Streak Analysis
The streak analysis feature provides insights into the longest streaks of daily and weekly habits, along with the longest streak for a given habit.

# Troubleshooting
If you encounter errors or issues, consider the following steps:
- Ensure the database file (`habit_tracker.db`) exists and has the correct structure.
- Check for typos or misnamed variables in the code.
- Validate that the required dependencies are installed.
- If the streak analysis feature reports no habits, ensure habits are added and have valid data.

# Contact
For questions, suggestions, or support, please contact me at deskofvisheshvaibhav@gmail.com
