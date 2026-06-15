var nombre = "Felipe";
var apellido = " Aviani";
var nombreCompleto = nombre + " " + apellido; //Primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = "Felipe" + " " + "Aviani"; //Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17; //Aqui se puede diferencia a través de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //Concatenamos usando el operador simplificado
console.log(nombre);