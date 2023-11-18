import tkinter as tk

class FibonacciGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Fibonacci Generator")
        master.geometry("800x600")  # Set the window size to 800x600

        # Configure a light blue background
        master.configure(bg="#ADD8E6")

        self.label = tk.Label(master, text="Enter the number of Fibonacci numbers:", bg="#ADD8E6")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.generate_button = tk.Button(master, text="Generate Fibonacci Numbers", command=self.generate_fibonacci, bg="lightgreen")
        self.generate_button.pack(pady=10)

        self.result_text = tk.Text(master, height=15, width=50, wrap=tk.WORD)
        self.result_text.pack(pady=10)

    def generate_fibonacci(self):
        try:
            n = int(self.entry.get())
            fib_sequence = self.calculate_fibonacci(n)
            self.display_result(fib_sequence)
        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please enter a valid number.")

    def calculate_fibonacci(self, n):
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def display_result(self, fib_sequence):
        self.result_text.delete(1.0, tk.END)
        for num in fib_sequence:
            self.result_text.insert(tk.END, f"{num}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciGenerator(root)
    root.mainloop()
