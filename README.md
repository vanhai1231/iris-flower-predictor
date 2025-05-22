## 🌸 MLOps Project: DVC + MLflow + AI Agent + Iris Classifier

### 🌟 Mục tiêu

Thiết lập một workflow MLOps cơ bản, bao gồm:

* Quản lý dữ liệu và pipeline bằng DVC
* Theo dõi quá trình huấn luyện bằng MLflow
* Tự động hóa pipeline với AI Agent
* Triển khai mô hình bằng Gradio

---

### 📁 Cấu trúc thư mục

```
mlops-project/
├── data/
│   ├── raw/                # Dữ liệu gốc (iris.csv)
│   └── processed/          # Dữ liệu đã xử lý
├── model/                  # Mô hình đã train (model.pkl)
├── src/
│   ├── preprocess.py       # Tiền xử lý dữ liệu
│   ├── train.py            # Huấn luyện và log MLflow
│   └── agent.py            # AI Agent theo dõi thay đổi dữ liệu
├── app.py                  # Gradio demo mô hình
├── dvc.yaml                # Pipeline DVC
├── params.yaml             # Tham số mô hình
├── metrics.json            # Kết quả training
├── requirements.txt
└── README.md
```

---

### ⚙️ Cài đặt & khởi tạo

```bash
git clone https://github.com/your-username/mlops-project.git
cd mlops-project

python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

pip install -r requirements.txt
```

---

### 🧪 Chạy pipeline với DVC

```bash
dvc repro
```

> Tự động chạy:
>
> * `preprocess.py`: xử lý dữ liệu
> * `train.py`: huấn luyện mô hình, log MLflow, lưu model + metrics

---

### 📊 Mở giao diện theo dõi MLflow

```bash
mlflow ui
```

Mở trình duyệt tại: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 🤖 Chạy AI Agent để tự động hóa pipeline

```bash
python src/agent.py
```

> Agent sẽ tự động `dvc repro` khi file `data/raw/iris.csv` thay đổi.

---

### 🌐 Demo mô hình bằng Gradio

```bash
python app.py
```

> Mở trình duyệt tại: [http://127.0.0.1:7860](http://127.0.0.1:7860)
> Cho phép bạn nhập các đặc trưng của hoa Iris và xem dự đoán loài.

---

### 📉 Ghi chú

* Mô hình sử dụng: `LogisticRegression` từ `sklearn`
* Dữ liệu: Bộ dữ liệu `Iris` chuẩn
* MLflow được dùng để log `C` và `accuracy`

---

