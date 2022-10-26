function negyzetszam(m) {
    let i = 1;
    let osszeg = 1;
    while (osszeg < m) {
        i = i + 2;
        osszeg = osszeg +i;
    }
    if (osszeg == m) {
        return "igen";
    }
    else{
        return  "nem";
    }
}
function check() {
    let x = Number(document.forms["urlap"]["beszam"].value);
    if (x % 2 == 0) {
        document.getElementById("paritas").innerHTML="páros";
    }
    else{
        document.getElementById("paritas").innerHTML="páratlan";
    }
    document.getElementById("negyzet").innerHTML=negyzetszam(x);
    document.getElementById("szamosszeg").innerHTML=szamjegyekosszege(x);

}

function szamjegyekosszege(n) {
    let osszeg = 0;
    while (n > 0) {
        osszeg += n % 10;
        n = Math.floor(n/10);
    }
    return osszeg;
}