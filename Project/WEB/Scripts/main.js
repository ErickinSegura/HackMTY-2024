// URL base de la API
const apiUrl = 'https://redesigned-space-succotash-v9wv45jjqxw3pvpv-5000.app.github.dev/';

// Función para cargar los productos en el dropdown
async function loadProducts() {
    try {
        const response = await fetch(`${apiUrl}products`);
        if (!response.ok) {
            throw new Error('Error al obtener los productos');
        }
        const products = await response.json();
        const selectElement = document.getElementById('productSelect');
        selectElement.innerHTML = '<option value="">Selecciona un producto</option>';
        products.forEach(product => {
            const option = document.createElement('option');
            option.value = product;
            option.textContent = product;
            selectElement.appendChild(option);
        });
    } catch (error) {
        console.error('Error:', error);
        alert('No se pudieron cargar los productos. Por favor, intenta de nuevo más tarde.');
    }
}

// Función para mostrar la pantalla de carga
function showLoadingScreen() {
    document.getElementById('loadingScreen').classList.remove('d-none');
}

// Función para ocultar la pantalla de carga
function hideLoadingScreen() {
    document.getElementById('loadingScreen').classList.add('d-none');
}

// Función para enviar un comentario y categorizarlo
async function submitComment(event) {
    event.preventDefault(); // Evitar que el formulario recargue la página

    const product = document.getElementById('productSelect').value;
    const opinion = document.getElementById('reviewText').value;

    if (!product || !opinion) {
        alert('Por favor, selecciona un producto y escribe un comentario.');
        return;
    }

    // Mostrar pantalla de carga
    showLoadingScreen();

    try {
        const response = await fetch(`${apiUrl}opinion`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ product, opinion }),
        });

        if (!response.ok) {
            throw new Error('Error al enviar el comentario');
        }

        const result = await response.json();
        if (result.status === 'success') {
            alert('Comentario enviado y categorizado con éxito');
            document.getElementById('reviewText').value = '';
        } else {
            throw new Error(result.message || 'Error desconocido al procesar el comentario');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('No se pudo enviar o categorizar el comentario. Por favor, intenta de nuevo más tarde.');
    } finally {
        // Ocultar pantalla de carga
        hideLoadingScreen();
    }
}

// Evento que se ejecuta cuando el DOM está completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    loadProducts();
    document.getElementById('reviewForm').addEventListener('submit', submitComment);
});
