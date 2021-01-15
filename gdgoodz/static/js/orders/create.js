$(document).ready(function() {

    // Disable submit when enter pressed
    $(window).keydown(function(event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });

    // Fetch suppliers
    $.ajax({
        url: '/suppliers/fetchall',
        success: function(data) {
            $.each(data, function(key, value) {
                supplierId = value.id;
                supplierName = value.name;

                // Create an option element
                var supplierOption = $('<option value="' + supplierId + '">' + supplierName + '</option>');

                // Append to the supplier select
                $('#supplierSelect').append(supplierOption);
            });
        },
        error: function(err) {
            console.error(err);
        }
    });

    // Search products
    $('#searchBtn').on('click', function() {
        $.ajax({
            url: '/products/search/' + $('#searchTerm').val(),
            success: function(data) {
                $.each(data, function(key, value) {
                    p_id = value.id;
                    p_name = value.name;
                    p_sku = value.sku;
                    p_cost_per_unit = value.cost_per_unit;

                    var product_ul = $('<ul style="width: 100%;"></ul>');

                    var id_li = $('<li>ID: ' + p_id + '</li>');
                    var name_li = $('<li>Name: ' + p_name + '</li>');
                    var sku_li = $('<li>SKU: ' + p_sku + '</li>');
                    var cost_li = $('<li>Cost Per Unit: ' + p_cost_per_unit + '</li>');

                    var qty_label = $('<label for="quantity" style="padding-right: 10px; width: 30%;">Quantity</label>');
                    var qty_input = $('<input type="number" step="1" name="quantity" class="qty-input" style="width: 70%">');

                    var qty_li = $('<li></li>').append(qty_label).append(qty_input);

                    var add_btn = $('<button type="button" class="btn btn-primary add-btn" style="width: 100%;">Add</button>');

                    // Add button click event
                    $(add_btn).on('click', function() {
                        var card = $('<div class="card bg-default mb-3" style="max-width: 18rem;"></div>');

                        var card_header = $('<div class="card-header text-white bg-primary">' + p_name + '</div>');
                        card.append(card_header);

                        var card_body = $('<div class="card-body"></div>');
                        card.append(card_body);

                        // var card_title = $('<h6 class="card-title">' + p_name + '</h6>');
                        // card_body.append(card_title);

                        var card_text = $('<p class="card-text"><b>ID: </b>' + p_id + '<br><b>SKU: </b>' + p_sku + '<br><b>Quantity: </b>' + $(qty_input).val() + '<br><b>Cost Per Unit: </b>' + p_cost_per_unit + '</p>');
                        card_body.append(card_text);

                        // Remove product button
                        var removeBtn = $('<button type="button" class="btn btn-outline-danger remove-btn" style="box-shadow: ">Remove</button>');
                        card_body.append(removeBtn);

                        $('#addedProductCards').append(card);

                        $(this).prop('disabled', true);
                    });

                    product_ul.append(id_li);
                    product_ul.append(name_li);
                    product_ul.append(sku_li);
                    product_ul.append(qty_li);
                    product_ul.append(cost_li);

                    product_ul.append(add_btn);

                    $('#productMatches').html('').append(product_ul);
                });
            },
            error: function(err) {
                console.error(err);
            }
        });
    });
});