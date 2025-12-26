import cv2
import mediapipe as mp
import pygame
import time
import os

pygame.mixer.init()

def load_sound(filename):
    if os.path.exists(filename):
        return pygame.mixer.Sound(filename)
    else:
        print(f"PERINGATAN: File {filename} tidak ditemukan! Pastikan file ada di folder yang sama.")
        return None

sound_berjuang = load_sound("Berjuang.mp3")
sound_selamat = load_sound("Selamat.mp3")
sound_sukses = load_sound("Sukses.mp3")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

last_played_time = 0
cooldown_seconds = 1.5

def play_audio(sound_object):
    """Fungsi untuk memutar suara"""
    if sound_object:
        sound_object.play()

def count_fingers(hand_landmarks):
    """
    Mendeteksi jari mana saja yang terbuka.
    Return: List 5 boolean [Jempol, Telunjuk, Tengah, Manis, Kelingking]
    """
    fingers = []
    
    if hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y: 
         fingers.append(True) 
    else:
        fingers.append(False)

    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    
    for tip, pip in zip(tips, pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers.append(True)
        else:
            fingers.append(False)
            
    return fingers

# Buka Kamera
cap = cv2.VideoCapture(0)

print("Program berjalan... Pastikan file .mp3 sudah ada di folder.")
print("Tekan 'q' untuk keluar.")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    current_time = time.time()
    detected_gesture = ""
    target_sound = None
    
    if results.multi_hand_landmarks:
        hands_fingers_status = []
        
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
            fingers_status = count_fingers(hand_lms)
            hands_fingers_status.append(fingers_status)
            
        # --- LOGIKA GESTURE ---
        if len(hands_fingers_status) == 2:
            
            def is_thumb_up(fingers_list):
                return fingers_list[0] and not any(fingers_list[1:])

            hand1_is_thumb = is_thumb_up(hands_fingers_status[0])
            hand2_is_thumb = is_thumb_up(hands_fingers_status[1])
            
            if hand1_is_thumb and hand2_is_thumb:
                detected_gesture = "Sukses"
                target_sound = sound_sukses
        elif len(hands_fingers_status) == 1:
            fingers = hands_fingers_status[0]
            if not any(fingers):
                detected_gesture = "Berjuang"
                target_sound = sound_berjuang
            elif all(fingers):
                detected_gesture = "Selamat"
                target_sound = sound_selamat

        if detected_gesture:
            color = (0, 255, 0)
            cv2.putText(img, f"Mode: {detected_gesture}", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
            
            if (current_time - last_played_time) > cooldown_seconds:
                if target_sound:
                    play_audio(target_sound)
                    last_played_time = current_time
                    cv2.circle(img, (30, 40), 15, (0, 0, 255), -1) 

    cv2.imshow("Gesture Audio Player", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()