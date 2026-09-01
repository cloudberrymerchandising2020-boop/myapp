import tkinter as tk
from tkinter import filedialog, messagebox


def build_greeting(name: str) -> str:
    name = name.strip()
    if name:
        return f"Hello, {name}!"
    return "Hello, stranger!"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("500x400")

        self._build_menu()
        self._build_widgets()

    def _build_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(
            label="Open...", command=self.open_file, accelerator="Cmd+O"
        )
        file_menu.add_command(
            label="Save As...", command=self.save_file, accelerator="Cmd+S"
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

        self.bind("<Command-o>", lambda event: self.open_file())
        self.bind("<Command-s>", lambda event: self.save_file())

    def _build_widgets(self):
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.name_entry = tk.Entry(self, width=25)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.greeting_label = tk.Label(self, text="Hello, Tkinter!")
        self.greeting_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.greet_button = tk.Button(self, text="Greet", command=self.on_greet)
        self.greet_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.text = tk.Text(self, wrap="word", undo=True)
        self.text.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def on_greet(self):
        name = self.name_entry.get()
        self.greeting_label.config(text=build_greeting(name))

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except OSError as e:
            messagebox.showerror("Error", f"Could not open file:\n{e}")
            return
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", content)
        self.title(f"My App — {path}")

    def save_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END))
        except OSError as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
            return
        self.title(f"My App — {path}")

    def show_about(self):
        messagebox.showinfo("About", "My App v0.1.0\nBuilt with Tkinter + Poetry.")


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
