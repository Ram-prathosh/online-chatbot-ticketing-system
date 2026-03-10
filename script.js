function sendMessage(){

let msg = document.getElementById("message").value;

fetch("/send",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:msg})
})
.then(res=>res.json())
.then(data=>{

let chatbox = document.getElementById("chatbox");

chatbox.innerHTML += "<p><b>You:</b> "+msg+"</p>";
chatbox.innerHTML += "<p><b>Bot:</b> "+data.reply+"</p>";

document.getElementById("message").value="";
});

}