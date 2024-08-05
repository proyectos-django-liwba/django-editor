function downloadSVG() {
    // Seleccionar el SVG que deseas descargar
    const svgElement = document.getElementById('drawing-svg');

    if (svgElement) {
        // Convertir el SVG a una cadena de texto
        const svgData = new XMLSerializer().serializeToString(svgElement);

        // Crear un enlace de descarga
        const link = document.createElement('a');
        link.href = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgData);
        // Nombre del archivo descargado
        link.download = 'drawing.svg';

        // Simular clic en el enlace para iniciar la descarga
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    } else {
        console.error('No se encontró el SVG para descargar.');
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const downloadButton = document.getElementById('save-svg');

    if (downloadButton) {
        downloadButton.addEventListener('click', downloadSVG);
    } else {
        console.error('No se encontró el botón para descargar el SVG.');
    }
});


document.addEventListener('DOMContentLoaded', function () {
    const loading = document.getElementById('loading');
    addEventListener('py:ready', () => loading.close());
    loading.showModal();
});


// document.addEventListener('DOMContentLoaded', function () {
//     //const element = document.getElementById('app');
//     const element = document.getElementById('drawing-svg');
//
//
//     if(element){
//         alert("hola")
//     }
// });

document.addEventListener('DOMContentLoaded', function () {
    const targetNode = document.body; // Observar cambios en todo el body
    const config = {childList: true, subtree: true}; // Configuración para observar todos los cambios en los hijos y subárboles

    const callback = function (mutationsList, observer) {
        for (let mutation of mutationsList) {
            if (mutation.type === 'childList') {
                // Verificar si el elemento deseado está presente
                const element = document.getElementById('drawing-svg');
                if (element) {
                    alert("Hola");
                    observer.disconnect(); // Dejar de observar después de encontrar el elemento
                    break;
                }
            }
        }
    };

    const observer = new MutationObserver(callback);
    observer.observe(targetNode, config);
});


const element = document.getElementById('drawing-svg');
if (element) {
    alert("Hola");
}