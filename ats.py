import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Application Manager")

        self.candidate_button = tk.Button(root, text="Candidate", command=self.candidate_view)
        self.candidate_button.pack(pady=10)

        self.recruiter_button = tk.Button(root, text="Recruiter", command=self.recruiter_view)
        self.recruiter_button.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

    def candidate_view(self):
        self.clear_frame()

        self.label = tk.Label(self.frame, text="Choose your option:")
        self.label.pack(pady=5)

        self.options = [
    "Data Scientist",
    "Data Engineer",
    "Database Administrator",
    "Data Analyst",
    "Machine Learning Engineer",
    "Web Developer",
    "Front End Developer",
    "Back End Developer",
    "Full Stack Developer",
    "UI/UX Designer",
    "Android Developer",
    "Mobile App Developer",
    "Quality Assurance (QA) Tester"
    "Database Developer",
    "Data Architect",
    "SQL Developer",
    "VR/AR Developer",
    "Unity Developer",
    "Cloud Architect",
    "Cloud Engineer",
    "DevOps Engineer",
    "Cloud Security Engineer",
    "Cloud Solutions Architect",
    "Big Data Engineer",
    "Network Engineer",
    "Network Administrator",
    "Network Architect",
    "Network Security Engineer",
    "Wireless Network Engineer",
    "Security Analyst",
    "Penetration Tester",
    "Security Engineer",
    "Security Consultant",
    "Talent Acquisition Specialist",]
        self.combobox = Combobox(self.frame, values=self.options)
        self.combobox.pack(pady=5)

        self.upload_button = tk.Button(self.frame, text="Upload PDF", command=self.upload_pdf)
        self.upload_button.pack(pady=5)

    def recruiter_view(self):
        self.clear_frame()

        self.label = tk.Label(self.frame, text="Paste Job Description:")
        self.label.pack(pady=5)

        self.job_desc_text = tk.Text(self.frame, height=10, width=40)
        self.job_desc_text.pack(pady=5)

        self.select_folder_button = tk.Button(self.frame, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=5)

    def upload_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            messagebox.showinfo("File Selected", f"Selected file: {file_path}")

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            messagebox.showinfo("Folder Selected", f"Selected folder: {folder_path}")

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
