document.getElementById('recordButton').addEventListener('click', function() {  
    // Here you would add the code to record the voice input  
    // This typically involves using the Web Audio API and might look something like this:  
  
    navigator.mediaDevices.getUserMedia({ audio: true })  
        .then(function(stream) {  
            var mediaRecorder = new MediaRecorder(stream);  
            mediaRecorder.start();  
  
            var audioChunks = [];  
            mediaRecorder.addEventListener("dataavailable", function(event) {  
                audioChunks.push(event.data);  
            });  
  
            mediaRecorder.addEventListener("stop", function() {  
                var audioBlob = new Blob(audioChunks);  
                var audioUrl = URL.createObjectURL(audioBlob);  
                var audio = new Audio(audioUrl);  
                audio.play();  
            });  
  
            setTimeout(function() {  
                mediaRecorder.stop();  
            }, 3000);  
        });  
});  
