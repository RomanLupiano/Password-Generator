var lenght_elem = document.getElementById("lenght");
var password_elem = document.getElementById("password");
var alert_elem = document.getElementById("alert");
var upper, special, numbers;

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

function generatePw() {
    if (lenght_elem.value > 100000 || lenght_elem.value < 1) { 
        alert_elem.innerText = "Por favor ingresa un valor entre 1 y 100000."
        return;
    } else{
        alert_elem.innerText = ""
    }

    let letters = "abcdefghijklmnñopqrstuvwxyz"
    if (upper) { letters += "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"}
    if (special) { letters += "!#$/%&'()*+,-./:;<=>?@[\]^_`{|}~"}
    if (numbers) { letters += "1234567890"}
    
    let pswd = ""

    for (let index = 0; index < lenght_elem.value; index++) {
        pswd += letters[getRandomInt(letters.length)]
    }

    password_elem.innerText = pswd
}


function clip_text(a_string){
    var input = document.createElement('input')
    input.id="__copyText__";
    input.value = a_string;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    var txt = input.value
    input.remove()
}
function clip_div(divId){
   return clip_text(document.getElementById(divId).innerText)
}