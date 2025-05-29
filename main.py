{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2aef11eb-8483-4e3b-bb61-67655039039f",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'habit_tracker'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[34;01mhabit_tracker\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m HabitTracker\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[34mmain\u001b[39m():\n\u001b[32m      4\u001b[39m     tracker = HabitTracker()\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'habit_tracker'"
     ]
    }
   ],
   "source": [
    "from habit_tracker import HabitTracker\n",
    "\n",
    "def main():\n",
    "    tracker = HabitTracker()\n",
    "\n",
    "    while True:\n",
    "        print(\"\\n=== Habit Tracker Menu ===\")\n",
    "        print(\"1. Add Habit\")\n",
    "        print(\"2. Mark Habit as Done\")\n",
    "        print(\"3. View All Habits\")\n",
    "        print(\"4. Reset for New Day\")\n",
    "        print(\"5. Exit\")\n",
    "\n",
    "        choice = input(\"Choose an option: \")\n",
    "\n",
    "        if choice == \"1\":\n",
    "            name = input(\"Enter habit name: \")\n",
    "            tracker.add_habit(name)\n",
    "\n",
    "        elif choice == \"2\":\n",
    "            name = input(\"Enter habit name to mark as done: \")\n",
    "            tracker.mark_habit_done(name)\n",
    "\n",
    "        elif choice == \"3\":\n",
    "            tracker.view_habits()\n",
    "\n",
    "        elif choice == \"4\":\n",
    "            tracker.reset_all_for_new_day()\n",
    "            print(\"All habits reset for a new day.\")\n",
    "\n",
    "        elif choice == \"5\":\n",
    "            print(\"Goodbye!\")\n",
    "            break\n",
    "\n",
    "        else:\n",
    "            print(\"Invalid choice. Please try again.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4fd9360-48a3-4f12-a98d-fddd59f001f0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
