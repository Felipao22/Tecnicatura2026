//Ejercicios para encontrar número pares e impares
let parImpar = 1;
if (parImpar % 2 == 0) {
    console.log("Es un número PAR");
} else {
    console.log("Es un númnero IMPAR")
}

//Ejercicio es mayor de edad
let edad = 18, adulto = 18;
if (edad >= adulto) {
    console.log("Es una persona adulta")
} else {
    console.log("Usted es una persona menor de edad")
}

//Ejercicio: dentro de un rango

let dentroRango = 10; //Aqui vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if (dentroRango >= valMin && dentroRango <= valMax) {
    console.log("Está dentro del rango establecido")
} else {
    console.log("No está dentro del rango establecido")

}

//Ejercicio: si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = false;
if (vacaciones || diaDescanso) {
    console.log("El padre asistir al juego de su hijo")
} else {
    console.log("El padre no puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2);
let numero = 12;
resultado2 = numero % 2 === 0 ? "Es un número PAR" : "Es un número IMPAR";

//Convertir String a Number
let miNumero = "21";//Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero)//Esta es una función
console.log(edad2);
//Funcion isNaN
if (isNaN(edad2)) { //No es número = is Not a Number(devuelve un resultado booleano)
    console.log("La variable no contiene solo números")
} else {
    if (edad2 >= 18) {
        console.log("Puede votar");
    } else {
        console.log("Muy joven para votar");
    }

}


let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar"
console.log(resultado3)