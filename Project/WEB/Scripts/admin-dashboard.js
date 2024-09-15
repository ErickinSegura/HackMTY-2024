const apiUrl = 'https://redesigned-space-succotash-v9wv45jjqxw3pvpv-5000.app.github.dev/';

function toggleLoadingScreen(show) {
    const loadingScreen = $('#loadingScreen');
    if (show) {
        loadingScreen.fadeIn(300);
    } else {
        loadingScreen.fadeOut(300);
    }
}

async function loadProducts() {
    try {
        const response = await fetch(apiUrl + 'products');
        if (!response.ok) {
            throw new Error('Error en la solicitud de productos');
        }

        const data = await response.json();
        const productSelect = $('#productSelect');
        
        productSelect.empty();
        productSelect.append('<option value="">Realizar consulta</option>');

        data.forEach(product => {
            productSelect.append(`<option value="${product}">${product}</option>`);
        });
    } catch (error) {
        console.error('Error:', error);
        alert('Error al cargar los productos. Por favor, intenta de nuevo más tarde.');
    }
}

async function fetchProductData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`Error fetching data from ${url}:`, error);
        throw error;
    }
}

async function updateProductInfo(product) {
    try {
        // Show loading screen
        toggleLoadingScreen(true);

        // Limpiar información anterior
        $('#goodComments, #badComments, #ratings').empty();
        $('#commentSummary').text('');

        // Actualizar nombre del producto
        $('#productName').text(product);

        // Fetch y actualizar imagen del producto
        try {
            const imgUrl = await fetchProductData(`${apiUrl}img/${product}`);
            $('#productImage').attr('src', imgUrl);
        } catch (error) {
            $('#productImage').attr('src', 'https://default-image-url.com/default.jpg'); // URL de una imagen por defecto
            console.error('Error al cargar la imagen del producto:', error);
        }

        // Fetch y actualizar buenos comentarios
        try {
            const goodComments = await fetchProductData(`${apiUrl}best_comments/${product}`);
            $('#goodComments').html(goodComments.map(comment => `<li>${comment}</li>`).join(''));
        } catch (error) {
            $('#goodComments').html('<li>Error al cargar los buenos comentarios.</li>');
        }

        // Fetch y actualizar malos comentarios
        try {
            const badComments = await fetchProductData(`${apiUrl}worst_comments/${product}`);
            $('#badComments').html(badComments.map(comment => `<li>${comment}</li>`).join(''));
        } catch (error) {
            $('#badComments').html('<li>Error al cargar los malos comentarios.</li>');
        }

        // Fetch y actualizar resumen
        try {
            const summary = await fetchProductData(`${apiUrl}op_general/${product}`);
            $('#commentSummary').text(summary);
        } catch (error) {
            $('#commentSummary').text('Error al cargar el resumen.');
        }

        // Fetch y actualizar calificaciones
        const categories = ['Tiempo de entrega', 'Calidad de los materiales', 'Comodidad de uso', 'Estética', 'Precio'];
        for (let i = 1; i < categories.length + 1; i++) {
            try {
                const data = await fetchProductData(`${apiUrl}review/${product}/${i}`);
                $('#ratings').append(`
                    <span>${categories[i - 1]}:</span> 
                    <div class="rating-item">
                        <span>${data}</span>
                    </div>
                `);
            } catch (error) {
                $('#ratings').append(`
                    <div class="rating-item">
                        <span>${categories[i]}:</span>
                        <span>Error al cargar</span>
                    </div>
                `);
            }
        }

        $('#queryCard').fadeOut(300, function() {
            $('#productInfo').fadeIn(300);
        });
    } catch (error) {
        console.error('Error:', error);
        alert('Error al cargar la información del producto. Por favor, intenta de nuevo más tarde.');
    } finally {
        // Hide loading screen
        toggleLoadingScreen(false);
    }
}


function showQueryCard() {
    $('#productInfo').fadeOut(300, function() {
        $('#queryCard').fadeIn(300);
    });
}

function typeWriter(text, element, i, fnCallback) {
    if (i < text.length) {
        element.html(text.substring(0, i+1));
        setTimeout(function() {
            typeWriter(text, element, i + 1, fnCallback)
        }, 20);
    } else if (typeof fnCallback == 'function') {
        setTimeout(fnCallback, 700);
    }
}

function startTyping(text) {
    let container = $('#modelResponse');
    container.html('<div class="typing-container form-control"><span class="typing-text "></span></div>');
    let element = container.find('.typing-text');
    typeWriter(text, element, 0, function() {
        element.removeClass('typing-text');
    });
}



async function submitQuery() {
    const query = $('#queryInput').val().trim();
    if (!query) {
        alert('Por favor, ingresa tu consulta.');
        return;
    }
    
    // Mostrar indicador de carga
    $('#modelResponse').html('<div class="spinner-border" role="status"><span class="sr-only">Cargando...</span></div>');
    
    try {
        const response = await fetch(`${apiUrl}ask`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: query }),
        });
        
        if (!response.ok) {
            throw new Error('Error en la solicitud de red');
        }

        const jsonData = await response.json();
        
        // Verifica si la respuesta es una cadena JSON y la analiza si es necesario
        let formattedResponse;
        try {
            formattedResponse = JSON.parse(jsonData);
            // Si es un objeto, lo convertimos a una cadena formateada
            if (typeof formattedResponse === 'object') {
                formattedResponse = JSON.stringify(formattedResponse, null, 2);
            }
        } catch (e) {
            // Si no es JSON válido, usamos la respuesta tal cual
            formattedResponse = jsonData;
        }
        
        // Reemplaza los saltos de línea con <br> para HTML
        formattedResponse = formattedResponse.replace(/\n/g, '<br>');
        
        startTyping(formattedResponse);
        
    } catch (error) {
        console.error('Error:', error);
        startTyping('Hubo un problema con la solicitud. Por favor, intenta de nuevo más tarde.');
    }
}

$(document).ready(function() {
    loadProducts();

    $('#productSelect').change(function() {
        const product = $(this).val();
        if (product) {
            updateProductInfo(product);
        } else {
            showQueryCard();
        }
    });

    $('#submitQuery').click(submitQuery);

    // Agregar manejo de la tecla Enter en el campo de entrada
    $('#queryInput').keypress(function(e) {
        if(e.which == 13) { // 13 es el código de la tecla Enter
            submitQuery();
            return false; // Previene el comportamiento por defecto del Enter
        }
    });

    showQueryCard();
});