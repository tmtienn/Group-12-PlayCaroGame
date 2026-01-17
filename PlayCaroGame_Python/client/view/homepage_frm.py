"""
Homepage Form - Main menu after login
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
from client.controller.client import Client
from shared.utils import create_message, format_win_ratio, calculate_mark
from shared.constants import *

class HomePageFrm:
    """Homepage form - main menu"""
    
    def __init__(self):
        # Always use Toplevel, never reassign Client.root
        if hasattr(Client, 'root') and Client.root:
            self.window = tk.Toplevel(Client.root)
            self.is_main_window = False
        else:
            # Fallback: create new Tk (shouldn't happen in normal flow)
            self.window = tk.Tk()
            self.is_main_window = True
            # DON'T reassign Client.root - let run_client.py handle it
        
        self.window.title("Trang chủ - Caro Game")
        self.window.geometry("900x700")  # Increased size for better layout
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.setup_ui()
        self.center_window()
    
    def center_window(self):
        """Center window on screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_ui(self):
        """Setup UI components"""
        # Title bar with harmonious colors
        title_frame = tk.Frame(self.window, bg="#4A90E2", height=80)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        # Title with icon
        title_container = tk.Frame(title_frame, bg="#4A90E2")
        title_container.pack(expand=True)
        
        tk.Label(
            title_container,
            text="🎮 CARO GAME",
            font=("Segoe UI", 24, "bold"),
            bg="#4A90E2",
            fg="white"
        ).pack(pady=(10, 0))
        
        tk.Label(
            title_container,
            text="Chào mừng bạn đến với thế giới Caro!",
            font=("Segoe UI", 10),
            bg="#4A90E2",
            fg="#E8F4FD"
        ).pack(pady=(0, 10))
        
        # Main content with harmonious background
        content_frame = tk.Frame(self.window, bg="#F8F9FA")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Welcome message with green accent
        if Client.user:
            welcome_frame = tk.Frame(content_frame, bg="#E8F5E9", relief="ridge", bd=2)
            welcome_frame.pack(fill=tk.X, pady=(0, 20))
            tk.Label(
                welcome_frame,
                text=f"Xin chào {Client.user.get_nickname()}! Chúc bạn chơi vui vẻ!",
                font=("Segoe UI", 12, "bold"),
                bg="#E8F5E9",
                fg="#2E7D32"
            ).pack(pady=10)
        
        # Content area
        main_area = tk.Frame(content_frame, bg="#F8F9FA")
        main_area.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - User info (harmonious colors)
        left_panel = tk.Frame(main_area, bg="white", relief="groove", bd=2, width=300)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        left_panel.pack_propagate(False)
        
        self.setup_user_info(left_panel)
        
        # Right panel - Menu and History/Chat
        right_panel = tk.Frame(main_area, bg="#F8F9FA")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Menu buttons in grid layout
        menu_frame = tk.LabelFrame(right_panel, text="🎯 Menu Chức Năng", font=("Segoe UI", 12, "bold"), 
                                 bg="white", fg="#4A90E2", padx=15, pady=15, relief="groove", bd=2)
        menu_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.setup_menu_buttons(menu_frame)
        
        # History section
        history_frame = tk.LabelFrame(right_panel, text="📜 Lịch Sử Trận Đấu", font=("Segoe UI", 10, "bold"), 
                                    bg="white", fg="#FF6B35", padx=10, pady=10, relief="groove", bd=2)
        history_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.setup_history(history_frame)
        
        # Chat (disabled as requested)
        chat_frame = tk.LabelFrame(right_panel, text="💬 Chat Server (Tạm thời không khả dụng)", font=("Segoe UI", 10, "bold"), 
                                 bg="#F5F5F5", fg="#999", padx=10, pady=10, relief="groove", bd=2)
        chat_frame.pack(fill=tk.X)
        
        self.setup_chat(chat_frame)
    
    def setup_history(self, parent):
        """Setup game history section"""
        # Sample history data (in real app, this would come from database)
        history_text = tk.Text(
            parent,
            font=("Segoe UI", 9),
            height=4,
            state=tk.NORMAL,
            bg="#FFF8E1",
            relief="flat",
            bd=1,
            wrap=tk.WORD
        )
        history_text.pack(fill=tk.BOTH, expand=True)
        
        # Insert sample history
        sample_history = """📅 Trận đấu gần đây:
• Thắng vs Player123 (17/01/2026)
• Hòa vs CaroMaster (16/01/2026)  
• Thua vs AI (15/01/2026)
• Thắng vs Guest (14/01/2026)

💡 Mẹo: Xem chi tiết trong Bảng xếp hạng!"""
        
        history_text.insert(tk.END, sample_history)
        history_text.config(state=tk.DISABLED)
    
    def setup_user_info(self, parent):
        """Setup user information panel with harmonious colors"""
        # Header with harmonious color
        header_frame = tk.Frame(parent, bg="#4A90E2", height=40)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="👤 THÔNG TIN NGƯỜI CHƠI",
            font=("Segoe UI", 11, "bold"),
            bg="#4A90E2",
            fg="white"
        ).pack(pady=8)
        
        # Avatar display
        avatar_frame = tk.Frame(parent, bg="white", width=120, height=120)
        avatar_frame.pack(pady=15)
        avatar_frame.pack_propagate(False)
        
        # Try to load avatar image
        if Client.user and hasattr(Client.user, 'get_avatar'):
            try:
                from PIL import Image, ImageTk
                from shared.utils import get_asset_path
                import os
                
                avatar_id = Client.user.get_avatar()
                avatar_path = get_asset_path('avatar', f'{avatar_id}.jpg')
                
                if os.path.exists(avatar_path):
                    img = Image.open(avatar_path)
                    img = img.resize((110, 110), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    avatar_label = tk.Label(avatar_frame, image=photo, bg="white")
                    avatar_label.image = photo  # Keep reference!
                    avatar_label.pack(expand=True)
                else:
                    tk.Label(avatar_frame, text="👤", bg="#E3F2FD", fg="#1976D2", font=("Arial", 40)).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            except Exception as e:
                tk.Label(avatar_frame, text="👤", bg="#E3F2FD", fg="#1976D2", font=("Arial", 40)).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            tk.Label(avatar_frame, text="👤", bg="#E3F2FD", fg="#1976D2", font=("Arial", 40)).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # User name with harmonious color
        if Client.user:
            tk.Label(
                parent,
                text=Client.user.get_nickname(),
                font=("Segoe UI", 14, "bold"),
                bg="white",
                fg="#4A90E2"
            ).pack(pady=(0, 15))
            
            # Stats in a nicer layout with harmonious colors
            stats_frame = tk.Frame(parent, bg="white")
            stats_frame.pack(fill=tk.X, padx=15, pady=10)
            
            # Stats labels with icons and harmonious colors
            user = Client.user
            stats = [
                ("🎯 Số ván:", user.get_number_of_game()),
                ("🏆 Thắng:", user.get_number_of_win()),
                ("🤝 Hòa:", user.get_number_of_draw()),
                ("📊 Tỷ lệ thắng:", format_win_ratio(user.get_number_of_win(), user.get_number_of_game())),
                ("⭐ Điểm:", calculate_mark(user.get_number_of_game(), user.get_number_of_win())),
                ("🥇 Hạng:", user.get_rank())
            ]
            
            for label, value in stats:
                row = tk.Frame(stats_frame, bg="white")
                row.pack(fill=tk.X, pady=3)
                tk.Label(row, text=label, font=("Segoe UI", 9), bg="white", fg="#666").pack(side=tk.LEFT)
                tk.Label(row, text=str(value), font=("Segoe UI", 9, "bold"), bg="white", fg="#4A90E2").pack(side=tk.RIGHT)
    
    def setup_menu_buttons(self, parent):
        """Setup menu buttons in grid layout with harmonious colors"""
        buttons = [
            ("🎮 Tìm phòng nhanh", self.quick_match, "#4CAF50", 0, 0),  # Green
            ("➕ Tạo phòng", self.create_room, "#2196F3", 0, 1),       # Blue
            ("🔍 Danh sách phòng", self.room_list, "#00BCD4", 1, 0),   # Cyan
            ("👥 Bạn bè", self.friend_list, "#FF9800", 1, 1),          # Orange
            ("🏆 Bảng xếp hạng", self.rank_board, "#9C27B0", 2, 0),    # Purple
            ("🤖 Chơi với AI", self.play_ai, "#607D8B", 2, 1),         # Blue Grey
            ("🚪 Đăng xuất", self.logout, "#F44336", 3, 0),            # Red
        ]
        
        for text, command, color, row, col in buttons:
            btn = tk.Button(
                parent,
                text=text,
                font=("Segoe UI", 11, "bold"),
                bg=color,
                fg="white",
                activebackground=self.darken_color(color),
                cursor="hand2",
                command=command,
                width=18,
                height=2,
                relief="raised",
                bd=3
            )
            btn.grid(row=row, column=col, padx=8, pady=8, sticky="ew")
            
            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn, c=color: self.on_hover_enter(b, c))
            btn.bind("<Leave>", lambda e, b=btn, c=color: self.on_hover_leave(b, c))
        
        # Configure grid weights
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
    
    def darken_color(self, color):
        """Darken a hex color for hover effect"""
        if color.startswith('#'):
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            r = max(0, r - 30)
            g = max(0, g - 30)
            b = max(0, b - 30)
            return f'#{r:02x}{g:02x}{b:02x}'
        return color
    
    def on_hover_enter(self, button, original_color):
        """Handle button hover enter"""
        button.config(bg=self.darken_color(original_color))
    
    def on_hover_leave(self, button, original_color):
        """Handle button hover leave"""
        button.config(bg=original_color)
    
    def setup_chat(self, parent):
        """Setup chat area (disabled)"""
        # Chat display (disabled)
        self.chat_text = scrolledtext.ScrolledText(
            parent,
            wrap=tk.WORD,
            font=("Segoe UI", 9),
            height=3,
            state=tk.DISABLED,
            bg="#F5F5F5",
            fg="#999",
            relief="flat",
            bd=1
        )
        self.chat_text.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        
        # Insert disabled message
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, "Chat tạm thời không khả dụng.\nVui lòng sử dụng các chức năng khác.")
        self.chat_text.config(state=tk.DISABLED)
        
        # Chat input (disabled)
        input_frame = tk.Frame(parent, bg="#F5F5F5")
        input_frame.pack(fill=tk.X)
        
        self.chat_input = tk.Entry(input_frame, font=("Segoe UI", 9), relief="flat", bd=1, state=tk.DISABLED, bg="#F5F5F5")
        self.chat_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        send_btn = tk.Button(
            input_frame,
            text="📤 Gửi",
            font=("Segoe UI", 9, "bold"),
            bg="#CCC",
            fg="#666",
            state=tk.DISABLED,
            width=6,
            relief="flat",
            bd=1
        )
        send_btn.pack(side=tk.RIGHT)
    
    def add_message(self, message):
        """Add message to chat"""
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, message + "\n")
        self.chat_text.see(tk.END)
        self.chat_text.config(state=tk.DISABLED)
    
    def send_message(self):
        """Send chat message"""
        message = self.chat_input.get().strip()
        if message and Client.socket_handle:
            Client.socket_handle.write(create_message(PROTOCOL_CHAT_SERVER, message))
            self.chat_input.delete(0, tk.END)
    
    # Button handlers
    def quick_match(self):
        """Quick match"""
        if Client.socket_handle:
            Client.socket_handle.write(create_message(PROTOCOL_QUICK_ROOM))
            # Don't open waiting room immediately
            # Wait for server response (PROTOCOL_GO_TO_ROOM or PROTOCOL_YOUR_CREATED_ROOM)
            # Server will send room_id in response
            self.close()
    
    def create_room(self):
        """Create room"""
        Client.open_create_room()
    
    def room_list(self):
        """Show room list"""
        self.close()
        Client.open_room_list()
    
    def friend_list(self):
        """Show friend list"""
        self.close()
        Client.open_friend_list()
    
    def rank_board(self):
        """Show rank board"""
        Client.open_rank()
    
    def play_ai(self):
        """Play with AI"""
        Client.open_ai_game()
    
    def logout(self):
        """Logout"""
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn đăng xuất?"):
            if Client.socket_handle and Client.user:
                Client.socket_handle.write(create_message(PROTOCOL_OFFLINE, Client.user.get_id()))
            self.close()
            Client.open_login()
    
    def on_closing(self):
        """Handle window closing"""
        self.logout()
    
    def show(self):
        """Show window"""
        self.window.deiconify()
        # Don't call mainloop here - it's called in run_client.py
    
    def close(self):
        """Close window"""
        try:
            self.window.destroy()
        except:
            pass
