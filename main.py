for habit_tracker import HabitTracker

def main():
    tracker = HabitTracker()

    while True:
        print("\n=== Habit Tracker Menu ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View All Habits")
        print("4. Reset for New Day")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter habit name: ")
            tracker.add_habit(name)
        
        elif choice == "2":
            name = input("Enter habit name to mark as done: ")
            tracker.mark_habit_done(name)

        elif choice == "3":
            tracker.view_habits()

        elif choice == "4":
            tracker.reset_all_for_new_day()
            print("All habits reset for a new day.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        
        