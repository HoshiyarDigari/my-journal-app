
// show tracing Area when tile is clicked

function letterTracing(letter=A, show=true){
    if(show){
        document.getElementById('letterTiles').style.display='none';
        document.getElementById('tracingArea').style.display='block';
        // call drawing function
        drawLetter(letter);
    }
    else {
        document.getElementById('letterTiles').style.display='block';
        document.getElementById('tracingArea').style.display='none';
    }
    
    
}

// store the value of current letter drawn on the canvas so we can enable tracing for the letter
let currentLetter='';
// draw letters on the canvas

function drawLetter(letter) {
    
    const canvas = document.getElementById('myCanvas');
    const ctx = canvas.getContext('2d')
    currentLetter = letter;
    //canvas_width = canvas.
    ctx.font = '350px HindiFont';
    // clear the canvas 
    ctx.clearRect(0,0,500,500);
    // draw the letter
    ctx.fillText(`${letter}`, 100, 350);
    setupTracing(letter);

}


// setup tracing of the letters
let isTracing = false; // Tracks whether the user is tracing

function setupTracing(letter) {
    const canvas = document.getElementById('myCanvas');
    const ctx = canvas.getContext('2d');

    canvas.addEventListener('mousedown', () => {
        isTracing = true;
        ctx.beginPath(); // Start a new path
    });

    canvas.addEventListener('mouseup', () => {
        isTracing = false;
        ctx.beginPath(); // Reset path
    });

    canvas.addEventListener('mousemove', (event) => {
        if (!isTracing) return;

        // Extract position relative to canvas
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        // Start tracing with a green line
        ctx.lineWidth = 15;
        ctx.strokeStyle = 'white';
        ctx.lineCap = 'round';

        ctx.lineTo(x, y);
        ctx.stroke();
        ctx.beginPath(); // Reset for the next segment
        ctx.moveTo(x, y);
    });
}
