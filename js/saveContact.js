
var firebaseConfig = {
  apiKey: "AIzaSyAp6LDqQa7iO2JQzVfQ1b3lzFvJFOty2b4",
  authDomain: "customer-contacts-77b23.firebaseapp.com",
  databaseURL: "https://customer-contacts-77b23.firebaseio.com",
  projectId: "customer-contacts-77b23",
  storageBucket: "customer-contacts-77b23.appspot.com",
  messagingSenderId: "235336606950",
  appId: "1:235336606950:web:39a130fc75a0153a0bc727",
  measurementId: "G-21QD7Q13HD"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore()

//Listen to form submit

document.getElementById('contactForm').addEventListener('submit',submitForm)

function submitForm(e){
    e.preventDefault();
    var telNumber = document.getElementById('telNumber').value;

    if(telNumber.length >= 10){
      saveNumber(telNumber)
    }
    else{
      Swal.fire({
        title: "<i>Please enter your conatct number</i>",
        html: " So that we can set up your free trail.</b>",
        confirmButtonText: "Thank you",
      }).then((result) => {
        if (result.value) {
          document.getElementById('telNumber').value = '+91-'
        }
      })
    }
}

function saveNumber(telNumber){
    db.collection('customerInfo').add({
        contact: telNumber,
        date : firebase.firestore.FieldValue.serverTimestamp()
    })

    Swal.fire({
      title: "<i>You have been register for free trail.</i>",
      html: "Our team will get back to you soon</b>",
      confirmButtonText: "Thank you",
    }).then((result) => {
      if (result.value) {
        document.getElementById('telNumber').value = '+91-'
      }
    })


}
