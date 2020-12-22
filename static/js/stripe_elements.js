const stripePublicKey = $("#id_stripe_public_key").text().slice(1,-1);
let clientSecret = $("#id_client_secret").text().slice(1,-1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
const card = elements.create('card', {hidePostalCode : true, style : style}); //eircode in future
card.mount("#card-element");

/* Realtime Validation */
card.addEventListener("change", function(e){
    let errorDiv = document.getElementById("card-errors");
    if(e.error){
        let html = `
        <span class="icon" role="alert"><i class="fas fa-times"></i></span>
        <span>${e.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    }else{
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});