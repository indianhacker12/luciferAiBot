let btn=document.querySelector("#btn")
let content=document.querySelector("#content")
let voice=document.querySelector("#voice")

function speak(text){
    let text_speak=new SpeechSynthesisUtterance(text)
    text_speak.rate=1
    text_speak.pitch=1
    text_speak.volume=1
    text_speak.lang="hi-IN"
    window.speechSynthesis.speak(text_speak)
}

function wishMe(){
    let day=new Date()
    let hours=day.getHours()
    if(hours>=0 && hours<12){
        speak("Good Morning Sir")
    }
    else if(hours>=12 && hours <17){
        speak("Good afternoon Sir")
    }else{
        speak("Good Night Sir")
    }
}
window.addEventListener('load',()=>{
   wishMe()
 })
let speechRecognition= window.SpeechRecognition || window.webkitSpeechRecognition 
let recognition =new speechRecognition()
recognition.onresult=(event)=>{
    let currentIndex=event.resultIndex
    let transcript=event.results[currentIndex][0].transcript
    content.innerText=transcript
   takeCommand(transcript.toLowerCase())
}

btn.addEventListener("click",()=>{
    recognition.start()
    voice.style.display="block"
    btn.style.display="none"
})
function takeCommand(message){
   voice.style.display="none"
    btn.style.display="flex"
    if(message.includes("hello")){
        speak("hello sir,what can i help you?")
    }
    else if(message.includes("who are you")){
        speak("i am Lucifer your virtual assistant ,created by Yaswant Pandey")
    }else if(message.includes("open youtube")){
        speak("opening youtube...")
        window.open("https://youtube.com/","_blank")
    }
    else if(message.includes("open google")){
        speak("opening google...")
        window.open("https://google.com/","_blank")
    }
    else if(message.includes("open facebook")){
        speak("opening facebook...")
        window.open("https://facebook.com/","_blank")
    }
    else if(message.includes("open instagram")){
        speak("opening instagram...")
        window.open("https://instagram.com/","_blank")
    }
    else if(message.includes("open calculator")){
        speak("opening calculator..")
        window.open("calculator://")
    }
    else if (message.includes("open camera")) {
        speak("Opening camera...");

        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                const video = document.createElement('video');
                video.srcObject = stream;
                video.play();
                document.body.appendChild(video);
            })
            .catch(function(err) {
                // Handle any errors, such as camera access being denied
                speak("Sorry, there was an error accessing the camera: " + err.message);
            });
    }
    else if(message.includes("open whatsapp")){
        speak("opening whatsapp..")
        window.open("whatsapp://")
    }
    else if(message.includes("open vs code")){
        speak("opening whatsapp..")
        window.open("vscode://")
    }
    else if(message.includes("time")){
      let time=new Date().toLocaleString(undefined,{hour:"numeric",minute:"numeric"})
      speak(time)
    }
    else if(message.includes("date")){
        let date=new Date().toLocaleString(undefined,{day:"numeric",month:"short"})
        speak(date)
      }
    else{
        let finalText="I found this on internet" + message.replace("Lucifer","") || message.replace("Lucifer","")
        speak(finalText)
        window.open(`https://www.google.com/search?q=${message.replace("Lucifer","")}`,"_blank")
    }
}