// TIpos de datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es idéntica
*/

var nombre = 'Felipe'; //Tipo str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero = 3000; //Tipo number
console.log(numero);

//Tipo objeto
var objeto = {
  nombre: 'Felipe',
  apellido: 'Aviani',
  telefono: '123456789',
};

console.log(typeof objeto);

//Tipo de dato booleano
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion() {}
console.log(typeof miFuncion);

//Tipo de dato Symbol
var simbolo = Symbol('Mi simbolo');
console.log(typeof simbolo);

//Tipo de dato clase
class Persona {
  constructor(nombre, apellido) {
    this.nombre = nombre;
    this.apellido = apellido;
  }
}

console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(x);

x = undefined;
console.log(typeof x);

//null: ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Citroen', 'Peugeot', 'Renault'];
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de dato es

var z = '';
console.log(z); //Esto se refiere a una cadena vacía
console.log(typeof z);
