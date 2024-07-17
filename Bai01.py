import tkinter as tk

def create_window():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Ghi khung hình")
    root.geometry("600x300")
    root.configure(bg="lightpink")

    # Thêm nhãn tiêu đề lớn ở giữa
    title_label = tk.Label(root, text="Ghi khung hình", font=("Arial", 24), bg="lightpink")
    title_label.pack(pady=20)

    # Thêm trường đầu vào FPS với nhãn
    fps_frame = tk.Frame(root, bg="lightpink")
    fps_label = tk.Label(fps_frame, text="tạo một", font=("Arial", 12), bg="lightpink")
    fps_label.pack(side=tk.LEFT)
    fps_entry = tk.Entry(fps_frame, width=5)
    fps_entry.pack(side=tk.LEFT)
    fps_text_label = tk.Label(fps_frame, text="fps video", font=("Arial", 12), bg="lightpink")
    fps_text_label.pack(side=tk.LEFT)
    fps_frame.pack(pady=10)

    # Thêm các nút trong một hàng
    button_frame = tk.Frame(root, bg="lightpink")
    pause_button = tk.Button(button_frame, text="Tạm dừng", width=10)
    pause_button.pack(side=tk.LEFT, padx=10)
    start_button = tk.Button(button_frame, text="Bắt đầu", width=10)
    start_button.pack(side=tk.LEFT, padx=10)
    end_button = tk.Button(button_frame, text="Kết thúc", width=10)
    end_button.pack(side=tk.LEFT, padx=10)
    button_frame.pack(pady=10)

    # Thêm nhãn trạng thái
    status_label = tk.Label(root, text="Đang tạm dừng ghi", font=("Arial", 12), bg="lightpink")
    status_label.pack(pady=10)

    root.mainloop()

create_window()
