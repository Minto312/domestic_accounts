const options = ['date','kind','price']

let incomeList = new List('income', options)
let paymentList = new List('payment', options)

window.onload = () => {

    // ------------------- List -------------------
    $('#income-add-button').on('click', () => {
        $('#list-add-container').css('display', 'flex');
        $('#income-or-payment').val('income');
    })
    $('#payment-add-button').on('click', () => {
        $('#list-add-container').css('display', 'flex');
        $('#income-or-payment').val('payment');
    })
    // ------------------- List -------------------

}