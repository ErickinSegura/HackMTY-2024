const products = {
    1: {
        name: "Producto A",
        image: "https://via.placeholder.com/400x300.png?text=Producto+A",
        goodComments: ["Excelente calidad", "Entrega rápida", "Muy cómodo de usar"],
        badComments: ["Un poco caro", "El empaque podría mejorar", "Instrucciones poco claras"],
        summary: "En general, los usuarios están satisfechos con el Producto A. La mayoría de las críticas se centran en el precio y las instrucciones de uso.",
        ratings: {
            "Tiempo de entrega": 4.5,
            "Calidad de los materiales": 4,
            "Comodidad de uso": 3.5,
            "Estética": 4,
            "Precio": 3
        }
    },
    2: {
        name: "Producto B",
        image: "https://via.placeholder.com/400x300.png?text=Producto+B",
        goodComments: ["Diseño innovador", "Buena relación calidad-precio", "Fácil de usar"],
        badComments: ["Entregas lentas", "Calidad inconsistente", "Servicio al cliente mejorable"],
        summary: "El Producto B tiene opiniones mixtas. Los usuarios aprecian su diseño y facilidad de uso, pero hay preocupaciones sobre la consistencia de la calidad y los tiempos de entrega.",
        ratings: {
            "Tiempo de entrega": 3,
            "Calidad de los materiales": 3.5,
            "Comodidad de uso": 4,
            "Estética": 4.5,
            "Precio": 4
        }
    },
    3: {
        name: "Producto C",
        image: "https://via.placeholder.com/400x300.png?text=Producto+C",
        goodComments: ["Muy duradero", "Excelente atención al cliente", "Packaging eco-friendly"],
        badComments: ["Precio elevado", "Curva de aprendizaje empinada", "Diseño poco atractivo"],
        summary: "El Producto C es apreciado por su durabilidad y el compromiso de la empresa con la sostenibilidad. Sin embargo, algunos usuarios consideran que el precio es alto y que el producto puede ser difícil de usar al principio.",
        ratings: {
            "Tiempo de entrega": 4,
            "Calidad de los materiales": 5,
            "Comodidad de uso": 3,
            "Estética": 3,
            "Precio": 2.5
        }
    }
};

function updateProductInfo(productId) {
    const product = products[productId];
    if (!product) return;

    $('#productName').text(product.name);
    $('#productImage').attr('src', product.image);
    
    $('#goodComments').html(product.goodComments.map(comment => `<li>${comment}</li>`).join(''));
    $('#badComments').html(product.badComments.map(comment => `<li>${comment}</li>`).join(''));
    
    $('#commentSummary').text(product.summary);
    
    $('#ratings').html(Object.entries(product.ratings).map(([category, rating]) => `
        <div class="rating-item">
            <span>${category}:</span>
            <span>${rating}/5</span>
        </div>
    `).join(''));

    $('#productInfo').show();
}

$(document).ready(function() {
    $('#productSelect').change(function() {
        const productId = $(this).val();
        if (productId) {
            updateProductInfo(productId);
        } else {
            $('#productInfo').hide();
            alert('Por favor, selecciona un producto.');
        }
    });
});





