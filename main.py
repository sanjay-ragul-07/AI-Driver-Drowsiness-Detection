import cv2
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_eye.xml"
)

if face_cascade.empty():
    print("ERROR: Face detector not loaded!")
    exit()

if eye_cascade.empty():
    print("ERROR: Eye detector not loaded!")
    exit()

print("Face detector loaded!")
print("Eye detector loaded!")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Camera could not be opened!")
    exit()

print("Camera started!")
print("Press Q or ESC to exit.")

eye_closed_start = None
DROWSY_TIME = 3.0

cv2.namedWindow(
    "Driver Monitoring",
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    "Driver Monitoring",
    900,
    650
)

while True:

    ret, frame = camera.read()

    if not ret:
        print("ERROR: Cannot read camera!")
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    if len(faces) > 0:

        x, y, w, h = faces[0]

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "FACE DETECTED",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            face_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(25, 25)
        )

        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(
                face_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (255, 0, 0),
                2
            )

        if len(eyes) > 0:

            eye_closed_start = None

            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()

            cv2.putText(
                frame,
                "EYES OPEN - AWAKE",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        else:

            if eye_closed_start is None:
                eye_closed_start = time.time()

            closed_time = time.time() - eye_closed_start

            cv2.putText(
                frame,
                f"EYES CLOSED: {closed_time:.1f} sec",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

            if closed_time >= DROWSY_TIME:

                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play(-1)

                cv2.putText(
                    frame,
                    "DROWSY DETECTED!",
                    (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    (0, 0, 255),
                    3
                )

                cv2.putText(
                    frame,
                    "WAKE UP DRIVER!",
                    (30, 145),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    (0, 0, 255),
                    3
                )

    else:

        eye_closed_start = None

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        cv2.putText(
            frame,
            "NO FACE DETECTED",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

    cv2.imshow(
        "Driver Monitoring",
        frame
    )

    key = cv2.waitKey(30) & 0xFF

    if key == ord("q") or key == ord("Q") or key == 27:
        print("Exit key detected!")
        break

camera.release()

pygame.mixer.music.stop()
pygame.mixer.quit()

cv2.destroyAllWindows()

cv2.waitKey(1)

print("Driver monitoring closed successfully.")