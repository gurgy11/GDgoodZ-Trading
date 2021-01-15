$(document).ready(function() {

    $('#calcFinalCostBtn').on('click', function() {
        var costPerUnit = $('#costPerUnit').val();
        var orderQuantity = $('#orderQuantity').val();
        var shippingCost = $('#shippingCost').val();

        calculateFinalCostPerUnit(costPerUnit, orderQuantity, shippingCost);
    });

    function calculateFinalCostPerUnit(costPerUnit, orderQuantity, shippingCost) {
        var allUnitsCost = costPerUnit * orderQuantity;
        console.log(allUnitsCost);

        var totalCost = parseFloat(allUnitsCost) + parseFloat(shippingCost);
        console.log(totalCost);

        $('#finalCostPerUnit').html('$ ' + totalCost);
    }
});