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
                    console.log(product);
                    arr.push(product);
                });
            },
            error: function(err) {
                console.error(err);
            }
        });
        return arr;
    }
});