var i = 0;
var txt = `I am Muhammed Büyükkınacı. I was born in Mersin in 1994. I am ${new Date().getFullYear() - 1994} years old.
I am a Data Scientist and Industrial Engineer. I am trying to engineer a better world using AI.  If you want to contact with me, you are at the right place.`;
var speed = 40;

function typeWriter() {
    if (i < txt.length) {
        document.getElementById("whoami").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

typeWriter();
