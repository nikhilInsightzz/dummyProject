/*
E18-D80NK Infrared Distance Ranging Sensor
*/
int proxpin=A1;
int DELAY = 100;
int buttonState = 0;         // variable for reading the pushbutton status
int pin1 = 1;

void setup() {
  Serial.begin(9600); //Start serial communication boud rate at 9600
  pinMode(proxpin,INPUT_PULLUP);
 digitalWrite(pin1, OUTPUT); //Pin 5 as signal input
 digitalWrite(pin1, LOW);
}
void loop() {
  buttonState = digitalRead(proxpin);
  //delay(DELAY);
  if(buttonState == 1){
    digitalWrite(pin1, HIGH);
    Serial.println(buttonState);
  }
  else if(buttonState == 0){
    digitalWrite(pin1, LOW);
  }
}
