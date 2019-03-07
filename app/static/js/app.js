var products = [
        {
            'id': 1001,
            'title': 'Soap',
            'price': 3.98,
            'desc': 'Very clean soapy soap, descriptive text'
        },
        {
            'id': 1002,
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'A bundle of grapey grapes, yummy'
        },
        {
            'id': 1003,
            'title': 'Pickles',
            'price': 5.67,
            'desc': 'A jar of pickles is pickly'
        },
        {
            'id': 1004,
            'title': 'Juice',
            'price': 2.68,
            'desc': 'Yummy orange juice'
        }
    ]

    /******************************
    Start cart operation functions
    ******************************/

    // create add item function to push to cart
    function addItem(id) {
      // clear session storage
      // sessionStorage.clear();

      // check to see if a cart key exists in session storage
      if (sessionStorage.getItem('cart')) {
        // if it does, set a local cart variable to work with, using the parsed string //JSON is js library
        var cart = JSON.parse(sessionStorage.getItem('cart'));
      } else {
        // if it does not exist, set an empty array
        var cart = [];
      }

      // loop through global products variable and push to Cart
      for (let i in products) {
        if (products[i].id == id) {
          cart.push(products[i]);
          break;
        }
      }

      // // call total function to update
      // calcTotal();

      // store the cart into the session storage
      sessionStorage.setItem('cart', JSON.stringify(cart));
    }


    // create a removeItem function that splices the given item
    function removeItem(id) {
      // get cart key from session storage and parse it into an object
      let cart = JSON.parse(sessionStorage.getItem('cart'));

      // loop through all items in the cart
      for (let i in cart) {
        // check if the id passed in is the same as the current item
        if (cart[i].id == id) {
          // if it is, remove it, and break
          cart.splice(i, 1);
          break;
        }
      }

      // add stringified cart to session storage under cart key
      sessionStorage.setItem('cart', JSON.stringify(cart));

      // call showCart again
      showCart();
    }

    // calculating and returning the total
    function calcTotal() {
      // get the value and parse from session storage
      let cart = JSON.parse(sessionStorage.getItem('cart'));

      // define a total variable = 0
      let total = 0;

      // loop through all items in the cart
      for (let i in cart) {
        // add each item's price to total
        total += cart[i].price;
      }

      // return the total
      return total.toFixed(2);
    }


    // updating all classes with total being displayed
    function updateTotals() {
      // define a total variable from the return of calcTotal
      let total = calcTotal();

      // insert that total into all places that render the total price
      $('.total').text(`$${total}`);

      //convert total to cents
      total = total * 100;
      total = Math.ceil(total);

      // insert form into id of pay
      let html = `
      <form action="/pay/?amount=${total}" method="POST">
        <script
          src="https://checkout.stripe.com/checkout.js" class="stripe-button"
          data-key="pk_test_SBvNgQvCWDApohiofKwLw5eb"
          data-amount="${total}"
          data-name="Demo Site"
          data-description="Widget"
          data-image="https://stripe.com/img/documentation/checkout/marketplace.png"
          data-locale="auto">
        </script>
      </form>`;

      $('#pay').html(html);
    }

    function countDuplicates(id) {
      let cart = JSON.parse(sessionStorage.getItem('cart'));
      let count = 0;
      for (let i in cart) {
        if (cart[i].id == id) {
          count += 1
        }
      }
      return count;
    }


    // create a showCart method to render all items within the cart variable
    function showCart() {
      // get the value and parse from session storage
      let cart = JSON.parse(sessionStorage.getItem('cart'));

      if (cart === null) {
        cart = [];
      }
      // if cart is empty set the table in the cart col md 3 section to display none
      if (cart.length === 0) {
        $('#cart').css('display', 'none');
        $('#empty').text('You have no item in your cart.');
      } else {
        // otherwise show table by setting display to block, loop over all items in cart and create a new row for each item.
        $('#cart').css('display', 'block');

        let html = '';

        let duplicates = [];

        for (let i in cart) {
          let count = countDuplicates(cart[i].id);

          if (duplicates.indexOf(cart[i].id)== -1) {
            html += `
              <tr>
                <td>${count}</td>
                <td>${cart[i].title}</td>
                <td>$${(cart[i].price*count).toFixed(2)}</td>
                <td>
                <button onClick="removeItem(${cart[i].id})" class="btn btn-danger">X</button>
                </td>
              </tr>
            `;
            duplicates.push(cart[i].id);
          }
        }


        // send the proper string into the tbody section
        $('tbody').html(html);
      }
      // call update totals
      updateTotals();
    }


    showCart();

    /******************************
    End cart operation functions
    ******************************/
