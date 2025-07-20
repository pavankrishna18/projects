import tkinter as tk
from tkinter import messagebox
from predict_url import predict_url

class URLCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing URL Detector")
        self.root.geometry("500x250")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="Enter URL:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), width=40)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Check", font=("Arial", 14), command=self.check_url)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def check_url(self):
        url = self.entry.get()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL")
            return
        result = predict_url(url)
        self.result_label.config(text=f"Result: {result}", fg="red" if result == "Phishing" else "green")

if __name__ == '__main__':
    root = tk.Tk()
    app = URLCheckerApp(root)
    root.mainloop()