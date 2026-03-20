import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import dns_lookup
import re


# Domain validation
def is_valid_domain(domain):

    pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,}$"

    if re.match(pattern, domain):
        return True

    return False


def clear_results(event=None):

    for row in result_table.get_children():
        result_table.delete(row)

    status_label.config(text="Results cleared")


# SAVE RESULTS FUNCTION
def save_results():

    domain = domain_entry.get().strip()

    if domain == "":
        messagebox.showerror("Error", "No domain entered")
        return

    rows = result_table.get_children()

    if len(rows) == 0:
        messagebox.showerror("Error", "No results to save")
        return

    filename = domain + ".txt"

    try:

        with open(filename, "w") as file:

            file.write("===== DNS ENUMERATION RESULT =====\n\n")
            file.write("Domain: " + domain + "\n\n")

            for row in rows:
                values = result_table.item(row)["values"]
                file.write(f"{values[0]} : {values[1]}\n")

        status_label.config(text=f"Results saved to {filename}")
        messagebox.showinfo("Saved", f"Results saved as {filename}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def enumerate_dns(event=None):

    domain = domain_entry.get().strip()

    if domain == "":
        messagebox.showerror("Error", "Please enter a domain name")
        return

    if not is_valid_domain(domain):
        messagebox.showerror(
            "Invalid Domain",
            "Please enter a valid domain (example: google.com)"
        )
        return

    clear_results()

    status_label.config(text="Scanning DNS records...")
    root.update()

    try:

        a_records = dns_lookup.get_a_records(domain)
        mx_records = dns_lookup.get_mx_records(domain)
        ns_records = dns_lookup.get_ns_records(domain)
        txt_records = dns_lookup.get_txt_records(domain)

        row_index = 0

        for record in a_records:
            tag = "even" if row_index % 2 == 0 else "odd"
            result_table.insert("", "end", values=("A", record), tags=(tag,))
            row_index += 1

        for record in mx_records:
            tag = "even" if row_index % 2 == 0 else "odd"
            result_table.insert("", "end", values=("MX", record), tags=(tag,))
            row_index += 1

        for record in ns_records:
            tag = "even" if row_index % 2 == 0 else "odd"
            result_table.insert("", "end", values=("NS", record), tags=(tag,))
            row_index += 1

        for record in txt_records:
            tag = "even" if row_index % 2 == 0 else "odd"
            result_table.insert("", "end", values=("TXT", record), tags=(tag,))
            row_index += 1

        status_label.config(text="Scan complete")

    except Exception as e:
        status_label.config(text="Error occurred")
        messagebox.showerror("Error", str(e))


# MAIN WINDOW
root = tk.Tk()
root.title("DNS Enumeration Tool")
root.geometry("800x560")
root.configure(bg="#1e1e1e")


# TITLE
title = tk.Label(
    root,
    text="DNS RECONNAISSANCE TOOL",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1e1e1e"
)

title.pack(pady=15)


# INPUT FRAME
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(pady=10)


domain_label = tk.Label(
    input_frame,
    text="Enter Domain:",
    fg="white",
    bg="#1e1e1e",
    font=("Arial", 11)
)

domain_label.grid(row=0, column=0, padx=5)


domain_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 11)
)

domain_entry.grid(row=0, column=1, padx=5)


# ENTER KEY SCAN
domain_entry.bind("<Return>", enumerate_dns)

domain_entry.focus()


scan_button = tk.Button(
    input_frame,
    text="Scan DNS",
    command=enumerate_dns,
    bg="#00aaff",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10
)

scan_button.grid(row=0, column=2, padx=10)


# SAVE BUTTON
save_button = tk.Button(
    input_frame,
    text="Save Results",
    command=save_results,
    bg="#28a745",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10
)

save_button.grid(row=0, column=3, padx=10)


# TABLE FRAME
table_frame = tk.Frame(root)
table_frame.pack(pady=15, fill="both", expand=True)


columns = ("Record Type", "Value")

result_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

result_table.heading("Record Type", text="Record Type")
result_table.heading("Value", text="Value")

result_table.column("Record Type", width=120, anchor="center")
result_table.column("Value", width=650, anchor="w", stretch=True)

result_table.pack(side="left", fill="both", expand=True)


# SCROLLBAR
scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=result_table.yview
)

result_table.configure(yscroll=scrollbar.set)

scrollbar.pack(side="right", fill="y")


# ROW COLORS
result_table.tag_configure("odd", background="#f2f2f2")
result_table.tag_configure("even", background="#ffffff")


# STATUS BAR
status_label = tk.Label(
    root,
    text="Ready",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 10)
)

status_label.pack(pady=5)


# CLEAR SHORTCUT
root.bind("<Control-l>", clear_results)


root.mainloop()