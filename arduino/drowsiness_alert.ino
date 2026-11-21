
// ==========================================
// DRIVER DROWSINESS DETECTION SYSTEM
// ARDUINO UNO
// ==========================================

// Broches des composants

const int buzzerPin = 8;

const int ledR = 9;
const int ledG = 10;
const int ledB = 11;

const int moteurPin = 4;


// Configuration du moteur
#define MOTEUR_ON LOW
#define MOTEUR_OFF HIGH


// Variables du systeme

bool alert = false;

unsigned long alertStartTime = 0;


// ==========================================
// SETUP
// ==========================================

void setup() {

    pinMode(buzzerPin, OUTPUT);

    pinMode(ledR, OUTPUT);
    pinMode(ledG, OUTPUT);
    pinMode(ledB, OUTPUT);

    pinMode(moteurPin, OUTPUT);

    Serial.begin(9600);

    // Etat initial : VERT
    setColor(0, 255, 0);

    digitalWrite(buzzerPin, LOW);

    // Moteur en marche
    digitalWrite(moteurPin, MOTEUR_ON);

}


// ==========================================
// BOUCLE PRINCIPALE
// ==========================================

void loop() {

    // Reception des commandes Python

    if (Serial.available() > 0) {

        char cmd = Serial.read();

        // Somnolence detectee
        if (cmd == 'O') {

            if (!alert) {

                alert = true;

                alertStartTime = millis();

            }

        }

        // Yeux ouverts
        else if (cmd == 'N') {

            alert = false;

        }

    }


    // ======================================
    // GESTION DES ALERTES
    // ======================================

    if (alert) {

        unsigned long elapsed = millis() - alertStartTime;


        // PHASE 1 : ORANGE (0 a 3 secondes)

        if (elapsed < 3000) {

            setColor(255, 128, 0);

            // Moteur en marche
            digitalWrite(moteurPin, MOTEUR_ON);

            // Buzzer intermittent
            if ((elapsed / 500) % 2 == 0) {

                digitalWrite(buzzerPin, HIGH);

            }

            else {

                digitalWrite(buzzerPin, LOW);

            }

        }


        // PHASE 2 : ROUGE (apres 3 secondes)

        else {

            setColor(255, 0, 0);

            // Buzzer actif
            digitalWrite(buzzerPin, HIGH);

            // Arret du moteur
            digitalWrite(moteurPin, MOTEUR_OFF);

        }

    }


    // ======================================
    // ETAT NORMAL : VERT
    // ======================================

    else {

        setColor(0, 255, 0);

        digitalWrite(buzzerPin, LOW);

        digitalWrite(moteurPin, MOTEUR_ON);

    }

}


// ==========================================
// FONCTION LED RGB
// ==========================================

void setColor(int r, int g, int b) {

    analogWrite(ledR, r);

    analogWrite(ledG, g);

    analogWrite(ledB, b);

}
