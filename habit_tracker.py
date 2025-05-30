from habit import Habit

class HabitTracker:
    def __init__(self):
        self.habits: []

    def add_habit(self, name):
        if any(h.name.lower() == name.lower() for h in self.habits):
            print("Habit already exists.")
            return
        self.habits.append(Habit(name))
        print(f"Habit '{name}' added.")

    def mark_habit_done(self, name):
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                habit.mark_done()
                return
        print(f"No habit found with the name '{name}'.")

    def view_habits(self):
        if not self.habits:
            print("No habits to show.")
            return
        for idx, habit in enumerate(self.habits, start=1):
            print(f"{idx}. {habit}")

    def reset_all_for_new_day(self):
        for habit in self.habits:
            habit.reset_day()