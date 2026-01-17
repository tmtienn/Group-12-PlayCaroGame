# 🎮 Caro Game Python

Một trò chơi Caro (Gomoku) được phát triển bằng Python với kiến trúc client-server, hỗ trợ chơi với người chơi khác, AI, và các tính năng mạng xã hội.

## 📋 Mục lục
- [Tính năng](#tính-năng)
- [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
- [Cài đặt](#cài-đặt)
- [Chạy chương trình](#chạy-chương-trình)
- [Cấu trúc thư mục](#cấu-trúc-thư-mục)
- [Công nghệ sử dụng](#công-nghệ-sử-dụng)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)

## ✨ Tính năng

### 🎯 Chơi game
- **Chơi với người**: Tìm phòng nhanh, tạo phòng riêng tư
- **Chơi với AI**: Máy tính với các mức độ khó khác nhau
- **Chế độ xem**: Xem các trận đấu đang diễn ra

### 👥 Mạng xã hội
- **Đăng ký/Đăng nhập**: Hệ thống tài khoản người dùng
- **Danh sách bạn bè**: Thêm/Kết bạn
- **Bảng xếp hạng**: Xếp hạng người chơi theo điểm số
- **Chat server**: Trò chuyện với người chơi khác

### 🎨 Giao diện
- **GUI hiện đại**: Sử dụng Tkinter với thiết kế đẹp mắt
- **Responsive**: Tự động điều chỉnh kích thước cửa sổ
- **Icons & Emojis**: Giao diện trực quan với biểu tượng

## 💻 Yêu cầu hệ thống

- **Python**: 3.8 trở lên
- **Hệ điều hành**: Windows, macOS, Linux
- **RAM**: 512MB trở lên
- **Đĩa**: 100MB dung lượng trống

## 🚀 Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/your-username/caro-game-python.git
cd caro-game-python
```

### 2. Tạo virtual environment (khuyến nghị)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 4. Khởi tạo database
Database SQLite sẽ được tự động tạo khi chạy server lần đầu.

## 🎮 Chạy chương trình

### Chạy Server
```bash
python run_server.py
```
Server sẽ khởi động trên port 7777 với giao diện admin.

### Chạy Client
```bash
python run_client.py
```
Mở giao diện đăng nhập. Tài khoản mặc định: `admin/admin123`

### Chạy cả hai cùng lúc
Mở 2 terminal riêng biệt:
- Terminal 1: `python run_server.py`
- Terminal 2: `python run_client.py`

## 📁 Cấu trúc thư mục

```
PlayCaroGame_Python/
├── requirements.txt              # Dependencies Python
├── run_client.py                 # Script chạy client
├── run_server.py                # Script chạy server
├── test_*.py                     # Files test
├── assets/                       # Tài nguyên game
│   ├── avatar/                   # Ảnh avatar người dùng
│   ├── game/                     # Tài nguyên game
│   ├── icon/                     # Icons ứng dụng
│   ├── image/                    # Hình ảnh chung
│   └── sound/                    # Âm thanh
├── client/                       # Code client
│   ├── main.py                   # Entry point client
│   ├── controller/               # Logic xử lý client
│   │   ├── client.py             # Main client controller
│   │   ├── socket_handle.py      # Xử lý socket
│   │   └── __init__.py
│   └── view/                     # Giao diện người dùng
│       ├── homepage_frm.py       # Trang chủ
│       ├── login_frm.py          # Đăng nhập
│       ├── game_client_frm.py    # Giao diện game
│       └── ...                   # Các form khác
├── server/                       # Code server
│   ├── main.py                   # Entry point server
│   ├── controller/               # Logic xử lý server
│   │   ├── server.py             # Main server controller
│   │   ├── room.py               # Quản lý phòng
│   │   ├── server_thread.py      # Thread xử lý client
│   │   └── server_thread_bus.py  # Bus quản lý threads
│   ├── dao/                      # Data Access Objects
│   │   ├── database.py           # Kết nối database
│   │   └── user_dao.py           # Xử lý dữ liệu user
│   └── view/                     # Giao diện admin
│       └── admin.py              # Panel quản trị
├── shared/                       # Code dùng chung
│   ├── config.py                 # Cấu hình
│   ├── constants.py              # Hằng số
│   ├── game_logic.py             # Logic game Caro
│   ├── point.py                  # Class Point
│   ├── user.py                   # Class User
│   └── utils.py                  # Utilities
└── database/
    └── init_database.sql         # Schema database
```

## 🛠 Công nghệ sử dụng

### Backend
- **Python 3.13**: Ngôn ngữ chính
- **SQLite**: Cơ sở dữ liệu
- **Socket Programming**: Mạng client-server
- **Threading**: Xử lý đa luồng

### Frontend
- **Tkinter**: GUI framework
- **Pillow**: Xử lý hình ảnh
- **Pygame**: Âm thanh và multimedia

### Libraries
- **python-dateutil**: Xử lý ngày tháng
- **sqlite3**: Database operations (built-in)

## 🧪 Chạy Tests

```bash
# Chạy tất cả tests
python test_all_fixes.py

# Test hệ thống
python test_system.py

# Test game logic
python test_game_context.py
```

## 🤝 Đóng góp

1. Fork project
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📝 Quy tắc đóng góp

- Tuân thủ PEP 8 style guide
- Viết docstring cho functions
- Test code trước khi commit
- Sử dụng meaningful commit messages

## 🐛 Báo lỗi

Nếu bạn tìm thấy lỗi, vui lòng tạo issue trên GitHub với:
- Mô tả lỗi chi tiết
- Steps to reproduce
- Expected behavior
- Screenshots (nếu có)

## 📄 Giấy phép

Dự án này sử dụng giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 👥 Tác giả

- **Nhóm 12**: Phát triển dự án Caro Game Python
- **GitHub**: [your-username](https://github.com/your-username)

## 🙏 Lời cảm ơn

Cảm ơn tất cả contributors và người dùng đã hỗ trợ dự án!

---

**Chúc bạn chơi vui vẻ! 🎮✨**</content>
<parameter name="filePath">c:\Users\Van Minh\Downloads\Group-12-PlayCaroGame\PlayCaroGame_Python\README.md