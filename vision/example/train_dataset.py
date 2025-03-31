from ultralytics import YOLO

def main():
    # Cargar modelo base
    model = YOLO('yolov8n.pt')

    # Entrenar
    results = model.train(
        data='datasets/data.yaml',
        epochs=50,
        imgsz=640,
        batch=8,
        name='objetos_laboratorio'
    )

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
