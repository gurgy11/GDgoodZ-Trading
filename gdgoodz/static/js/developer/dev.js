$(document).ready(function() {

    var products_arr = Array();
    fetchAllProducts(products_arr);

    function fetchAllProducts(arr) {
        $.ajax({
            url: '/developer/fetchall/products',
            success: function(data) {
                $.each(data, function(key, value) {
                    var product = {
                        id: value.id,
                        name: value.name,
                        category: value.category,
                        description: value.description,
                        sku: value.sku,
                        status: value.status,
                        supplier: value.supplier,
                        country_of_origin: value.country_of_origin,
                        quantity: value.quantity,
                        quantity_sold: value.quantity_sold,
                        cost_per_unit: value.cost_per_unit,
                        price_per_unit: value.price_per_unit,
                        notes: value.notes,
                        created_at: value.created_at,
                        updated_at: value.updated_at,
                    };
                    arr.push(product);
                });
                $.each(products_arr, function(key, value) {
                    var pId = value.id;
                    var pName = value.name;
                    var pCategory = value.category;
                    var pSku = value.sku;
                    var pStatus = value.status;
                    var pQuantity = value.quantity;
                    var pCostPerUnit = value.cost_per_unit;
                    var pPricePerUnit = value.price_per_unit;

                    var card = $('<div class="card bg-default mb-3" style="max-width: 18rem;"></div>');
                    var cardHeader = $('<div class="card-header text-white bg-primary">' + pName + '</div>');
                    var cardBody = $('<div class="card-body"></div>');
                    var cardTitle = $('<h5 class="card-title"></h5>');
                    var cardText = $('<p class="card-text">' +
                        '<b>Name: </b>' + pName + '<hr>' +
                        '<b>Category: </b>' + pCategory + '<hr>' +
                        '<b>SKU: </b>' + pSku + '<hr>' +
                        '<b>Status: </b>' + pStatus + '<hr>' +
                        '<b>Quantity: </b>' + pQuantity + '<hr>' +
                        '<b>Cost Per Unit: </b>' + pCostPerUnit + '</p><br>');
                    var addBtn = $('<button type="button" class="add-btn btn btn-outline-primary form-control">Add</button>');

                    cardBody.append(cardTitle);
                    cardBody.append(cardText);
                    cardBody.append(addBtn);

                    card.append(cardHeader);
                    card.append(cardBody);
                    console.log(card);
                    $('#productCards').append(card);
                });
            },
            error: function(err) {
                console.error(err);
            }
        });
        return arr;
    }
});