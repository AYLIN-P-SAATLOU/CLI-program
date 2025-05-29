{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "af9c03ab-5771-4eec-8a83-03af3af75164",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'habit'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[9]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[34;01mhabit\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Habit\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[34;01mHabitTracker\u001b[39;00m:\n\u001b[32m      4\u001b[39m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[34m__init__\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'habit'"
     ]
    }
   ],
   "source": [
    "from habit import Habit\n",
    "\n",
    "class HabitTracker:\n",
    "    def __init__(self):\n",
    "        self.habit: []\n",
    "\n",
    "    def add_habit(self, name):\n",
    "        if any(h.name.lower() == name.lower() for h in self.habits):\n",
    "            print(\"Habit already exists.\")\n",
    "            return\n",
    "        self.habits.append(Habit(name))\n",
    "        print(f\"Habit '{name}' added.\")\n",
    "\n",
    "    def mark_habit_done(self, name):\n",
    "        for habit in self.habits:\n",
    "            if habit.name.lower() == name.lower():\n",
    "                habit.mark_done()\n",
    "                return\n",
    "        print(f\"No habit found with the name '{name}'.\")\n",
    "\n",
    "    def view_habits(self):\n",
    "        if not self.habits:\n",
    "            print(\"No habits to show.\")\n",
    "            return\n",
    "        for idx, habit in enumerate(self.habits, start=1):\n",
    "            print(f\"{idx}. {habit}\")\n",
    "\n",
    "    def reset_all_for_new_day(self):\n",
    "        for habit in self.habits:\n",
    "            habit.reset_day()\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfeed8dc-75da-45b5-8f38-4c77d79d4310",
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
