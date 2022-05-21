/*
Stack overflow source:
https://stackoverflow.com/questions/34101183/how-do-i-stop-a-sound-when-a-key-is-released-in-javascript
*/


var NOTES = [
    {key: 'KeyA', sound: playNote('Strings/string_2.wav')},
    {key: 'KeyB', sound: playNote('Strings/string_3.wav')},
    {key: 'KeyC', sound: playNote('Strings/string_4.wav')},
    {key: 'KeyD', sound: playNote('Strings/string_5.wav')},
    {key: 'KeyE', sound: playNote('Drums/Melodic/melodic_5.wav')},
    {key: 'KeyF', sound: playNote('Drums/Melodic/melodic_6.wav')},
    {key: 'KeyG', sound: playNote('Drums/Melodic/melodic_3.wav')},
    {key: 'KeyH', sound: playNote('Drums/Melodic/melodic_7.wav')}
];

var DELAY = 0;

function playNote(file) {
    var audio = new Audio(file);

    comp_output = "<html>\n<body>\n<button style='" + "width: 300px; height: 300px;'"+"onclick="+"play();"+">PLAY</button>\n<script>\nfunction play() {\n"
    return { 
        start: function() {
            audio.play();
        },
        stop: function() {
            audio.pause();
            console.log(audio.currentTime);
        },
        print: function() {
            document.getElementById("compBox").value = comp_output += 
            "\nsetTimeout(function() {\nvar audio = new Audio('" + file + "');\naudio.play();\n" + 
            "setTimeout(function() { audio.pause(); }, " + audio.currentTime * 10000 + ", audio);\n}, " + 1000 * DELAY + ");\n"

            document.getElementById("compBox").value = comp_output + "}\n<\/script>\n\</body>\n</html>";
            audio.currentTime = 0;
            DELAY++;
        }
    };
}

function soundOn() {
    NOTES.forEach(function(note) {
        if(event.code == note.key) {
            note.sound.start();
            
        }
    });
}   

function soundOff() {
    NOTES.forEach(function(note) {
        if(event.code == note.key) {
            note.sound.stop();
            note.sound.print();
        }
    });
}


function beat_pad() { 

    comp_output = "<html>\n<body>\n<script>"

    var btnA_click = document.getElementById('btnA');
    var btnB_click = document.getElementById('btnB');
    var btnC_click = document.getElementById('btnC');
    var btnD_click = document.getElementById('btnD');
    var btnE_click = document.getElementById('btnE');
    var btnF_click = document.getElementById('btnF');
    var btnG_click = document.getElementById('btnG');
    var btnH_click = document.getElementById('btnH');

    
    btnA_click.addEventListener("click", function() {   
        document.getElementById("compBox").value = comp_output += "\nnew Audio('Strings/string_2.wav').play();\n";
        document.getElementById("compBox").value = comp_output + "<\/script>\n\</body>\n</html>";            
        new Audio('Strings/string_2.wav').play();
    });
    btnB_click.addEventListener("click", function() {
        document.getElementById("compBox").value = comp_output += "\nnew Audio('Strings/string_3.wav').play();\n";
        document.getElementById("compBox").value = comp_output + "<\/script>\n\</body>\n</html>";             
        new Audio('Strings/string_3.wav').play();
    });
    btnC_click.addEventListener("click", function() {
        document.getElementById("compBox").value = comp_output += "\nnew Audio('Strings/string_4.wav').play();\n";
        document.getElementById("compBox").value = comp_output + "<\/script>\n\</body>\n</html>";            
        new Audio('Strings/string_4.wav').play();
    });
    btnD_click.addEventListener("click", function() {
        document.getElementById("compBox").value = comp_output += "\nnew Audio('Strings/string_5.wav').play();\n";
        document.getElementById("compBox").value = comp_output + "<\/script>\n\</body>\n</html>";               
        new Audio('Strings/string_5.wav').play();
    });
    btnE_click.addEventListener("click", function() {
        document.getElementById("compBox").value = comp_output += "\nnew Audio('Drums/Melodic/melodic_5.wav').play();\n";
        document.getElementById("compBox").value = comp_output + "<\/script>\n\</body>\n</html>";              
        new Audio('Drums/Melodic/melodic_5.wav').play();
    });
    btnF_click.addEventListener("click", function() {
        document.getElementById("compBox").value = comp_output += "\nnew Audio('Drums/Melodic/melodic_6.wav').play();\n";
        document.getElementById("compBox").value = comp_output + "<\/script>\n\</body>\n</html>";
        new Audio('Drums/Melodic/melodic_6.wav').play();
    });
    btnG_click.addEventListener("click", function() {
        document.getElementById("compBox").value = comp_output += "\nnew Audio('Drums/Melodic/melodic_3.wav').play();\n";
        document.getElementById("compBox").value = comp_output + "<\/script>\n\</body>\n</html>";            
        new Audio('Drums/Melodic/melodic_3.wav').play();
    });
    btnH_click.addEventListener("click", function() {
        document.getElementById("compBox").value = comp_output += "\nnew Audio('Drums/Melodic/melodic_7.wav').play();\n";
        document.getElementById("compBox").value = comp_output + "<\/script>\n\</body>\n</html>";              
        new Audio('Drums/Melodic/melodic_7.wav').play();
    });
    return;
}

function play_music() {
    music = document.getElementById("textBox").value;
    console.log(music);
    lines = music.split(/\r?\n/);
    console.log(lines);

    comp_output = "<html>\n<body>\n<button style='"+"width: 300px; height: 300px;'"+"onclick="+"play();"+">PLAY</button>\n<script>\nfunction play() {\n"
    line_timeout = 0;
    for(i = 0; i < lines.length; ++i){
        line_timeout = line_timeout + (i * 700)
        if(lines[i][0] == 'A') {
            comp_output += "\nsetTimeout(function () {new Audio('Drums/Melodic/melodic_1.wav').play();}, " +  line_timeout + ");\n";
            setTimeout( function () {
                new Audio('Drums/Melodic/melodic_1.wav').play();
            }, line_timeout);
        }
        if(lines[i][1] == 'B') {
            comp_output += "\nsetTimeout(function () {new Audio('Drums/Melodic/melodic_2.wav').play();}, " +  line_timeout + ");\n";
            setTimeout( function () {
                new Audio('Drums/Melodic/melodic_2.wav').play();  
            }, line_timeout);
        }
        if(lines[i][2] == 'C') {
            comp_output += "\nsetTimeout(function () {new Audio('Drums/Melodic/melodic_3.wav').play();}, " + line_timeout + ");\n";
            setTimeout( function () {
                new Audio('Drums/Melodic/melodic_3.wav').play();      
            }, line_timeout);
        }
        if(lines[i][3] == 'D') {
            comp_output += "\nsetTimeout(function () {new Audio('Drums/Melodic/melodic_4.wav').play();}, " +  line_timeout +");\n";
            setTimeout( function () {
                new Audio('Drums/Melodic/melodic_4.wav').play();
            }, line_timeout);
        }
        console.log(lines[i]);
        document.getElementById("compBox").value = comp_output + "}\n<\/script>\n\</body>\n</html>";
    }
    return;
}