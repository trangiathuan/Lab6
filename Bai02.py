import tkinter as tk

def create_window():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("AtarBals Modern Antivirus")
    root.geometry("800x500")
    root.configure(bg="white")

    # Tạo khung chính
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Tạo thanh bên
    sidebar = tk.Frame(main_frame, bg="blue", width=200)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    # Thêm các nhãn và nút vào thanh bên
    options = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
    for option in options:
        label = tk.Label(sidebar, text=option, fg="white", bg="blue", font=("Arial", 12), anchor="w", padx=10)
        label.pack(fill=tk.X, pady=5)

    scan_now_button = tk.Button(sidebar, text="Scan Now", bg="green", fg="white", font=("Arial", 14), padx=10, pady=5)
    scan_now_button.pack(pady=20)

    # Tạo khu vực chính
    content_frame = tk.Frame(main_frame, bg="white")
    content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Thêm nhãn tiêu đề và phụ đề
    title_label = tk.Label(content_frame, text="Scan", font=("Arial", 24, "bold"), bg="white")
    title_label.pack(pady=20)

    subtitle_label = tk.Label(content_frame, text="Premium will be free forever. You just need to click button.", font=("Arial", 12), bg="white")
    subtitle_label.pack(pady=10)

    # Thêm các nút chức năng
    button_texts = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
    button_commands = [None, None, None, None, None]  # Thay bằng các hàm thực tế nếu có
    for i, text in enumerate(button_texts):
        button = tk.Button(content_frame, text=text, bg="magenta", fg="black", font=("Arial", 14), width=15, height=2, command=button_commands[i])
        button.pack(pady=5)

    # Thêm nhãn trạng thái
    status_label = tk.Label(content_frame, text="Get Premium to Enable: (Web Protection), (Full Scan), (Simple Update)", font=("Arial", 12), bg="white", fg="magenta")
    status_label.pack(pady=20)

    root.mainloop()

create_window()
