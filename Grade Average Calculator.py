#
# Aaron Deaver
#
# Grade Calculator program

# Import tkinter module
import tkinter as tk

# Import .messagebox
import tkinter.messagebox as mb

TEST_WEIGHT = 0.20  # 20% Tests
LAB_WEIGHT = 0.30   # 30% Lab
EXAM_WEIGHT = 0.50  # 50% Exam

class MyGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tk.Tk()
        self.main_window.title('Grade Calculator')
        self.main_window.geometry('260x125')

        # Assign a frame to main window
        self.frame1 = tk.Frame(self.main_window)
        self.frame2 = tk.Frame(self.main_window)
        self.frame3 = tk.Frame(self.main_window)
        self.frame4 = tk.Frame(self.main_window)
        self.frame5 = tk.Frame(self.main_window)
        # Create labels using tkinter
        self.label1 = tk.Label(self.frame1, text='Tests Grade: ')
        self.label1.pack()

        self.label2 = tk.Label(self.frame2, text='Labs Grade: ')
        self.label2.pack()

        self.label3 = tk.Label(self.frame3, text='Exams Grade: ')
        self.label3.pack()

        self.label4 = tk.Label(self.frame4, text='Grade Average:')
        # Use StringVar
        self.average_value = tk.StringVar()
        # Associate with label
        self.average_result_value = tk.Label(self.frame4,
                                             textvariable=self.average_value)

        # Set the StringVar value
        self.average_value.set('00.0 ()')
        self.label4.pack(side='left')
        # .pack the StringVar
        self.average_result_value.pack(side='left')

        # Call Pack method for frame1 and frame2
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        # Create buttons with tkinter
        self.button1 = tk.Button(self.frame5,
                                 text='Calculate',
                                 command=self.show_message)
        # Create Quit button and attach destroy function to close application
        self.quit_button = tk.Button(self.frame5, text='Quit',
                                 command=self.main_window.destroy)
        # Call button
        self.quit_button.pack(side='right')
        self.button1.pack(side='right')

        # Create Entry Widget
        self.test_entry = tk.Entry(self.frame1,
                                   width=10)  # Adjust width
        # Make sure to use .pack with label and entry
        self.label1.pack(side='left')
        self.test_entry.pack(side='left')

        self.lab_entry = tk.Entry(self.frame2,
                                  width=10)  # Adjust width
        self.label2.pack(side='left')
        self.lab_entry.pack(side='left')

        self.exam_entry = tk.Entry(self.frame3,
                                   width=10)  # Adjust width
        self.label3.pack(side='left')
        self.exam_entry.pack(side='left')



        # Enter tkinter main loop
        tk.mainloop()

    # Print the button function
    def show_message(self):
        # Input entry instance with try except block
        try:
            test_grade = float(self.test_entry.get())  # Make sure to convert to float
            labs_grade = float(self.lab_entry.get())
            exam_grade = float(self.exam_entry.get())

            average =  ((test_grade * TEST_WEIGHT) +
                         (labs_grade * LAB_WEIGHT) +
                         (exam_grade * EXAM_WEIGHT))  # Grade average calculation

            # Determine the letter grade
            if average >= 90:
                letter_grade = 'A'
            elif average >= 80:
                letter_grade = 'B'
            elif average >= 70:
                letter_grade = 'C'
            elif average >= 60:
                letter_grade = 'D'
            else:
                letter_grade = 'F'
            # Set the StringVar with the letter grade
            self.average_value.set(f'{average:.1f} ({letter_grade})')
        except ValueError:
            self.average_value.set('Error')



my_gui = MyGUI()
print('Program done')
