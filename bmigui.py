import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())  
        bmi = weight / (height ** 2)

        # Show result with 2 decimal places
        result_label.config(text=f"BMI: {bmi:.2f}")

        # Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        category_label.config(text=f"Category: {category}")

    except:
        messagebox.showerror("Error", "Enter valid numbers!")

# Create window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("1000x1000")

# Labels and Entries
tk.Label(root, text="Weight (kg):", font=("Arial",24)).grid(row=0,column=0,pady=20)
weight_entry = tk.Entry(root,width=50)
weight_entry.grid(row=0,column=1,pady=20)

tk.Label(root, text="Height (m):", font=('Arial',24)).grid(row=1,column=0,padx=100,pady=20)
height_entry = tk.Entry(root)
height_entry.grid(row=1,column=1,pady=20)

# Button
tk.Button(root, text="Calculate BMI",font=('Arial',24), command=calculate_bmi).grid(row=2,column=0,padx=100,pady=20)

# Result Labels
result_label = tk.Label(root, text="BMI: ",font=('Serif',24))
result_label.grid(row=3,column=0,padx=100,pady=20)

category_label = tk.Label(root, text="Category: ",font=('Serif',24))
category_label.grid(row=4,column=0,padx=100,pady=20)

# Run app
root.mainloop()