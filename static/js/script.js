const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let isDrawing = false;
let lastX = 0;
let lastY = 0;
let lineWidth = 1;
const saveButton = document.getElementById('save-canvas');
canvas.addEventListener('mousedown', (event) => {
    if (event.button === 0) { // Solo el botón izquierdo del mouse
        isDrawing = true;
        const {x, y} = getMousePos(event);
        lastX = x;
        lastY = y;
        ctx.beginPath(); // Comienza un nuevo trazo al iniciar el dibujo
        ctx.moveTo(lastX, lastY); // Mueve la "pluma" a la posición inicial
    }
});

canvas.addEventListener('mouseup', () => {
    if (isDrawing) {
        isDrawing = false;
        ctx.beginPath(); // Resetea el path para evitar líneas no deseadas
    }
});

canvas.addEventListener('mousemove', (event) => {
    if (!isDrawing) return;

    const {x, y} = getMousePos(event);
    ctx.lineWidth = lineWidth;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';

    ctx.lineTo(x, y);
    ctx.stroke();
    lastX = x;
    lastY = y;
});

function getMousePos(event) {
    const rect = canvas.getBoundingClientRect();
    return {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top
    };
}

// Redimensiona el canvas cuando cambia el tamaño de la ventana
window.addEventListener('resize', resizeCanvas);
resizeCanvas(); // Llamada inicial para configurar el tamaño del canvas

function resizeCanvas() {
    const ratio = window.devicePixelRatio || 1;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;

    canvas.width = width * ratio;
    canvas.height = height * ratio;
    ctx.scale(ratio, ratio);
}

const clearButton = document.getElementById('clear-canvas');
clearButton.addEventListener('click', function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});


window.addEventListener('resize', resizeCanvas);
resizeCanvas();

function saveCanvasAsSVG() {
    const svg = canvasToSVG(canvas);
    const svgBlob = new Blob([svg], {type: 'image/svg+xml;charset=utf-8'});
    const url = URL.createObjectURL(svgBlob);

    // Create a temporary link element
    const link = document.createElement('a');
    link.href = url;
    link.download = 'canvas-image.svg'; // The default filename

    // Append the link to the body
    document.body.appendChild(link);

    // Programmatically click the link to trigger the download
    link.click();

    // Remove the link from the document
    document.body.removeChild(link);
    URL.revokeObjectURL(url); // Clean up the URL object
}

function canvasToSVG(canvas) {
    // Get the canvas content as SVG
    const svgHeader = `<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="${canvas.width}" height="${canvas.height}" viewBox="0 0 ${canvas.width} ${canvas.height}">\n`;
    const svgFooter = `</svg>`;
    const canvasContent = canvas.toDataURL('image/png').replace(/^data:image\/png;base64,/, '');

    // Create an SVG element with canvas content
    return svgHeader + `<image href="data:image/png;base64,${canvasContent}" x="0" y="0" width="${canvas.width}" height="${canvas.height}"/>` + svgFooter;
}

saveButton.addEventListener('click', saveCanvasAsSVG);