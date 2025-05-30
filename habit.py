class Habit:
    def __init__(self, name):
        self.name = name
        self.streak = 0
        self.completed_today = False

    def mark_done(self):
        if not self.completed_today:
            self.streak += 1
            self.completed_today = True
            print(f"Habit '{self.name}' marked as done. Streak is now {self.streak}.")
        else:
            print(f"Habit '{self.name}' is already marked as done today.")

    def reset_day(self):
        self.completed_today = False

    def __str__(self):
        status = "✓" if self.completed_today else "✗"
        return f"{self.name} - Streak: {self.streak} - Done Today: {status}"