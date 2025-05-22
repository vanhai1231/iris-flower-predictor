import gradio as gr
import joblib
import numpy as np

# Load mô hình đã huấn luyện
model = joblib.load("model/model.pkl")

# Map label -> thông tin loài hoa
class_info = {
    0: {
        "name": "Iris-setosa 🌱",
        "description": "Iris-setosa là loài nhỏ nhất trong 3 loài, thường có cánh hoa ngắn và màu xanh tím.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Iris_setosa_2.jpg/330px-Iris_setosa_2.jpg"
    },
    1: {
        "name": "Iris-versicolor 🌷",
        "description": "Iris-versicolor có màu sắc đa dạng và thường được tìm thấy ở vùng đất ngập nước.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Verschiedenfarbige_Schwertlilie_%28Iris_versicolor%29-20200603-RM-100257.jpg/330px-Verschiedenfarbige_Schwertlilie_%28Iris_versicolor%29-20200603-RM-100257.jpg"
    },
    2: {
        "name": "Iris-virginica 🌸",
        "description": "Iris-virginica có kích thước lớn nhất và thường mọc ở bờ sông hoặc đầm lầy.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/250px-Iris_virginica_2.jpg"
    }
}

def predict(sepal_length, sepal_width, petal_length, petal_width):
    X = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(X)[0]
    info = class_info.get(prediction, {})
    return (
        info.get("name", "Không xác định"),
        info.get("description", "Không có mô tả"),
        info.get("image", "")
    )

# Giao diện hiện đại dùng Blocks
with gr.Blocks(title="🌸 Dự đoán Loài Hoa Iris") as demo:
    gr.Markdown("## 🔍 Nhập thông số để dự đoán loài hoa Iris")
    
    with gr.Row():
        sepal_length = gr.Number(label="Sepal Length (cm)")
        sepal_width = gr.Number(label="Sepal Width (cm)")
        petal_length = gr.Number(label="Petal Length (cm)")
        petal_width = gr.Number(label="Petal Width (cm)")

    submit_btn = gr.Button("Dự đoán")

    with gr.Column():
        label_output = gr.Text(label="Tên loài")
        desc_output = gr.Textbox(label="Thông tin loài", lines=2)
        image_output = gr.Image(label="Ảnh minh họa")

    submit_btn.click(fn=predict,
                     inputs=[sepal_length, sepal_width, petal_length, petal_width],
                     outputs=[label_output, desc_output, image_output])

# Chạy app
if __name__ == "__main__":
    demo.launch()
