#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h" 

// 1. Configurações de WiFi e API
const char* ssid = "Wifi";
const char* password = "Senha";
const char* serverUrl = "http://0.0.0.0:5000/api/leitura";

// 2. Configuração dos Sensores e Atuadores
#define ledPin 2
#define DHTPIN 4     
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
  dht.begin();
  
  // Conecta ao Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi!");
  digitalWrite(ledPin, HIGH);

}

void loop() {
  // Lê as informações do sensor
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  String local = "Sala de Maquinas";
  
  // Verifica se a leitura foi bem-sucedida
  if (isnan(h) || isnan(t)) {
    Serial.println("Falha ao ler o sensor DHT!");
    delay(5000);
    return;
  }
  
  // Converte as leituras para o formato JSON
  String jsonPayload = "{";
  jsonPayload += "\"Setor\": \"" + local + "\",";   // usa a variável local
  jsonPayload += "\"umidade\": " + String(h, 2) + ",";
  jsonPayload += "\"temperatura\": " + String(t, 2);
  jsonPayload += "}";

  // Envia a requisição HTTP POST
  HTTPClient http;
  http.begin(serverUrl);
  http.addHeader("Content-Type", "application/json");

  int httpResponseCode = http.POST(jsonPayload);
  
  if (httpResponseCode > 0) {
    Serial.print("Código de Resposta HTTP: ");
    Serial.println(httpResponseCode);
    String response = http.getString();
    Serial.println(response);
    for (int i=0; i<5;i++){
        digitalWrite(ledPin, LOW);
        delay(300);
        digitalWrite(ledPin, HIGH);
        delay(300);
    }      
      
  } else {
    Serial.print("Erro no envio HTTP. Código: ");
    Serial.println(httpResponseCode);
  }
  
  http.end(); // Fecha a conexão
  
  // Espera 60 segundos antes da próxima leitura
  delay(60000); 
}