import cv2
import argparse
from ultralytics import YOLO
import supervision as sv
import numpy as np
import sqlite3
from collections import Counter
conn = sqlite3.connect('results.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM class_counts")
conn.commit()
# Create a table to store the results
cursor.execute('''CREATE TABLE IF NOT EXISTS class_counts (
                    Products TEXT,
                    Available INTEGER,
                    InStock TEXT
                )''')

ZONE_POLYGON = np.array([
    [0.25, 0.35],
    [0.35, 0.35],
    [0.45, 0.55],
    [0.25, 0.55]
])


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution",
        default=[1280, 720],
        nargs=2,
        type=int
    )
    args = parser.parse_args()
    return args

def main():
    
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(1)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("weights-AIM.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=1,
        text_thickness=1,
        text_scale=0.4
    )

    zone_polygon = (ZONE_POLYGON * np.array(args.webcam_resolution)).astype(int)
    zone = sv.PolygonZone(polygon=zone_polygon, frame_resolution_wh=tuple(args.webcam_resolution))
    zone_annotator = sv.PolygonZoneAnnotator(
        zone=zone,
        color=sv.Color.green(),
        thickness=1,
        text_thickness=1,
        text_scale=1,
    )

    while True:
        ret, frame = cap.read()

        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_yolov8(result)
        labels = [
            model.model.names[class_id]
            for _, _, class_id, _
            in detections
        ]
        unique_classes = set()
        for label in labels:
            unique_classes.add(label)

        class_counts = Counter(labels)
        # Iterate over the unique class names and update the count in the database
        for name in unique_classes:
            cursor.execute("SELECT * FROM class_counts WHERE Products = ?", (name,))
            existing_row = cursor.fetchone()
            if existing_row:
                existing_count = class_counts[name]
                if existing_count is not None:
                    cursor.execute("UPDATE class_counts SET Available = ?, InStock = ? WHERE Products = ?",
                           (class_counts[name], "In Stock", name))
                if existing_count < 2:
                    cursor.execute("UPDATE class_counts SET Available = ?, InStock = ? WHERE Products = ?",
                           (class_counts[name], "Low Stock", name))
            else:
                cursor.execute("INSERT INTO class_counts (Products, Available, InStock) VALUES (?, ?, ?)",
                       (name, class_counts[name], "In Stock"))
        detected_classes = set(labels)

        # Fetch all the existing rows from the class_counts table
        cursor.execute("SELECT Products FROM class_counts")
        existing_classes = set(row[0] for row in cursor.fetchall())

        # Find the classes that are in the database but not detected
        classes_to_delete = existing_classes - detected_classes

        # Delete the rows for the classes that are not detected
        for class_name in classes_to_delete:
            #cursor.execute("DELETE FROM class_counts WHERE Class = ?", (class_name,))
            cursor.execute("UPDATE class_counts SET Available = 0, InStock = ? WHERE Products = ?",
                           ("Out Of Stock", class_name))
        frame = box_annotator.annotate(
            scene=frame,
            detections=detections,
            labels=labels
        )
        zone.trigger(detections=detections)
        frame = zone_annotator.annotate(scene=frame)
        cv2.imshow("yolov8", frame)


        conn.commit()
        if cv2.waitKey(30) == 27:
            cursor.close()
            conn.close()
            break


if __name__ == "__main__":
    main()

