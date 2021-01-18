$(document).ready(function() {

    var order = Array();

    $('#searchBtn').on('click', function() {
        searchProducts($('#searchTerm').val());
    });

    $('#createOrderForm').on('submit', function(e) {

        e.preventDefault();

        var form = new FormData();

        form.set('supplier', $('#supplierSelect').val());
        form.set('products', $(order).serializeArray());
        form.set('shipping_cost', $('#shippingCost').val());
        form.set('delivery_date', $('#deliveryDate').val());
        form.set('delivery_address', $('#deliveryAddress').val());
        form.set('status', $('#status').val());
        form.set('notes', $('#notes').val());

        $.ajax({
            url: '/orders/create',
            type: 'POST',
            data: $(form).serializeArray(),
            success: function() {
                window.location.href = '/orders/index';
            }
        });
    });

    function searchProducts(searchTerm) {
        $.ajax({
            url: '/products/search/' + searchTerm,
            success: function(data) {

                $('#productMatchesTable tbody').html('');

                $.each(data, function(key, value) {
                    var tr = $('<tr></tr>');

                    var idTd = $('<td>' + value.id + '</td>');
                    var nameTd = $('<td>' + value.name + '</td>');
                    var skuTd = $('<td>' + value.sku + '</td>');
                    var inStockTd = $('<td>' + value.quantity + '</td>');
                    var costTd = $('<td>' + value.cost_per_unit + '</td>');
                    var orderQtyTd = $('<td></td>');
                    var addTd = $('<td></td>');

                    var qtyInput = $('<input type="number" step="1" class="form-control"></input>');
                    var addBtn = $('<button type="button" class="add-btn btn btn-success">Add</button>');

                    orderQtyTd.append(qtyInput);
                    addTd.append(addBtn);

                    tr.append(idTd);
                    tr.append(nameTd);
                    tr.append(skuTd);
                    tr.append(inStockTd);
                    tr.append(costTd);
                    tr.append(orderQtyTd);
                    tr.append(addTd);

                    $('#productMatchesTable tbody').append(tr);

                    $(addBtn).on('click', function() {
                        var orderItem = {
                            id: value.id,
                            name: value.name,
                            sku: value.sku,
                            in_stock: value.quantity,
                            cost_per_unit: value.cost_per_unit,
                            order_quantity: $(qtyInput).val()
                        };
                        order.push(orderItem);
                        $(qtyInput).val('');
                        console.log(order);
                    });
                });
            },
            error: function(err) {
                console.error(err);
            }
        });
    }
});