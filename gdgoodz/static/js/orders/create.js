$(document).ready(function() {

    var products = Array();
    var order = Array();

    $('#searchBtn').on('click', function() {

        $('#productMatches').html('');

        $.ajax({
            url: '/products/search/' + $('#searchTerm').val(),
            success: function(data) {
                $.each(data, function(key, value) {
                    var id = value.id;
                    var name = value.name;
                    var sku = value.sku;
                    var quantity = value.quantity;
                    var costPerUnit = value.cost_per_unit;

                    var product = {
                        id: id,
                        name: name,
                        sku: sku,
                        quantity: quantity,
                        cost_per_unit: costPerUnit
                    };
                    products.push(product);

                    var card = $('<div class="card bg-default mb-3" style="max-width: 18rem;"></div>');
                    var header = $('<div class="card-header text-white bg-primary">' + product.name + '</div>');
                    var body = $('<div class="card-body"></div>');
                    var text = $('<p class="card-text">' +
                        '<b>Id: </b>' + product.id + '<hr>' +
                        '<b>Name: </b>' + product.name + '<hr>' +
                        '<b>SKU: </b>' + product.sku + '<hr>' +
                        '<b>Quantity: </b>' + product.quantity + '<hr>' +
                        '<b>Cost Per Unit: </b>' + product.cost_per_unit + '</p>');
                    var qtyLabel = $('<label for="qty_input">Amount: </label>');
                    var qtyInput = $('<input type="number" step="1" name="qty_input">');
                    var addBtn = $('<button type="button" class="add-btn btn btn-outline-primary">Add</button>');

                    body.append(text);
                    body.append(qtyLabel);
                    body.append(qtyInput);
                    body.append(addBtn);

                    card.append(header);
                    card.append(body);

                    $('#productMatches').append(card);
                });
            },
            error: function(err) {
                console.log(err);
            }
        });
    });
});