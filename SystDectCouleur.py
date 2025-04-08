import cv2
import numpy as np
import urllib.request
import time
from collections import defaultdict

# Paramètres
NOMBRE_VOITURES = 4
TOURS_A_FAIRE = 10

#Définir les gammes de couleurs en HSV
color_ranges = {
    "red": [(0, 50, 50), (10, 255, 255)],
    "yellow": [(20, 50, 50), (40, 255, 255)],
    "green": [(40, 50, 50), (90, 255, 255)],
    "blue": [(100, 50, 50), (130, 255, 255)],
    "dark blue": [(110, 50, 50), (130, 255, 255)]
}

# Suivi de voiture
tours_completes = defaultdict(int)  # Laps par voiture
temps_par_voiture = {color: [] for color in ["red", "blue", "green", "yellow"]}  # Ltemps de lap
voitures_en_course = {"red", "blue", "green", "yellow"}  # Voiture en course
last_detection_time = {}  # dernier lap
finish_times = {}  # Les temps total fait par chaque voiture

def detect_color(image):
    pixels = cv2.resize(image, (100, 100))
    pixels = cv2.cvtColor(pixels, cv2.COLOR_BGR2HSV)
    
    color_counts = {color: 0 for color in color_ranges}
    for row in pixels:
        for pixel in row:
            h, s, v = pixel
            for color, (lower, upper) in color_ranges.items():
                if lower[0] <= h < upper[0] and lower[1] <= s <= upper[1] and lower[2] <= v <= upper[2]:
                    color_counts[color] += 1
                    break
    
    return max(color_counts, key=color_counts.get) if any(color_counts.values()) else None

def afficher_classement():
    classement = sorted(tours_completes.items(), key=lambda x: x[1], reverse=True)
    print("\nClassement actuel:")
    for i, (voiture, tours) in enumerate(classement, 1):
        print(f"{i}. Voiture {voiture}: {tours} tours complétés")

def attendre_signal_depart():
    input("Appuyez sur Entrée pour commencer la course...")
    print("GO!")

url = 'XXXXXXXX'# put url here
cv2.namedWindow("Course")

# Signal de depart
attendre_signal_depart()

temps_debut = time.time()
while voitures_en_course:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgnp, -1)
    dominant_color = detect_color(frame)
    
    current_time = time.time()
    if dominant_color in voitures_en_course:
        if dominant_color not in last_detection_time or (current_time - last_detection_time[dominant_color]) > 5:
            tours_completes[dominant_color] += 1
            lap_time = round(current_time - temps_debut, 2)
            temps_par_voiture[dominant_color].append(lap_time)
            last_detection_time[dominant_color] = current_time  # change le temps de detour à l'actuelle
            print(f"La voiture {dominant_color} a franchi la ligne d'arrivée en {lap_time} secondes!")
            afficher_classement()
            
            if tours_completes[dominant_color] >= TOURS_A_FAIRE:
                voitures_en_course.remove(dominant_color)
                finish_times[dominant_color] = lap_time  # Enregistres les temps de completions puis les associe au couleur des voitures
    
    cv2.imshow("Course", frame)
    if cv2.waitKey(5) == ord('q'):
        break

cv2.destroyAllWindows()
print("\nCourse terminée!")
classement_final = sorted(finish_times.items(), key=lambda x: x[1])  # Arrange les voitures en ordre
print("\nClassement final:")
for i, (voiture, finish_time) in enumerate(classement_final, 1):
    print(f"{i}. Voiture {voiture} - 10 tours complétés - Temps total: {finish_time} secondes")
print(f"\nLe gagnant est la voiture {classement_final[0][0]}!")
