import tkinter as tk
from tkinter import messagebox
import random

# Quiz Questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Index of correct option
    },
    {
        "topic": "Lists",
        "question": "How do you access the third element of a list `lst`?",
        "code": "",
        "options": ["lst[3]", "lst[2]", "lst[-1]", "lst[1]"],
        "answer": 1
    },
    {
        "topic": "Strings",
        "question": "What will be the output of `print('hello'[::-1])`?",
        "code": "",
        "options": ["hello", "olleh", "h", "None"],
        "answer": 1
    }
]

# Initialize Tkinter Window
root = tk.Tk()
root.title("Python Code Quiz Generator")
root.geometry("600x500")
root.configure(bg="white")

# Input field for topic
tk.Label(root, text="Enter Python Topic (e.g., loops, lists, strings)", bg="white").pack(pady=5)
topic_entry = tk.Entry(root, width=40)
topic_entry.pack(pady=5)

# Button to generate a question
generate_btn = tk.Button(root, text="Generate Python Question")
generate_btn.pack(pady=10)

# Question display area
question_frame = tk.Frame(root, bg="white")
question_frame.pack(pady=10)

question_label = tk.Label(question_frame, text="", bg="white", font=("Arial", 12))
question_label.pack()

code_label = tk.Label(question_frame, text="", bg="white", font=("Courier", 10))
code_label.pack()

# Answer choices
selected_answer = tk.IntVar()
option_buttons = []

for i in range(4):  # Assuming 4 options per question
    btn = tk.Radiobutton(root, text="", variable=selected_answer, value=i, bg="white")
    option_buttons.append(btn)
    btn.pack(anchor="w")

# Submit button
submit_btn = tk.Button(root, text="Submit Answer")
submit_btn.pack(pady=10)

# Feedback label
feedback_label = tk.Label(root, text="", bg="white", font=("Arial", 12, "bold"))
feedback_label.pack()

# Function to Generate a Question
def generate_question():
    topic = topic_entry.get().strip().lower()
    filtered_questions = [q for q in questions if q["topic"].lower() == topic]
    
    if not filtered_questions:
        messagebox.showerror("Error", "No questions found for this topic.")
        return

    question = random.choice(filtered_questions)  # Pick a random question
    question_label.config(text=f"Topic: {question['topic']}\n\n{question['question']}")
    code_label.config(text=question["code"] if question["code"] else "")
    
    for i, option in enumerate(question["options"]):
        option_buttons[i].config(text=option)
    
    submit_btn.config(command=lambda: check_answer(question))

# Function to Check the Answer
def check_answer(question):
    selected_index = selected_answer.get()
    
    if selected_index == question["answer"]:
        feedback_label.config(text="Correct! Well done! 🎉", fg="green")
    else:
        feedback_label.config(text="Incorrect. Try again.", fg="red")

# Attach Button to Function
generate_btn.config(command=generate_question)

# Run Tkinter Main Loop
root.mainloop()
