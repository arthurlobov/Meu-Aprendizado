//
//  ContentView.swift
//  desafio_1
//
//  Created by Turma01-2 on 23/10/25.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    @State private var temp: Double = 0
    @State private var distancia: Double = 0
    @State private var velocidade: Double = 0
    var body: some View {
        VStack{
            VStack{
                Text("Digite a distancia(Km): ")
                TextField("Number: ", value: $distancia,format: .number )
                    .keyboardType(.decimalPad)
                    .textContentType(.oneTimeCode)
                    .padding()
                    .background(Color.gray.opacity(0.2))
                    .cornerRadius(10)
                    .background(.white)
                    .multilineTextAlignment(.center)
                    .frame(width: 300, height: 50)
                    .background(Color.white)
                    .cornerRadius(10)
                Text("Digite o tempo (h): ")
                TextField("Number: ", value: $temp,format: .number )
                    .keyboardType(.decimalPad)
                    .textContentType(.oneTimeCode)
                    .padding()
                    .background(Color.gray.opacity(0.2))
                    .cornerRadius(10)
                    .background(.white)
                    .multilineTextAlignment(.center)
                    .frame(width: 300, height: 50)
                    .background(Color.white)
                    .cornerRadius(10)
                Button("Calcular") {
                    velocidade = distancia/temp
                    print(velocidade)
                }
                .font(.headline)
                .fontWeight(.semibold)
                .padding()
                .background(.black)
                .foregroundColor(.white)
                .frame(width: 200, height: 50)
                .cornerRadius(15)
                
                Text(String(format: "%.2f Km/h", velocidade))
                if (velocidade == 0){
                    Image("interrogacao")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 400, height: 300)
                    .background(.green)
                    .clipShape(Circle())
                }
                else if (velocidade < 10 && velocidade > 0){
                    Image("interrogacao")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 400, height: 300)
                    .background(.green)
                    .clipShape(Circle())
                }
                else if (velocidade >= 10 && velocidade < 30){
                    Image("tartaruga")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 400, height: 300)
                    .background(.green)
                    .clipShape(Circle())                }
                else if (velocidade >= 30 && velocidade < 70){
                    Image("interrogacao")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 400, height: 300)
                    .background(.green)
                    .clipShape(Circle())                }
                else if (velocidade >= 70 && velocidade < 90){
                    Image("interrogacao")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 400, height: 300)
                    .background(.green)
                    .clipShape(Circle())
                }
                else if (velocidade >= 90 && velocidade <= 130){
                    Image("interrogacao")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 400, height: 300)
                    .background(.green)
                    .clipShape(Circle())
                }
            }
            VStack{
                HStack{
                    Text("Tartaruga")
                        .frame(width: 100)
                    Text("(0-9.9 km/h)")
                        .frame(width: 150)
                    Circle()
                        .frame(width: 50, height: 15)
                    
                }
                HStack{
                    Text("Elefante")
                        .frame(width: 100)
                    Text("(10-29.9 km/h)")
                        .frame(width: 150)
                    Circle()
                        .frame(width: 50, height: 15)
                }
                HStack{
                    Text("Avestruz")
                        .frame(width: 100)
                    Text("(30-69.9 km/h)")
                        .frame(width: 150)
                    Circle()
                        .frame(width: 50, height: 15)
                }
                HStack{
                    Text("Leão")
                        .frame(width: 100)
                    Text("(70-89.9 km/h)")
                        .frame(width: 150)
                    Circle()
                        .frame(width: 50, height: 15)
                }
                HStack{
                    Text("Guepardo")
                        .frame(width: 100)
                    Text("(90-130 km/h)")
                        .frame(width: 150)
                    Circle()
                        .frame(width: 50, height: 15)
                }
                .frame(width: 300)
            }
            .multilineTextAlignment(.center)
            .frame(width: 300, height: 150)
            .background(Color.white)
            .cornerRadius(10)
            
        }     
        .frame(maxWidth: /*@START_MENU_TOKEN@*/.infinity/*@END_MENU_TOKEN@*/,maxHeight: .infinity)
        .background(.gray)

    }
}


#Preview {
    ContentView()
}
