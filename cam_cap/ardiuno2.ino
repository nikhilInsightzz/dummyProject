/*
E18-D80NK Infrared Distance Ranging Sensor
*/
int proxpin=A1;
int DELAY = 10;
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  Serial.begin(9600); //Start serial communication boud rate at 9600
  pinMode(proxpin,INPUT_PULLUP); //Pin 5 as signal input
}
void loop() {
  buttonState = digitalRead(proxpin);
  Serial.println(buttonState);
  delay(DELAY);
}
