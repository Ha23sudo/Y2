def login_window():
    clear_window()

    tk.Label(root, text="Login", font=("Arial", 18)).pack(pady=10)

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if check_login(username, password):
            messagebox.showinfo("Success", "Login Successful!")
            main_menu(username)
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    tk.Button(root, text="Login", command=login).pack(pady=5)
    tk.Button(root, text="Go to Signup", command=signup_window).pack()


