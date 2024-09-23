int hearts = 10;

void setup() {
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  start();
}

void loop() {
  if (Serial.available() > 0){
    String msg = Serial.readString();
    int new_hearts = msg.toInt();
    while (new_hearts == -1){
      new_hearts = msg.toInt();
    }
    if (new_hearts > hearts){ //INCREASE
      for(int i = hearts; i <= new_hearts; i+=1){
        digitalWrite(i+1, HIGH);
        delay(100);
      }
    }
    else{ //DECREASE
      for(int i = hearts; i > new_hearts; i-=1){
        digitalWrite(i+1, LOW);
        delay(100);
      }
    }
    hearts = new_hearts;
  }   
}

void start(){
  for (int pinValue = 1; pinValue <= 10; pinValue += 1) {
    digitalWrite(pinValue+1, HIGH);
    delay(250);
  }
}