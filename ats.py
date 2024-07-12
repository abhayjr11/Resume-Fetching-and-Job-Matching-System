import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
from pathlib import Path
import fitz  # PyMuPDF
import os
import re




data_it_roles = [
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
    "Big Data Engineer",
    "Network Engineer",
    "Network Administrator",
    "Network Architect",
    "Network Security Engineer",
    "Wireless Network Engineer",
    "Penetration Tester",
    "Talent Acquisition Specialist",]



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
    "Talent Acquisition Specialist"]
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

        #self.show_pdf_button = tk.Button(self.frame, text="Show Content", command=self.pdf_content)
        #self.show_pdf_button.pack(pady=5)

    def replace_multiple(self,text, replacements):
        # Create a regular expression from the keys of the replacements dictionary
        regex = re.compile("|".join(map(re.escape, replacements.keys())))
    
        # Replace function using the dictionary
        return regex.sub(lambda match: replacements[match.group(0)], text)

    def job_desc_txt(self):  # process the pasted job description converted to list

        jobd = self.job_desc_text
        rep = { ": ":",", " (":",", ") ":",", ")":",", "\n":",", ",  ":",", ", ":",", ",,":",", ", ,":",", " and ":",", "  ":"" , "for ":"" }
        a = self.replace_multiple(jobd , rep)
        self.job_desc_list =a.split(',')
        return self.job_desc_list

    def upload_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            messagebox.showinfo("File Selected", f"Selected file: {file_path}")

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        return folder_path

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def reader(self,file_path):
        self.text = ""
        try:
            with fitz.open(file_path) as pdf_document:
                for page_num in range(len(pdf_document)):
                    page = pdf_document.load_page(page_num)
                    text += page.get_text()
        except Exception as e:
            print(f"file has not any text")
        return self.text

    def read_n_save(self):
        # Initialize a list to store the contents of each PDF
        self.pdf_contents = []
        path=self.select_folder()  # folder path
        self.pdf_file  # actual path of file

        pdf_files=self.fetch_pdf  # list of pdf files fetch from folder

        for f in pdf_files:
            pdf_file = path+"\\"+f        
            # Iterate through the list of PDF files, read their content, and append it to pdf_contents
            pdf_text = self.reader(pdf_file)
            self.pdf_contents.append(pdf_text)

        return self.pdf_contents

            
    def fetch_pdf(self):
        directory_path = self.select_folder()
        pdf_files=[]
        # Get a list of all files in the directory
        all_files = os.listdir(directory_path)

        # Optionally, filter for specific file types, e.g., PDF files
        pdf_files = [f for f in all_files if f.endswith('.pdf')]
        for pdf_file in pdf_files:
            pdf_files.append(pdf_file)
        return pdf_files


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
