void setup() {
  // シリアル通信を開始する
  Serial.begin(9600);
  // LEDを制御するピンを出力モードに設定する
  pinMode(13, OUTPUT);
} 

void loop() {
  // センサーから値を読み取る
  int val = analogRead(1);
  // センサーの値をシリアルモニターに出力する
  Serial.println(val);
 

  // センサーの値が150を超えた場合、LEDを点灯させる
  if (val > 150) {
    digitalWrite(13, HIGH); // LEDを点灯させる
  } else {
    digitalWrite(13, LOW); // LEDを消灯させる
  }
}

